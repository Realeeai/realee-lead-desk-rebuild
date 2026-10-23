"""Run one arm of the rebuild test: every lead in questions.md, in order, one fresh session each.

    python harness/run_arms.py original 1
    python harness/run_arms.py rebuild 1
    python harness/run_arms.py original 1 --model claude-haiku-5-5 --effort low
                                                     another model or effort level;
                                                     writes run-original/claude-haiku-5-5-low/run-1/

original  system prompt = harness/base-system-prompt.txt + the judged folder in original/ (seven files)
rebuild   system prompt = the same line + the rebuilt folder in rebuild/ (three files)
Both use the same wrapper and label every file `lead-desk/<name>`, so the files are the only difference.
The default is claude-opus-5-5 at effort high, the setting the Comp #14 entry was judged on.

Writes run-<arm>/run-<n>/:
  q<N>.json          the CLI's JSON output, byte for byte (stderr beside it if there was any)
  system-prompt.txt  exactly what was passed as the system prompt
  run-info.json      model, effort, CLI version, the command, the repo commit, start and end times
  transcript.md      each prompt and reply, rendered from the .json files with no edits

A question that times out gets q<N>.timeout.txt instead of q<N>.json and grades as a fail; the run
continues. A call Claude Code itself fails (`is_error` in its JSON: a usage limit, a model this
account can't use) stops the run: its q<N>.json is kept, run-info.json records `stopped_on_error`,
and the exit code is 3. That run is incomplete and not graded; the next try gets a new number.
Runs are never overwritten. Copied from realee-lead-desk-control's runner, with the arms changed.
Needs Claude Code on PATH and logged in. Standard library only.
"""
import argparse
import datetime
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from grade import QUESTIONS, REPO, parse_questions

MODEL = "claude-opus-5-5"
EFFORT = "high"
EFFORTS = ("low", "medium", "high", "xhigh", "max")
TIMEOUT = 600  # seconds per question
# Each arm's folder and the files it loads, in order. original/ is the judged folder (Comp #14,
# commit a887b92 of realee-lead-desk-control); rebuild/ is the folder after the feedback.
ARMS = {
    "original": ("original", ["README.md", "identity.md", "rules.md", "examples.md",
                              "reference/icp.md", "reference/intake-script.md", "reference/output-format.md"]),
    "rebuild": ("rebuild", ["README.md", "rules.md", "reference/intake-script.md"]),
}
# --safe-mode: no CLAUDE.md, memory, skills, plugins or hooks. --tools "": no tools.
# --strict-mcp-config with no config: no MCP servers. Each question is its own session.
def cli_flags(model, effort):
    return [
        "-p", "--safe-mode", "--tools", "", "--strict-mcp-config", "--no-session-persistence",
        "--model", model, "--effort", effort, "--output-format", "json",
    ]


def system_prompt(arm):
    base = (REPO / "harness" / "base-system-prompt.txt").read_text(encoding="utf-8").strip()
    folder, names = ARMS[arm]
    parts = [base, "", "The following folder is loaded for this conversation.", ""]
    for name in names:
        body = (REPO / folder / name).read_text(encoding="utf-8").strip()
        parts += [f'<file path="lead-desk/{name}">', body, "</file>", ""]
    return "\n".join(parts)


def fence(text):
    """A code fence longer than any backtick run inside text, so replies render unchanged."""
    longest, run = 0, 0
    for ch in text:
        run = run + 1 if ch == "`" else 0
        longest = max(longest, run)
    return "`" * max(4, longest + 1)


def main():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("arm", choices=ARMS)
    parser.add_argument("number", type=int)
    parser.add_argument("questions", nargs="?")
    parser.add_argument("--model", default=MODEL)
    parser.add_argument("--effort", default=EFFORT, choices=EFFORTS)
    args = parser.parse_args()
    arm, number, model, effort = args.arm, str(args.number), args.model, args.effort
    questions_path = Path(args.questions).resolve() if args.questions else QUESTIONS
    claude = shutil.which("claude")
    if not claude:
        sys.exit("Claude Code (`claude`) is not on PATH")
    flags = cli_flags(model, effort)
    run_name = f"run-{number}" if questions_path == QUESTIONS else f"{questions_path.stem}-run-{number}"
    cell = "" if (model, effort) == (MODEL, EFFORT) else f"{model}-{effort}/"
    out = REPO / f"run-{arm}" / f"{cell}{run_name}"
    if out.exists():
        sys.exit(f"{out} already exists. Runs are never overwritten; use the next number.")

    template, questions = parse_questions(questions_path)
    out.mkdir(parents=True)
    prompt_file = out / "system-prompt.txt"
    prompt_file.write_text(system_prompt(arm), encoding="utf-8", newline="\n")
    version = subprocess.run([claude, "--version"], capture_output=True, text=True).stdout.strip()
    git = ["git", "-C", str(REPO)]
    commit = subprocess.run([*git, "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
    uncommitted = subprocess.run([*git, "status", "--porcelain", "--", "original", "rebuild", "harness", str(questions_path)],
                                 capture_output=True, text=True).stdout.strip()
    info = {
        "arm": arm,
        "run": int(number),
        "questions_file": questions_path.relative_to(REPO).as_posix() if questions_path.is_relative_to(REPO) else questions_path.name,
        "model": model,
        "effort": effort,
        "claude_code_version": version,
        "repo_commit": commit,
        "uncommitted_changes_to_folder_questions_or_harness": uncommitted.splitlines(),
        "command": ["claude", *flags, "--system-prompt-file", f"run-{arm}/{cell}{run_name}/system-prompt.txt"],
        "prompt_delivery": "stdin, one fresh session per question, from an empty temporary folder",
        "questions": [q["id"] for q in questions],
        "started_at": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    }

    transcript = [f"# run-{arm} {cell}{run_name}", "",
                  f"Rendered from the q<N>.json files in this folder, no edits. Model `{model}`, effort `{effort}`, {version}.",
                  "System prompt: `system-prompt.txt` in this folder.", ""]
    for q in questions:
        prompt = template.replace("{lead}", q["lead"])
        stem = q["id"].lower()
        try:
            with tempfile.TemporaryDirectory(prefix="lead-desk-run-") as empty:
                done = subprocess.run(
                    [claude, *flags, "--system-prompt-file", str(prompt_file)],
                    input=prompt.encode("utf-8"), capture_output=True, cwd=empty, timeout=TIMEOUT,
                )
        except subprocess.TimeoutExpired:
            # Recorded, not retried: a timeout counts as a failed answer (no qN.json) and the run goes on.
            stats = f"timed out after {TIMEOUT} s, no answer"
            (out / f"{stem}.timeout.txt").write_text(stats + "\n", encoding="utf-8", newline="\n")
            transcript += [f"## {q['id']}", "", f"_{stats}_", ""]
            print(f"{arm} run {number} {q['id']}: {stats}", flush=True)
            continue
        (out / f"{stem}.json").write_bytes(done.stdout)
        if done.stderr.strip():
            (out / f"{stem}.stderr.txt").write_bytes(done.stderr)
        try:
            raw = json.loads(done.stdout.decode("utf-8"))
            reply = raw.get("result") or ""
            stats = f"{raw.get('duration_ms', 0) / 1000:.1f} s · {(raw.get('usage') or {}).get('output_tokens', '?')} output tokens · session {raw.get('session_id', '?')}"
        except (ValueError, UnicodeDecodeError):
            raw, reply, stats = {}, done.stdout.decode("utf-8", "replace"), f"exit code {done.returncode}, output was not JSON"
        f_prompt, f_reply = fence(prompt), fence(reply)
        transcript += [f"## {q['id']}", "", f"_{stats}_", "", "**Prompt (sent on stdin, exact):**", "",
                       f_prompt + "text", prompt, f_prompt, "", "**Reply:**", "", f_reply + "text", reply, f_reply, ""]
        print(f"{arm} run {number} {q['id']}: {stats}", flush=True)
        if raw.get("is_error"):
            # The CLI failed, not the model: no answer to grade, so stop rather than spend the rest.
            info["stopped_on_error"] = {"question": q["id"], "message": reply[:300]}
            print(f"{arm} run {number} stopped on a CLI error at {q['id']}: {reply[:120]}", flush=True)
            break

    info["finished_at"] = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    (out / "run-info.json").write_text(json.dumps(info, indent=2) + "\n", encoding="utf-8", newline="\n")
    (out / "transcript.md").write_text("\n".join(transcript), encoding="utf-8", newline="\n")
    if "stopped_on_error" in info:
        sys.exit(3)


if __name__ == "__main__":
    main()

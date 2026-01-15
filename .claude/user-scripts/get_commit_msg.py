"""A hook handler script that get the commit message from `/commit` command."""

import json
import sys
from pathlib import Path


def main():
    try:
        input_data: dict = json.load(sys.stdin)
    except json.JSONDecodeError as e:
        print(f"error: invalid JSON input: {e}", file=sys.stderr)
        # Exit code 1 shows stderr to the user but not to Claude
        sys.exit(1)

    # The `/commit` command is executed by the `commit-hook` subagent.
    transcript_path = input_data.get("agent_transcript_path")
    if not transcript_path:
        print(
            "error: key 'agent_transcript_path' not found in JSON input.",
            file=sys.stderr,
        )
        sys.exit(1)

    with Path(transcript_path).open("r") as f:
        records = [json.loads(line) for line in f if line.strip()]
    responses = [r for r in records if r["type"] == "assistant"]
    if responses:
        text = responses[-1]["message"]["content"][0]["text"]
        sys.stdout.write(text)
        sys.stdout.flush()


if __name__ == "__main__":
    main()

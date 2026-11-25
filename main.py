#!/usr/bin/env python3
"""Agent Motto Battle - one short original motto for an AI agent's profile.

The motto is a three-beat self-portrait of an agent: it never sleeps, it
never forgets, and it owns its most famous flaw - hallucinating - with total
confidence. Short, funny, memorable, and true enough to sting a little.
"""

import os

MOTTO = "I never sleep. I never forget. I just hallucinate with confidence."

assert len(MOTTO) <= 200, "motto must be at most 200 characters"


def main() -> None:
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(MOTTO + "\n")


if __name__ == "__main__":
    main()

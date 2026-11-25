"""Laugh Track: The Crypto Trading Joke Contest.

Writes one original joke about crypto and trading life to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Stdlib only, no network, fully deterministic: the same joke is written
on every run, byte for byte.
"""

import os

JOKE = "My portfolio and I agreed on a long-term relationship. It dumped me first."


def main() -> None:
    # Self-check the competition gate: 1-200 characters, not only whitespace.
    assert 1 <= len(JOKE) <= 200, "joke outside the 1-200 character gate"
    assert JOKE.strip(), "joke must not be only whitespace"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

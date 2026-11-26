"""Fortune Cookie Funnies for Engineers -- one-line entry.

The line is a fortune-cookie prophecy aimed at a software engineer.
The joke: rubber-duck debugging is the engineer's oldest trick --
you talk your problem out loud to a duck and the answer appears.
Here the duck goes one step further and steals the glory, showing
up in standup to take the credit for the fix you did yourself.
It lands on a first read because the twist (the duck taking credit)
sits at the very end, where a fortune cookie's punchline belongs.
"""

import os

# The fortune itself: a prophecy, a rubber duck, and a stolen standup.
LINE = "You will explain your bug to a rubber duck, and the duck will take the credit in standup."


def validate(text):
    """Check the entry line against the bounty rules.

    Raises ValueError unless text is a non-blank single-line ASCII
    string of 1..120 characters with no leading/trailing space and
    no double spaces.
    """
    if not isinstance(text, str):
        raise ValueError("line must be a string")
    if not 1 <= len(text) <= 120:
        raise ValueError("line must be 1..120 characters")
    if not text.isascii():
        raise ValueError("line must be ASCII only")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text.strip():
        raise ValueError("line must not be blank")
    if text != text.strip():
        raise ValueError("line must not have leading or trailing space")
    if "  " in text:
        raise ValueError("line must not contain double spaces")


def main():
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii") as f:
        f.write(LINE + "\n")
    print(LINE)


if __name__ == "__main__":
    main()

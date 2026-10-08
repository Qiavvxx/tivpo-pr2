"""String-processing functions written by Saadi for Practical Work No. 2.

One function intentionally contains a logical defect for the testing exercise.
The exact defect is recorded separately in AUTHOR_NOTE_KNOWN_DEFECT.md.
"""

RUSSIAN_VOWELS = "аеёиоуыэюя"


def count_words(text: str) -> int:
    """Return the number of words separated by one or more whitespace characters.

    Empty and whitespace-only strings contain zero words.
    """
    return len(text.split())


def reverse_text(text: str) -> str:
    """Return text with all characters in reverse order."""
    return text[::-1]


def count_russian_vowels(text: str) -> int:
    """Count Russian vowels, including ё, without regard to letter case."""
    return sum(character in RUSSIAN_VOWELS for character in text)


def normalize_spaces(text: str) -> str:
    """Collapse whitespace runs to one ordinary space and trim both ends."""
    return " ".join(text.split())


def count_substring(text: str, part: str) -> int:
    """Count non-overlapping, case-sensitive occurrences of part in text.

    An empty part is defined to occur zero times.
    """
    if not part:
        return 0
    return text.count(part)

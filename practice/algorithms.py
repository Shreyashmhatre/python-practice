import math
import re
from collections import Counter
from collections.abc import Iterable, Sequence
from statistics import mean, median
from typing import TypeVar

T = TypeVar("T")


def normalize_words(text: str) -> list[str]:
    """Extract Unicode letters; punctuation, underscores, and numbers separate words."""
    return re.findall(r"[^\W\d_]+", text.casefold(), flags=re.UNICODE)


def word_frequencies(text: str) -> dict[str, int]:
    return dict(Counter(normalize_words(text)))


def is_palindrome(text: str) -> bool:
    normalized = "".join(c for c in text.casefold() if c.isalnum())
    return bool(normalized) and normalized == normalized[::-1]


def deduplicate(values: Iterable[T]) -> list[T]:
    """Stable deduplication; elements must be hashable."""
    return list(dict.fromkeys(values))


def chunked(values: Sequence[T], size: int) -> list[list[T]]:
    if type(size) is not int or size <= 0:
        raise ValueError("size must be a positive integer")
    return [list(values[i : i + size]) for i in range(0, len(values), size)]


def flatten_once(values: Iterable[Iterable[T]]) -> list[T]:
    return [item for group in values for item in group]


def is_prime(number: int) -> bool:
    if type(number) is not int:
        raise ValueError("number must be an integer")
    if number < 2:
        return False
    return all(number % divisor for divisor in range(2, math.isqrt(number) + 1))


def primes_up_to(limit: int) -> list[int]:
    if type(limit) is not int or not 0 <= limit <= 100000:
        raise ValueError("limit must be an integer between 0 and 100000")
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for candidate in range(2, math.isqrt(limit) + 1):
        if sieve[candidate]:
            for multiple in range(candidate * candidate, limit + 1, candidate):
                sieve[multiple] = 0
    return [number for number, prime in enumerate(sieve) if prime]


def fibonacci(count: int) -> list[int]:
    if type(count) is not int or count < 0:
        raise ValueError("count must be a nonnegative integer")
    result = []
    a, b = 0, 1
    for _ in range(count):
        result.append(a)
        a, b = b, a + b
    return result


def summarize(values: Iterable[float]) -> dict[str, float | int]:
    numbers = list(values)
    if not numbers or any(
        isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v)
        for v in numbers
    ):
        raise ValueError("provide at least one finite number")
    return {
        "count": len(numbers),
        "minimum": min(numbers),
        "maximum": max(numbers),
        "mean": mean(numbers),
        "median": median(numbers),
    }

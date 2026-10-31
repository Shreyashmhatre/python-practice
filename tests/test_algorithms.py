import json
import subprocess
import sys
import unittest

from practice.algorithms import (
    chunked,
    deduplicate,
    fibonacci,
    flatten_once,
    is_palindrome,
    is_prime,
    normalize_words,
    primes_up_to,
    summarize,
    word_frequencies,
)


class AlgorithmsTests(unittest.TestCase):
    def test_unicode_words_and_counts(self):
        self.assertEqual(
            normalize_words("Hello, WORLD! café 123"), ["hello", "world", "café"]
        )
        self.assertEqual(word_frequencies("Test test, TEST!"), {"test": 3})
        self.assertEqual(normalize_words(""), [])

    def test_palindromes(self):
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama!"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("---"))

    def test_stable_deduplication(self):
        self.assertEqual(deduplicate([3, 1, 3, 2, 1]), [3, 1, 2])
        self.assertEqual(deduplicate(iter(["a", "a", "b"])), ["a", "b"])
        self.assertEqual(deduplicate([]), [])

    def test_chunks_and_flatten(self):
        self.assertEqual(chunked([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunked([], 2), [])
        self.assertEqual(flatten_once([[1], [], [2, 3]]), [1, 2, 3])
        for invalid in [0, -1, True, 1.5]:
            with self.subTest(size=invalid), self.assertRaises(ValueError):
                chunked([1], invalid)

    def test_primes(self):
        for value in [-3, 0, 1, 4, 9, 25]:
            self.assertFalse(is_prime(value))
        for value in [2, 3, 7, 29]:
            self.assertTrue(is_prime(value))
        self.assertEqual(primes_up_to(11), [2, 3, 5, 7, 11])
        self.assertEqual(primes_up_to(0), [])
        for invalid in [-1, 100001, True, 3.5]:
            with self.subTest(limit=invalid), self.assertRaises(ValueError):
                primes_up_to(invalid)
        with self.assertRaises(ValueError):
            is_prime(2.5)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci(0), [])
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_summary(self):
        self.assertEqual(
            summarize([1, 2, 3, 4]),
            {"count": 4, "minimum": 1, "maximum": 4, "mean": 2.5, "median": 2.5},
        )
        for values in [[], [float("nan")], [float("inf")], [True], ["1"]]:
            with self.subTest(values=values), self.assertRaises(ValueError):
                summarize(values)

    def test_cli(self):
        result = subprocess.run(
            [sys.executable, "-m", "practice", "text", "one two one"],
            capture_output=True,
            text=True,
            check=True,
        )
        self.assertEqual(json.loads(result.stdout)["word_count"], 3)
        bad = subprocess.run(
            [sys.executable, "-m", "practice", "primes", "-1"],
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(bad.returncode, 2)


if __name__ == "__main__":
    unittest.main()

# Python Practice

Small, testable exercises in Python fundamentals: strings, numbers, collections,
input validation, and command-line programs. This is a learning repository, not a
claim of advanced algorithm expertise.

## Try it

Python 3.12+; no external packages required.

```bash
python -m practice text "Build small. Test often. Build again."
python -m practice primes 30
python -m unittest discover -s tests -v
```

The text command reports word counts and the five most frequent words. The primes
command lists primes up to an inclusive limit (maximum 100,000).

## Exercises

| Function | Focus | Important behavior |
| --- | --- | --- |
| `normalize_words` | Regex, Unicode, case folding | Punctuation separates words; digits are excluded |
| `word_frequencies` | Dictionaries, counting | Case-insensitive word counts |
| `is_palindrome` | String normalization | Ignores punctuation and case; empty input is false |
| `deduplicate` | Sets and stable order | Keeps the first occurrence of each hashable value |
| `chunked` | Iteration and slicing | Positive integer chunk size required |
| `flatten_once` | Comprehensions | Flattens exactly one level |
| `is_prime` | Arithmetic, loop bounds | Handles values below two |
| `primes_up_to` | Sieve of Eratosthenes | Includes the upper bound when prime |
| `fibonacci` | Iterative state | Returns a requested count, starting at zero |
| `summarize` | Statistics, validation | Requires nonempty finite numeric data |

Code is in [`practice/algorithms.py`](practice/algorithms.py). Tests include empty
inputs, invalid sizes, boundary numbers, order preservation, and CLI errors.

## Practice workflow

1. Read a function's contract and tests.
2. Implement it independently before looking at the solution.
3. Add a boundary case and explain its expected result.
4. Compare readability and complexity, not just whether the test passes.

Next exercises: file parsing, generators, and profiling. These are plans, not
features implemented here.

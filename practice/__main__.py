import argparse
import json

from practice.algorithms import normalize_words, primes_up_to, word_frequencies


def main():
    parser = argparse.ArgumentParser(description="Small Python practice tools")
    commands = parser.add_subparsers(dest="command", required=True)
    text = commands.add_parser("text", help="Count words in supplied text")
    text.add_argument("value")
    primes = commands.add_parser("primes", help="List primes up to an inclusive limit")
    primes.add_argument("limit", type=int)
    args = parser.parse_args()
    if args.command == "text":
        frequencies = word_frequencies(args.value)
        top = sorted(frequencies.items(), key=lambda item: (-item[1], item[0]))[:5]
        result = {
            "word_count": len(normalize_words(args.value)),
            "unique_words": len(frequencies),
            "top_words": dict(top),
        }
    else:
        try:
            result = {"limit": args.limit, "primes": primes_up_to(args.limit)}
        except ValueError as exc:
            parser.error(str(exc))
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

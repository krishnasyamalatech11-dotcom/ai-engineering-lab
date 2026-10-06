"""Alert-log analyzer: count ORA- errors in an Oracle alert log."""
import json
import re
import sys

ORA_PATTERN = re.compile(r"ORA-\d{5}")


def count_errors(path: str) -> dict[str, int]:
    """Return a dictionary of ORA- code -> number of times it appears."""
    counts: dict[str, int] = {}
    with open(path) as f:
        for line in f:
            for code in ORA_PATTERN.findall(line):
                counts[code] = counts.get(code, 0) + 1
    return counts


def print_summary(ranked: dict[str, int]) -> None:
    """Print a table of error codes, highest count first."""
    print(f"{'Error code':<12}{'Count':>6}")
    print("-" * 18)
    for code, count in ranked.items():
        print(f"{code:<12}{count:>6}")
    print("-" * 18)
    print(f"{'Total':<12}{sum(ranked.values()):>6}")


def save_summary(ranked: dict[str, int], path: str = "summary.json") -> None:
    """Write the summary to a JSON file."""
    with open(path, "w") as f:
        json.dump(ranked, f, indent=2)
    print(f"Saved {path}")


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: uv run python analyzer.py <alert-log-file>")
        return 1

    log_path = sys.argv[1]
    try:
        counts = count_errors(log_path)
    except FileNotFoundError:
        print(f"Error: file not found: {log_path}")
        return 1

    if not counts:
        print("No ORA- errors found.")
        return 0

    ranked = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
    print_summary(ranked)
    save_summary(ranked)
    return 0


if __name__ == "__main__":
    sys.exit(main())
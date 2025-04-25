"""Module for parsing goodreads database jsonl"""

import json


def parse_goodreads_jsonl(filename):
    """Parse the Goodreads data, which is in JSONL format.
    Arguments:
    filename - the path to the JSONL (one JSON per line) file.
    Returns: a list of objects parsed from the JSONL file.
    """
    data = []
    with open(filename, "r", encoding="utf8") as file:
        for line in file:
            # for each line, parse it and add it to the list
            data.append(json.loads(line))
    return data


def main():
    """Main function for informal testing."""
    goodreads_data = parse_goodreads_jsonl("Data/goodreads_subset_k.jsonl")
    print(goodreads_data[0])


if __name__ == "__main__":
    main()

"""Module for parsing bookbans_merged.csv"""

import csv


def parse_bookban_csv(database_file):
    """Creates a list of book bans from a csv file
    Args:
        database_file (str): the path to the database file
    Returns:
        a list where each item is a ban of the form
        {
            "title": str,
            "author": str,
            "secondary_author: str,
            "illustrator": str,
            "translator": str,
            "state": str,
            "district": str,
            "ban_date": str,
            "ban_status": str,
            "origin": str
        }
    """
    bookban_list = []
    with open(database_file, newline="", encoding="utf8") as csv_file:
        reader = csv.reader(csv_file)
        next(reader, None)  # Skips header
        for (
            title,
            author,
            secondary_author,
            illustrator,
            translator,
            state,
            district,
            ban_date,
            ban_status,
            origin,
        ) in reader:
            bookban_list.append(
                {
                    "title": title,
                    "author": lastfirst_to_firstlast(author),
                    "secondary_author": secondary_author,
                    "illustrator": illustrator,
                    "translator": translator,
                    "state": state,
                    "district": district,
                    "ban_date": ban_date,
                    "ban_status": ban_status,
                    "origin": origin,
                }
            )
    return bookban_list


def lastfirst_to_firstlast(name):
    """converts Last, First to First Last format
    Args:
        name (str): Name in the format LastName, FirstName
    Returns:
        Name in the format FirstName LastName
    """
    words = name.split(", ")
    if len(words) > 1:
        return words[1] + " " + words[0]
    return name


def main():
    """Main function for informal testing"""
    book_banlist = parse_bookban_csv("Data/bookbans-merged.csv")
    print(book_banlist[0])


if __name__ == "__main__":
    main()

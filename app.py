'''The flask app. READ THIS:
tested on python 3.13. might fail to start on other versions.'''
from datetime import datetime
from statistics import fmean
from flask import Flask
from ProductionCode.data import bookban_data, goodreads_data

def print_book_full(book,bans):
    """modified slightly from team's productioncode.print_book_short"""
    # title line - title, authors, year (from unix timestamp), isbn
    output = "Details for " + book["title"] + " by "
    output += ", ".join(book["authors"])
    output += f" ({datetime.fromtimestamp(book["year"]/1000).year}, ISBN: {book["isbn"]})"
    # print the entire summary field
    output += "\nBook details from Goodreads: "+book["summary"]
    # print entire genre list
    output += "\nGenres: " + ", ".join(book["genres"])
    # print weighted avg of reviews
    output += f"\nAverage review: {fmean([1,2,3,4,5],weights=book["rating"]):.1f} stars"
    for ban in bans:
        output += f"\nBanned in {ban["district"]}, {ban["state"]} in {ban["ban_date"]}"
    # using a tiny bit of html so the newlines show up
    return output.replace('\n', '<br /><br />')

def fuzzy_match(data, query, partial):
    """modified slightly from team's productioncode.search"""
    if partial:
        return query.lower().strip() in data.lower().strip()
    return query.lower().strip() == data.lower().strip()

app = Flask(__name__)

@app.route("/")
def homepage():
    """homepage containing specific instructions for using the app"""
    return """Go to /details/&lt;isbn&gt; for information on a book.
    Here's a valid ISBN to get you started: 1423134540"""

@app.route("/details/<isbn>", strict_slashes=False)
def details_page(isbn):
    """the page described on the homepage. fetches book details.
    so much of this should be abstracted out later... sorry"""
    matches = [book for book in goodreads_data if book["isbn"] == isbn]
    if len(matches) == 0:
        return "No book with that ISBN found!"
    # at this point there should be exactly one book in matches. test this later
    book = matches[0]
    # totally scuffed fuzzy match patch but should work for now.
    bans = [ban for ban in bookban_data if
        fuzzy_match(ban["title"], book["title"].split(":")[0], True)
    ]
    return print_book_full(book, bans)


@app.errorhandler(404)
def page_not_found(_):
    """handle error 404"""
    return "That page doesn't exist. Try going home."

@app.errorhandler(500)
def python_bug(_):
    """handle error 500"""
    return "We totally messed up. Sorry."

if __name__ == "__main__":
    app.run()

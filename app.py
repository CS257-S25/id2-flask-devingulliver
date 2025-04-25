'''Replace me with your flask app'''
from ProductionCode.data import bookban_data, goodreads_data
from flask import Flask

app = Flask(__name__)

@app.route("/")
def homepage():
    return "Go to /details/<isbn> for information on a book. Here's a valid ISBN to get you started: 0805093079"

@app.route("/details/<isbn>")
def details_page(isbn):
    pass

@app.errorhandler(404)
def page_not_found(e):
    return "That page doesn't exist. Try going home."

@app.errorhandler(500)
def python_bug(e):
    return "We totally messed up. Sorry."

if __name__ == "__main__":
    app.run()
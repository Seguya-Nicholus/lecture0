from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"]=True

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

@app.route("/", methods=['GET'])
def index():
    return "Welcome To My Books App"

@app.route("/books", methods=['GET'])
def return_all_books():
    return jsonify({"BOOKS" : books})

@app.route("/books/<int:book_id>", methods=['GET'])
def return_one_book(book_id):
    return jsonify({"BOOK" : books[book_id]})

@app.route("/books/add", methods=['POST'])
def add_a_book():
    

if __name__ == "__main__":
    app.run()
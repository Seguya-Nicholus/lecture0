from flask import jsonify

class Book():
    def __init__(self, id=None, title=None, author=None, first_sentence=None, year_published=None):
        self.id = id
        self.title = title
        self.author = author
        self.first_sentence = first_sentence
        self.year_published = year_published

    def get_book(self, id, title, author, first_sentence, year_published):
        return jsonify({})



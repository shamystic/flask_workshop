from flask import Flask
from flask import render_template, request, redirect, url_for

import inventory

app = Flask(__name__)

# Index: Home page of the website 
@app.route('/')
def index():
    return render_template('index.html')

# example.com/hello/Shamikh
@app.route('/hello/<string:name>') 
def hello(name):
     # returns hello Shamikh!
    return 'Hello ' + name + '!'

# View all data
@app.route('/all', methods = ['GET'])
def all():
    books_and_authors = inventory.all()
    return render_template('view_table.html', input = books_and_authors)

# List view: Books only
@app.route('/books', methods = ['GET'])
def show_books():
    books = inventory.all_books()
    return render_template('view.html', input = books)
    
# List view: Authors only
@app.route('/authors', methods = ['GET'])
def show_authors():
    authors = inventory.all_authors()
    return render_template('view.html', input = authors)

@app.route('/new-book', methods = ['GET'])
def new_book():
    return render_template('new_book.html')

@app.route('/add_book', methods = ['POST', 'GET'])
def add_book():
   if request.method == 'POST':
        author = request.form['author']
        book = request.form['name']
        inventory.add_book(author, book)    
        #  return render_template("result.html", result = result)
        return redirect(url_for('all'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug = True)

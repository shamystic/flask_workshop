authorToBooks = {}
books = []
authors = []

def add_book(author, book): 
	authors.append(author)
	books.append(book)
	if author not in authorToBooks: 
		authorToBooks[author] = [book]
	else: 
		authorToBooks[author].append(book)
	print ("Added book {} and author {}".format(book, author))
	return

# Handle commands of the form 'list books of an author'
def booksByAuthor(author):
	return authorToBooks[author]

def all(): 
	return authorToBooks
	
def all_books():
	return books

def all_authors():
	return authors

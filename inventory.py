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
	
# shopToPopularity = dict() # map of shop to number of Likes
# shopToSections = dict() # map of shop to set(sections)
# sectionShopToListings = dict() # map of (shop, section) to set(listings)

# # Handle commands of the form 'add shop <shop>'.
# def addShop(shop):
#     if shop not in shopToSections:
#     	shopToSections[shop] = set()
#     if shop not in shopToPopularity:
#         shopToPopularity[shop] = 0

# # Handle commands of the form 'add section <section> by <shop>'.
# def addSection(section, shop):
# 	if shop not in shopToPopularity:
# 		shopToPopularity[shop] = 0
# 	shopToSections[shop].add(section)
# 	if (section, shop) not in sectionShopToListings:
# 		sectionShopToListings[(section, shop)] = set()

# # Handle commands of the form 'add listing <listing> on <section> by <shop>'.
# def addListing(listing, section, shop):
# 	if shop not in shopToPopularity:
# 		shopToPopularity[shop] = 0
# 	shopToSections[shop].add(section)
# 	if (section, shop) in sectionShopToListings:
# 		sectionShopToListings[(section, shop)].add(listing)
# 	else:
# 		sectionShopToListings[(section, shop)] = set()



# # Handle commands of the form 'list listings on <section> by <shop>'.
# def listListingsOnSection(section, shop):
# 	return sectionShopToListings[(section, shop)]

# # Handle commands of the form 'like <listing> in <section> by <shop>'.
# def likeListing(listing, section, shop):
# 	shopToPopularity[shop] += 1

# # Handle commands of the form 'list top <N> shops'.
# def listTopNShops(N):
#     shops = [(shop, shopToPopularity[shop]) for shop in shopToPopularity.keys()]
#     shops.sort(key = lambda x: x[1], reverse = True)
#     shops = [x[0] for x in shops]
#     print(shops)
#     return ' '.join(shops[:int(N)])

# def listShops():
#     return shopToSections.keys()
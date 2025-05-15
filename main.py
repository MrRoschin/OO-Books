# Write Python code for both the Novel and Magazine classes modelled in the previous slide. Include a suitable constructor method which uses the Book constructor method. Instantiate 2 novels and 2 magazines and print their details.
# Create the Book class (plus methods and attributes)
# Create the Novel class that inherits from Book class.
# Create the Magazine class that inherits from Book class.

class Book:
    def __init__(self, title, author, year, pages):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages

    def displayDetails(self, rating, review):
        self.rate = rating
        self.review = review
        return "Book methods"

class Novel(Book):
    def __init__(self, title, author, year, pages, genre, chapters):
        super().__init__(title, author, year, pages)
        self.genre = genre
        self.chapters = chapters
    
    def calcReadTime(self, readspeed):
        self.readspeed = readspeed
        return "Novel methods"
    
class Magazine(Book):
    def __init__(self, title, author, year, pages, issue, articles):
        super().__init__(title, author, year, pages)
        self.issue = issue
        self.articles = articles
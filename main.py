class Book:
    def __init__(self, title, author, year, pages, rating=None, review=None):
        self.title = title
        self.author = author
        self.year = year
        self.pages = pages
        self.rating = rating
        self.review = review

    def displayDetails(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        print(f"Pages: {self.pages}")
        if self.rating:
            print(f"Rating: {self.rating}")
        if self.review:
            print(f"Review: {self.review}")

    def rateBook(self, rating):
        self.rating = rating
        print(f"Rating set to: {rating}/5")

    def reviewBook(self, review):
        self.review = review
        print(f"Review set to: {review}")

class Novel(Book):
    def __init__(self, title, author, year, pages, genre, chapters, rating=None, review=None):
        super().__init__(title, author, year, pages, rating, review)
        self.genre = genre
        self.chapters = chapters
    
    def displayDetails(self):
        super().displayDetails()
        print(f"Genre: {self.genre}")
        print(f"Chapters: {self.chapters}")
    
    def calcReadTime(self, readspeed):
        return f"Estimated read time: {self.pages / readspeed:.2f} hours"

class Magazine(Book):
    def __init__(self, title, author, year, pages, issue, articles, rating=None, review=None):
        super().__init__(title, author, year, pages, rating, review)
        self.issue = issue
        self.articles = articles

    def displayDetails(self):
        super().displayDetails()
        print(f"Issue: {self.issue}")
        print(f"Articles: {', '.join(self.articles)}")

    def getArticleByTitle(self, articletitle):
        if articletitle in self.articles:
            return f"Article found: {articletitle}"
        else:
            return "Article not found"


# Instantiate one novel and one magazine (plus one book)
book1 = Book("IT", "Stephen King", 1986, 1138, "5/5", "Great book")
novel1 = Novel("1984", "George Orwell", 1949, 328, "Dystopian", 24, "4.5/5", "Cool book")
magazine1 = Magazine("National Geographic", "Various", 2023, 100, "April", ["Climate Change", "Wildlife Wonders"], "4/5", "National Geographic is cool")

# Display their details
book1.displayDetails()
print()
novel1.displayDetails()
print()
magazine1.displayDetails()
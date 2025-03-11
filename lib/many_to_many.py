# class Author:
#     pass


# class Book:
#     pass


# class Contract:
#     pass

class Book:
    all_books = []

    def __init__(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        self.title = title
        Book.all_books.append(self)

    def contracts(self):
        """Returns a list of contracts related to this book."""
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        """Returns a list of authors who have contracts for this book."""
        return list({contract.author for contract in self.contracts()})  # Uses a set to remove duplicates

    def __repr__(self):
        return f"Book('{self.title}')"




class Author:
    all_authors = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("Name must be a string")
        self.name = name
        Author.all_authors.append(self)
    
    def contracts(self):
        """Returns a list of contracts associated with this author"""
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return list(set(contract.book for contract in self.contracts()))
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a positive integer")
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
    
    def __repr__(self):
        return f"Author('{self.name}')"


class Contract:
    all = []  # Ensure we use the expected class attribute

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise TypeError("author must be an instance of Author")
        if not isinstance(book, Book):
            raise TypeError("book must be an instance of Book")
        if not isinstance(date, str):
            raise TypeError("date must be a string")
        if not isinstance(royalties, int):
            raise TypeError("royalties must be an integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)  # Append to the expected class attribute

    @classmethod
    def contracts_by_date(cls, date):
        """Returns a list of contracts that match the specified date."""
        return [contract for contract in cls.all if contract.date == date]

    def __repr__(self):
        return f"Contract({self.author.name}, {self.book.title}, {self.date}, {self.royalties})"



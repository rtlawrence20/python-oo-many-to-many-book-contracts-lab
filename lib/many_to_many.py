class Author:
    """Represents an author who can sign multiple book contracts."""

    all = []

    def __init__(self, name: str):
        self.name = name
        Author.all.append(self)

    # Association helpers
    def contracts(self):
        """Return a list of Contract instances for this author."""
        return [c for c in Contract.all if c.author is self]

    def books(self):
        """Return a list of unique Book instances this author has contracts with."""
        books = [c.book for c in self.contracts()]
        # Preserve order while removing duplicates
        seen = set()
        unique = []
        for b in books:
            if id(b) not in seen:
                seen.add(id(b))
                unique.append(b)
        return unique

    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract linking this author with a book."""
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        """Sum of royalties across all this author's contracts."""
        return sum(c.royalties for c in self.contracts())


class Book:
    """Represents a book that may have multiple authors via contracts."""

    all = []

    def __init__(self, title: str):
        self.title = title
        Book.all.append(self)

    # Association helpers
    def contracts(self):
        """Return a list of Contract instances for this book."""
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        """Return a list of unique Author instances for this book."""
        authors = [c.author for c in self.contracts()]
        seen = set()
        unique = []
        for a in authors:
            if id(a) not in seen:
                seen.add(id(a))
                unique.append(a)
        return unique


class Contract:
    """Join model connecting an Author and a Book with date and royalties."""

    all = []

    def __init__(self, author, book, date, royalties):
        # Use property setters for validation
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # author
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    # book
    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    # date
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    # royalties
    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an int")
        self._royalties = value

    # Class method
    @classmethod
    def contracts_by_date(cls, date_str):
        """Return all contracts whose date equals date_str, preserving creation order."""
        return [c for c in cls.all if c.date == date_str]

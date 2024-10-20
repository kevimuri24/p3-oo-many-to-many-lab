class Author:
    
    all = []
    
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self._name = name  # Direct assignment to avoid recursion
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string.")
        self._name = name
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of Book.")
        if not isinstance(date, str):
            raise ValueError("Date must be a string in the format 'MM/DD/YYYY'.")
        if not isinstance(royalties, int):
            raise ValueError("Royalties must be an integer.")
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())
        


class Book:
    
    all = []
    
    def __init__(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        self._title = title  # Direct assignment to avoid recursion
        Book.all.append(self)
        
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string.")
        self._title = title
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]
        


class Contract:
    
    all = []
    
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of Book.")
        if not isinstance(date, str):
            raise ValueError("Date must be a string in the format 'MM/DD/YYYY'.")
        if not isinstance(royalties, int):
            raise ValueError("Royalties must be an integer.")
        
        self._author = author
        self._book = book
        self._date = date
        self._royalties = royalties
        Contract.all.append(self)
        
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        self._author = author
        
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of Book.")
        self._book = book
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if not isinstance(date, str):
            raise ValueError("Date must be a string in the format 'MM/DD/YYYY'.")
        self._date = date
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if not isinstance(royalties, int):
            raise ValueError("Royalties must be an integer.")
        self._royalties = royalties
        
    @classmethod
    def contracts_by_date(cls, date):
        sorted_contracts = sorted(cls.all, key=lambda x: x.date)
        return [contract for contract in sorted_contracts if contract.date == date]
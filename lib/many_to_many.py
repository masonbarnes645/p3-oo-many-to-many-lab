
class Author():
    def __init__(self, name):
        self.name = name
    def contracts(self):
        return [contract for contract in Contract.all if contract.author is self]
    def books(self):
        return [contract.book for contract in Contract.all if contract.author is self]
    def sign_contract( self, author, date, royalties):
        self.author = author
        self.date = date
        self.royalties = royalties
        
        
        Contract.all.append(self)
    
        contract = Contract(self, author, date, royalties)
        return contract
    def total_royalties(self):
        return sum(contract.royalties for contract in Contract.all if contract.author is self)
       
class Book:
    def __init__(self, title) -> None:
        self.title = title
    def contracts(self):
        return [contract for contract in Contract.all if contract.book is self]
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]

class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        type(self).all.append(self)

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,author):
        if isinstance(author, Author):
            self._author = author
        else:
            raise(Exception)

    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, book):
        if isinstance(book, Book):
            self._book = book
        else:
            raise(Exception)
        
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date):
        if type(date) is not str:
            raise(Exception)
        else:
             self._date = date
            
             
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, royalties):
        if type(royalties) is not int:
            raise(Exception)
        else:
             self._royalties = royalties
    
    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in Contract.all if contract.date is date]

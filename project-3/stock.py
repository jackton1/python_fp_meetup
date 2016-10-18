from copy import copy
import json
from operator import attrgetter, itemgetter
from functools import reduce, partial

class Book:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.title
    
    def __repr__(self):
        return str(self)
    
    
def get_books(filename, raw=False):
    try:
        data = json.load(open(filename))
    except FileNotFoundError:
        return []
    else:
        if raw:
            return data['books']
        return [Book(**book) for book in data['books']]
    
BOOKS = get_books('books.json')
RAW_BOOKS = get_books('books.json', raw=True)

# pub_sort = sorted(RAW_BOOKS, key=itemgetter('publish_date'))
#pages_sort = sorted(BOOKS, key=attrgetter('number_of_pages'), reverse=True)
#print(pages_sort[0].number_of_pages, pages_sort[-1].number_of_pages)


#important_list = [5, 2, 3, 1]
## important_list.sort() #Bad idea, sorts list in place
#print(sorted(important_list))
#print(important_list)

#from operator import itemgetter
#fruit_list = [
#    ('apple', 2),
#    ('banana', 5),
#    ('coconut', 1),
#    ('durian', 3),
#    ('elderberries', 4)
#]
#
#sorted_fruit = sorted(fruite_list , key=itemgetter(1)) #This sorts by the second item in each tuple

"""Applies a 20% discount to the book's price"""
def sales_price(book):
  book = copy(book) 
  book.price = round(book.price - book.price*.2, 2)
  return book

#sales_books = list(map(sales_price , BOOKS))
#sales_books2 = [sales_price(book) for book in BOOKS]
#
#print(BOOKS[0].price, sales_books2[0].price)
#a = [1, 2, 3]
#print(list(map(lambda x: x * 2, a)))

"""Check for books with 600 pages or more"""
is_long_book = lambda book: book.number_of_pages >= 600

# long_books = list(filter(is_long_book, BOOKS))
# long_books2 = [book for book in BOOKS if book.number_of_pages >= 600] 
# print(len(long_books), len(BOOKS), len(long_books2))

has_rolland =  lambda book: any(['Roland' in subject for subject in book.subjects])

def titlecase(book):
  book = copy(book)
  book.title =  book.title.title()
  return book

#print(list(map(titlecase, filter(has_rolland, BOOKS))))

is_good_deal = lambda book: book.price <= 5
cheap_books = sorted(
    filter(is_good_deal, map(sales_price, BOOKS)),
    key=attrgetter('price')
)

# print(cheap_books)


def add_book_prices(book1, book2):
  return book1 + book2

# total = reduce(add_book_prices, [b.price for b in BOOKS])

def long_total(a=None, b=None, books=None):
  if a is None and b is None and books is None:
      return None
  if a is None and b is None and books is not None:
      a = books.pop(0)
      b = books.pop(0)
      return long_total(a, b, books)
  if a is not None and books and books is not None and b is None:
      b = books.pop(0)
      return long_total(a, b, books)
  if a is not None and b is not None and books is not None:
      return long_total(a+b, None, books)
  if a is not None and b is not None and not books:
      return long_total(a+b, None, None)
  if a is not None and b is None and not books or books is None:
      return a 
 
# print(long_total(None, None, [b.price for b in BOOKS]))
  
# print(total)

def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n-1)
  
# print(factorial(3))

total = reduce(lambda x, y: x + y, [book.price for book in BOOKS])
long_books =  list(filter(lambda book: book.number_of_pages >= 600, BOOKS))
good_deal = list(filter(is_good_deal, BOOKS))
#print(total, len(long_books), len(good_deal))


### PARTIALS ###
def mark_down(book, discount):
  book = copy(book)
  book.price = round(book.price - book.price * discount, 2)
  return book

#standard = partial(mark_down, discount=.2)
#half = partial(mark_down, discount=.5)
#print(standard(BOOKS[5]).price)
#print(half(BOOKS[5]).price)
#print(BOOKS[5].price)

### CURRYING ###
def curried_f(x, y=None, z=None):
  def f(x, y, z):
    return x**3 + y**2 + z
  
  if y is not None and z is not None:
    return f(x, y, z)
  if y is not None and z is None:
    return lambda z: f(x, y, z)
  return lambda y, z=None: (
    f(x, y, z) if (y is not None and z is not None)
    else (lambda z: f(x, y, z)))

print(curried_f(2,3,4))
f = curried_f(2)
print(f)
g = f(3)
print(g)
h = g(4)
print(h)




import redis
r = redis.Redis(host="localhost", port=6379, decode_responses=True)

def add_borrowed_book(borrower, title):
    r.sadd(f"borrower:{borrower}:books", title)

def remove_borrowed_book(borrower, title):
    r.srem(f"borrower:{borrower}:books", title)

def get_borrowed_books(borrower):
    return list(r.smembers(f"borrower:{borrower}:books"))
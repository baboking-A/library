import sqlite3

def init_db():
    conn = sqlite3.connect("mydb.db")
    cur = conn.cursor()

    # books 테이블 생성
    cur.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL UNIQUE,
        author TEXT NOT NULL
    )
    """)

    # borrowings 테이블 생성
    cur.execute("""
    CREATE TABLE IF NOT EXISTS borrowings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        borrower TEXT NOT NULL,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        borrow_month TEXT NOT NULL
    )
    """)

    # books 초기 데이터 삽입
    cur.executemany(
        "INSERT OR IGNORE INTO books (title, author) VALUES (?, ?)",
        [
            ("삼국지1", "침착맨"),
            ("삼국지2", "침착맨"),
            ("삼국지3", "침착맨"),
        ]
    )

    # borrowings 초기 데이터 삽입
    cur.execute(
        "INSERT OR IGNORE INTO borrowings (borrower, title, author, borrow_month) VALUES (?, ?, ?, ?)",
        ("choi", "삼국지2", "침착맨", "2025-07")
    )

    conn.commit()
    conn.close()

# 실행
if __name__ == "__main__":
    init_db()

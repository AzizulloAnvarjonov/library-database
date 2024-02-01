from base import Database


def book():
    book1 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('The Great Gatsby', 'A novel by F. Scott Fitzgerald', 100, 'English', '1925-04-10');"""

    book2 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('To Kill a Mockingbird', 'A novel by Harper Lee', 120, 'English', '1960-07-11');"""

    book3 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('1984', 'A dystopian novel by George Orwell', 90, 'English', '1949-06-08');"""

    book4 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('One Hundred Years of Solitude', 'A novel by Gabriel García Márquez', 80, 'Spanish', '1967-05-30');"""

    book5 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('The Catcher in the Rye', 'A novel by J.D. Salinger', 110, 'English', '1951-07-16');"""

    book6 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('Pride and Prejudice', 'A novel by Jane Austen', 95, 'English', '1813-01-28');"""

    book7 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('Crime and Punishment', 'A novel by Fyodor Dostoevsky', 85, 'Russian', '1866-11-11');"""

    book8 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('The Hobbit', 'A novel by J.R.R. Tolkien', 70, 'English', '1937-09-21');"""

    book9 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('The Da Vinci Code', 'A novel by Dan Brown', 105, 'English', '2003-03-18');"""

    book10 = """INSERT INTO book (name, description, count, language, written_date)
VALUES ('The Alchemist', 'A novel by Paulo Coelho', 88, 'Portuguese', '1988-01-01');"""

    data = [book1, book2, book3, book4, book5, book6, book7, book8, book9, book10]

    for query in data:
        print(Database.connect(query))


def author():
    author1 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('F. Scott', 'Fitzgerald', '1896-09-24');"""

    author2 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('Harper', 'Lee', '1926-04-28');"""

    author3 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('George', 'Orwell', '1903-06-25');"""

    author4 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('Gabriel', 'García Márquez', '1927-03-06');"""

    author5 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('J.D.', 'Salinger', '1919-01-01');"""

    author6 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('Jane', 'Austen', '1775-12-16');"""

    author7 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('Fyodor', 'Dostoevsky', '1821-11-11');"""

    author8 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('J.R.R.', 'Tolkien', '1892-01-03');"""

    author9 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('Dan', 'Brown', '1964-06-22');"""

    author0 = """INSERT INTO author (first_name, last_name, birth_year)
VALUES ('Paulo', 'Coelho', '1947-08-24');"""

    data = [author1, author2, author3, author4, author5, author6, author7, author8, author9, author0]

    for query in data:
        print(Database.connect(query))


def book_author():
    for i in range (1,11):
        query = f"""INSERT INTO book_author VALUES ({i},{i});"""
        print(Database.connect(query))


if __name__ == "__main__":
    book_author()

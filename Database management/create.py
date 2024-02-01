from base import Database


def create_tables():
    book = """CREATE TABLE book(
    book_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    description TEXT,
    count INT,
    language VARCHAR(10),
    written_date DATE DEFAULT NOW());"""

    author = """CREATE TABLE author(
    author_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    birth_year DATE,
    last_update TIMESTAMP DEFAULT NOW());"""

    book_author = """CREATE TABLE book_author(
    author_id INT REFERENCES author(author_id),
    book_id INT REFERENCES book(book_id));"""

    category = """CREATE TABLE category(
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    last_update TIMESTAMP DEFAULT NOW());"""

    book_category = """CREATE TABLE book_category(
    book_id INT REFERENCES book(book_id),
    category_id INT REFERENCES category(category_id));"""

    address = """CREATE TABLE address(
    address_id SERIAL PRIMARY KEY,
    full_address_name VARCHAR(50));"""

    group = """CREATE TABLE groups(
    group_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    student_number INT,
    last_update TIMESTAMP DEFAULT NOW());"""

    student = """CREATE TABLE student(
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    phone_number VARCHAR(12),
    address_id INT REFERENCES address(address_id),
    group_id INT REFERENCES groups(group_id),
    last_update TIMESTAMP DEFAULT NOW());"""

    staff = """CREATE TABLE staff(
    staff_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    phone_number VARCHAR(12),
    address_id INT REFERENCES address(address_id));"""

    rental = """CREATE TABLE rental(
    rental_id SERIAL PRIMARY KEY,
    student_id INT REFERENCES student(student_id),
    book_id INT REFERENCES book(book_id),
    take_date DATE DEFAULT NOW(),
    return_date DATE NOT NULL,
    staff_id INT REFERENCES staff(staff_id));"""

    payment = """CREATE TABLE payment(
    payment_id SERIAL PRIMARY KEY,
    rental_id INT REFERENCES rental(rental_id),
    amount NUMERIC(10,2),
    student_id INT REFERENCES student(student_id),
    staff_id INT REFERENCES staff(staff_id),
    payment_date TIMESTAMP DEFAULT NOW());"""

    data = [book, author, book_author, category, book_category, address, group, student, staff, rental, payment]

    for query in data:
        print(Database.connect(query))


if __name__ == "__main__":
    create_tables()

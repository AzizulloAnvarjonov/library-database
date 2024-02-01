from datetime import datetime


class Book:
    def __init__(self, name: str, description: str, count: int, language, amount):
        self.name = name
        self.description = description
        self.count = count
        self.language = language
        self.amount = amount
        self.written_date = f"{datetime.now().date()}"

    # @staticmethod
    # def insert_into(data):




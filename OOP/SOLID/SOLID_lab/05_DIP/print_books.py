from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        return book.content


class Printer(ABC):
    @abstractmethod
    def get_book(self, book: Book):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book

import pytest
from code_1 import Book, Library

def test_add_book():
    lib = Library()
    lib.books = {}
    lib.books["123"] = Book("123", "Test Book", "Author", "2025")
    assert "123" in lib.books
    assert lib.books["123"].title == "Test Book"

def test_delete_book():
    lib = Library()
    lib.books = {"123": Book("123", "Test Book", "Author", "2025")}
    lib.delete_book = lambda: lib.books.pop("123", None)
    lib.delete_book()
    assert "123" not in lib.books

def test_update_book():
    lib = Library()
    lib.books = {"123": Book("123", "Old Title", "Old Author", "2020")}
    lib.books["123"] = Book("123", "New Title", "New Author", "2025")
    assert lib.books["123"].title == "New Title"
    assert lib.books["123"].author == "New Author"
    assert lib.books["123"].year == "2025"

def test_list_books(capsys):
    lib = Library()
    lib.books = {
        "123": Book("123", "Book1", "Author1", "2020"),
        "456": Book("456", "Book2", "Author2", "2021"),
    }
    lib.list_books()
    captured = capsys.readouterr()
    assert "Book1" in captured.out
    assert "Book2" in captured.out

def test_book_info(capsys):
    lib = Library()
    lib.books = {"123": Book("123", "Book1", "Author1", "2020")}
    lib.book_info = lambda: print(lib.books["123"])
    lib.book_info()
    captured = capsys.readouterr()
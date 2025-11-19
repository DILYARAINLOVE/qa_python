from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
import pytest
from main import BooksCollector

class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    # Параметризованный тест добавления книги
    @pytest.mark.parametrize('name', ['Гордость и предубеждение и зомби', 'М', 'О' * 40])
    def test_add_new_book_valid_name(self, collector, name):
        collector.add_new_book(name)
        assert name in collector.get_books_genre()

    # Тесты добавления книги (негативные случаи)
    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('name', ['', 'О' * 41])
    def test_add_new_book_invalid_name(self, collector, name):
        collector.add_new_book(name)
        assert name not in collector.get_books_genre()

    # Тест установки жанра
    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Сон в летнюю ночь')
        collector.set_book_genre('Сон в летнюю ночь', 'Комедии')
        assert collector.get_book_genre('Сон в летнюю ночь') == 'Комедии'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Роман')
        assert collector.get_book_genre('Книга') == ''

    # Тест получения книг по жанру
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Книга 1')
        collector.set_book_genre('Книга 1', 'Фантастика')
        books = collector.get_books_with_specific_genre('Фантастика')
        assert 'Книга 1' in books

    # Тест получения книг для детей
    def test_get_books_for_children(self, collector):
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Комедии')
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Детская книга' in children_books
        assert 'Страшная книга' not in children_books

    # Тесты работы с избранным
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_in_genre(self, collector):
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    def test_get_books_genre_returns_copy(self, collector):
        collector.add_new_book('Книга')
        assert collector.get_books_genre() is not collector.books_genre
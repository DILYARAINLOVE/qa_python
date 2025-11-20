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

import pytest
from main import BooksCollector

class TestBooksCollector:

    # Тест добавления новой книги с допустимым именем
    @pytest.mark.parametrize('book_name', ['Гордость и предубеждение и зомби', 'М', 'О' * 40])
    def test_add_new_book_valid_name_adds_book(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    # Тест невозможности добавления дубликата книги
    def test_add_new_book_duplicate_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_new_book('Книга')
        assert len(collector.get_books_genre()) == 1

    # Тест невозможности добавления книги с недопустимым именем
    @pytest.mark.parametrize('invalid_name', ['', 'О' * 41])
    def test_add_new_book_invalid_name_not_added(self, invalid_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    # Тест установки допустимого жанра для книги
    def test_set_book_genre_valid_genre_sets_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Сон в летнюю ночь')
        collector.set_book_genre('Сон в летнюю ночь', 'Комедии')
        assert collector.get_book_genre('Сон в летнюю ночь') == 'Комедии'

    # Тест невозможности установки недопустимого жанра
    def test_set_book_genre_invalid_genre_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Роман')
        assert collector.get_book_genre('Книга') == ''

    # Тест получения книг по определенному жанру (с разными жанрами)
    def test_get_books_with_specific_genre_returns_correct_books(self):
        collector = BooksCollector()
        # Добавляем книги с разными жанрами
        collector.add_new_book('Фантастическая книга')
        collector.set_book_genre('Фантастическая книга', 'Фантастика')
        
        collector.add_new_book('Ужасная книга')
        collector.set_book_genre('Ужасная книга', 'Ужасы')
        
        collector.add_new_book('Еще фантастика')
        collector.set_book_genre('Еще фантастика', 'Фантастика')
        
        fantasy_books = collector.get_books_with_specific_genre('Фантастика')
        
        assert 'Фантастическая книга' in fantasy_books
        assert 'Еще фантастика' in fantasy_books
        assert 'Ужасная книга' not in fantasy_books
        assert len(fantasy_books) == 2

    # Тест получения книг для детей
    def test_get_books_for_children_returns_appropriate_books(self):
        collector = BooksCollector()
        collector.add_new_book('Детская книга')
        collector.set_book_genre('Детская книга', 'Комедии')
        collector.add_new_book('Страшная книга')
        collector.set_book_genre('Страшная книга', 'Ужасы')
        
        children_books = collector.get_books_for_children()
        
        assert 'Детская книга' in children_books
        assert 'Страшная книга' not in children_books

    # Тест добавления книги в избранное
    def test_add_book_in_favorites_adds_to_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        assert 'Книга' in collector.get_list_of_favorites_books()

    # Тест невозможности добавления несуществующей книги в избранное
    def test_add_book_in_favorites_not_in_genre_not_added(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Неизвестная книга')
        assert 'Неизвестная книга' not in collector.get_list_of_favorites_books()

    # Тест удаления книги из избранного
    def test_delete_book_from_favorites_removes_book(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.add_book_in_favorites('Книга')
        collector.delete_book_from_favorites('Книга')
        assert 'Книга' not in collector.get_list_of_favorites_books()

    # Тест получения словаря books_genre
    def test_get_books_genre_returns_books_genre_dict(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        
        books_genre = collector.get_books_genre()
        
        assert isinstance(books_genre, dict)
        assert 'Книга 1' in books_genre
        assert 'Книга 2' in books_genre
        assert books_genre['Книга 1'] == ''
        assert books_genre['Книга 2'] == ''

    # Тест получения жанра книги
    def test_get_book_genre_returns_correct_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Фантастика')
        
        genre = collector.get_book_genre('Книга')
        
        assert genre == 'Фантастика'

    # Тест получения списка избранных книг
    def test_get_list_of_favorites_books_returns_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book('Книга 1')
        collector.add_new_book('Книга 2')
        collector.add_book_in_favorites('Книга 1')
        
        favorites = collector.get_list_of_favorites_books()
        
        assert isinstance(favorites, list)
        assert 'Книга 1' in favorites
        assert 'Книга 2' not in favorites
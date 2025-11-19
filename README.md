# qa_python
# Тесты для BooksCollector

## Реализованные тесты:

1. **test_add_new_book_valid_name** - проверка добавления книги с допустимым именем
2. **test_add_new_book_duplicate** - проверка невозможности добавления дубликата
3. **test_add_new_book_invalid_name** - проверка обработки недопустимых имен
4. **test_set_book_genre_valid** - проверка установки допустимого жанра
5. **test_set_book_genre_invalid_genre** - проверка отклонения недопустимого жанра
6. **test_get_books_with_specific_genre** - проверка фильтрации по жанру
7. **test_get_books_for_children** - проверка фильтрации детских книг
8. **test_add_book_in_favorites** - проверка добавления в избранное
9. **test_add_book_in_favorites_not_in_genre** - проверка защиты избранного
10. **test_delete_book_from_favorites** - проверка удаления из избранного
11. **test_get_books_genre_returns_copy** - проверка возвращения копии словаря

Использована параметризация для тестов с разными допустимыми/недопустимыми именами.
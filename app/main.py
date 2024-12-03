import os
from app.model import *

path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '../books.json')


def run_tests():
    path_to_json = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '../test_books.json')
    # Тест 1: Добавление книги
    print("Вывод информации до тестов\n")
    print(Book.get_all(path_to_json))
    book = Book("Test Title", "Test Author", 2021)
    book.add(path_to_json)
    print("проверка после добавления книги\n")
    print(Book.get_all(path_to_json))
    # Тест 2: Удаление книги
    Book.delete("../test_books.json", 1)
    print("проверка после удаления книги\n")
    print(Book.get_all(path_to_json))
    # Тест 3: Поиск книги по названию
    print(Book.find_obj_title(path_to_json, "Test Title"))
    print(Book.find_obj_author(path_to_json, "Test Author"))
    print(Book.find_obj_year(path_to_json, 2021))
    # Тест 4: Изменение статуса книги
    Book.edit_status(path_to_json, 1, "Не в наличии")
    print(Book.get_all(path_to_json))



if __name__ == "__main__":
    while True:
        print("Напишите номер функции, которую хотите использовать:\n"
              "1. Добавление книги.\n"
              "2. Удаление книги.\n"
              "3. Поиск книги по названию (title).\n"
              "4. Поиск книги по автору (author).\n"
              "5. Поиск книги по году издания (year).\n"
              "6. Отображение всех книг.\n"
              "7. Изменение статуса книги (“в наличии” или “выдана”).\n"
              "8. Проведение тестов.\n"
              "0. Выход.")

        try:
            value = int(input("Введите номер функции: "))

            if value == 0:
                print("Выход из программы.")
                break

            if 1 <= value <= 8:
                if value == 1:
                    title = input("Введите название книги: ")
                    author = input("Введите автора: ")
                    year = input("Введите год издания книги: ")
                    book = Book(title, author, year)
                    book.add(path_to_json)
                    print(f"Книга '{title}' успешно добавлена.")

                elif value == 2:
                    id = int(input("Введите номер книги, которую хотите удалить: "))
                    Book.delete(path_to_json, id)
                    print(f"Книга с ID {id} успешно удалена.")

                elif value == 3:
                    title = input("Введите название книги: ")
                    results = Book.find_obj_title(path_to_json, title)
                    if results:
                        for book in results:
                            print(
                                f"Найдена книга: ID {book['id']}, Название: '{book['title']}', Автор: {book['author']}, Год: {book['year']}.")
                    else:
                        print("Книги с таким названием не найдены.")

                elif value == 4:
                    author = input("Введите автора: ")
                    results = Book.find_obj_author(path_to_json, author)
                    if results:
                        for book in results:
                            print(
                                f"Найдена книга: ID {book['id']}, Название: '{book['title']}', Автор: {book['author']}, Год: {book['year']}.")
                    else:
                        print("Книги от этого автора не найдены.")

                elif value == 5:
                    year = int(input("Введите год: "))
                    results = Book.find_obj_year(path_to_json, year)
                    if results:
                        for book in results:
                            print(
                                f"Найдена книга: ID {book['id']}, Название: '{book['title']}', Автор: {book['author']}, Год: {book['year']}.")
                    else:
                        print("Книги за этот год не найдены.")

                elif value == 6:
                    all_books = Book.get_all(path_to_json)
                    if all_books and isinstance(all_books, list):
                        print("\nСписок всех книг:")
                        for i in all_books:
                            print(
                                f"ID {i['id']} - Название: '{i['title']}', Автор: {i['author']}, Год: {i['year']}, Статус: {i['status']}.")
                    else:
                        print("Нет доступных книг для отображения.")

                elif value == 7:
                    id = int(input("Введите номер книги, статус которой хотите изменить: "))
                    status = input("Введите новый статус (выдана или в наличии): ")
                    Book.edit_status(path_to_json, id, status)
                    print(f"Статус книги с ID {id} успешно изменен на '{status}'.")

                elif value == 8:
                    run_tests()
                    print("Все тесты прошли успешно!")

            else:
                print("Выберите значение от 1 до 8 включительно.")

        except ValueError:
            print("Ошибка ввода! Пожалуйста, введите числовое значение.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")


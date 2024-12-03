from app.utils import dict_list_to_json, json_to_dict_list


class Book:
    # Уникальный идентификатор, генерируется автоматически
    _id_counter = 1  # Статический счетчик для генерации уникальных идентификаторов

    def __init__(self, title, author, year):
        self.id = Book._id_counter  # Присваиваем уникальный идентификатор
        Book._id_counter += 1  # Увеличиваем счетчик для следующей книги
        self.title = title
        self.author = author
        self.year = year
        self.status = "В наличии"

    def get(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status
        }

    def add(self, filename):
        try:
            # Получаем список книг из файла
            books = json_to_dict_list(filename)
            if books is None:
                books = []
            # Добавляем текущую книгу в список
            books.append(self.get())
            # Сохраняем обновленный список обратно в файл
            dict_list_to_json(books, filename)
        except Exception as e:
            print(f"Ошибка при добавлении книги: {e}")

    @classmethod
    def delete(cls, filename, idd: int):
        try:
            # Получаем список книг из файла
            books = json_to_dict_list(filename)
            if books is None:
                books = []
            # Удаляем книгу по ID
            for i in books:
                if i["id"] == idd:
                    books.remove(i)
                    return dict_list_to_json(books, filename)
            print(f"Книга с ID {idd} не найдена.")

            # Сохраняем обновленный список обратно в файл
        except Exception as e:
            print(f"Ошибка при удалении книги: {e}")

    @classmethod
    def find_obj_title(cls, path, title):
        try:
            books = json_to_dict_list(path)
            return_list = []
            for book in books:
                if book["title"] == title:
                    return_list.append(book)
            return return_list
        except Exception as e:
            print(f"Ошибка при поиске книг по названию: {e}")
            return []

    @classmethod
    def find_obj_year(cls, path, year):
        try:
            books = json_to_dict_list(path)
            return_list = []
            for book in books:
                if book["year"] == year:
                    return_list.append(book)
            return return_list
        except Exception as e:
            print(f"Ошибка при поиске книг по году: {e}")
            return []

    @classmethod
    def find_obj_author(cls, path, author):
        try:
            books = json_to_dict_list(path)
            return_list = []
            for book in books:
                if book["author"] == author:
                    return_list.append(book)
            return return_list
        except Exception as e:
            print(f"Ошибка при поиске книг по автору: {e}")
            return []

    @classmethod
    def get_all(cls, path):
        try:
            books = json_to_dict_list(path)
            if books is not None:
                return books
            else:
                return "Файл пустой"
        except Exception as e:
            print(f"Ошибка при получении всех книг: {e}")
            return []

    @classmethod
    def edit_status(cls, path, idd, status):
        try:
            books = json_to_dict_list(path)
            if books is None:
                books = []

            for i in range(len(books)):
                if books[i]["id"] == idd:
                    books[i]["status"] = status
                    break
            else:
                print(f"Книга с ID {idd} не найдена.")
                return dict_list_to_json(books, path)
        except Exception as e:
            print(f"Ошибка при изменении статуса книги: {e}")






import json
from Model.BookModel import Book
from Model.UserModel import User
from Model.Library import Library
from View.View import LibraryView

filePath_user = "Listeners.txt"
filePath_books = "Books.txt"

class LibraryController:
    def __init__(self):
        self.library = Library()
        self.library.books =  self.library.load_file(filePath_books, Book)
        self.library.users =  self.library.load_file(filePath_user, User)

    def run(self):
        while True:
            LibraryView.show_menu()
            choice = input("Выберите пункт меню: ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_books()
            elif choice == "3":
                self.filter_books_by_genre()
            elif choice == "4":
                self.issue_book()
            elif choice == "5":
                self.return_book()
            elif choice == "6":
                self.show_users()
            elif choice == "7":
                self.save_and_exit()
                print(" Данные сохранены. Выход...")
                break
            else:
                print(" Неверный выбор. Попробуйте снова.")



    def add_book(self):
        title = LibraryView.input_data("Название книги: ")
        author = LibraryView.input_data("Автор: ")
        year = LibraryView.input_data("Год издания: ")
        genre = LibraryView.input_data("Жанр: ")

        if self.library.books:
            max_id = max(book.book_id for book in self.library.books)
            new_id = max_id + 1
        else:
            new_id = 1

        new_book = Book(new_id, title, author, year, genre)
        self.library.books.append(new_book)
        self.library.save_file(self.library.books, filePath_books)
        print("Книга добавлена.")

    def view_books(self):
        LibraryView.show_books(self.library.books)

    def filter_books_by_genre(self):
        genre = LibraryView.input_data("Введите жанр для фильтрации: ")
        filtered = [b for b in self.library.books if b.genre.lower() == genre.lower()]
        LibraryView.show_books(filtered)

    def issue_book(self):
        user_name = LibraryView.input_data("Имя пользователя: ")
        card_number = LibraryView.input_data("Номер читательского билета: ")
        title = LibraryView.input_data("Название книги: ")

        user = next((u for u in self.library.users if u.library_card_number == card_number), None)
        if not user:
            user = User(user_name, card_number)
            self.library.users.append(user)
            self.library.save_file(self.library.users, filePath_user)

        if len(user.issued_books) >= 3:
            print("У пользователя уже 3 книги.")
            return

        book = next((b for b in self.library.books if b.title == title and b.available), None)

        if book:
            if book.book_id in user.issued_books:
                print(" Книга с таким названием уже выдана пользователю.")
            else:
                book.available = False
                user.issued_books.append(book.book_id)
                self.library.save_file(self.library.users, filePath_user)
                self.library.save_file(self.library.books, filePath_books)
                print("Книга выдана.")
        else:
            print("Книга недоступна или не найдена.")



    def return_book(self):
        card_number = LibraryView.input_data("Номер читательского билета: ")
        title = LibraryView.input_data("Название книги: ")

        user = next((u for u in self.library.users if u.card_number == card_number), None)
        book = next((b for b in self.library.books if b.title == title and b.available), None)

        if user and book.book_id in user.issued_books:
            user.book.remove( book.book_id)
            if book:
                book.available = True
            print("Книга возвращена.")
        else:
            print("Книга не найдена у пользователя.")

    def show_users(self):
        LibraryView.show_users(self.library.users, self.library.books)

    def save_and_exit(self):
        self.library.save_file(self.library.users, filePath_user)
        self.library.save_file(self.library.books, filePath_books)
        print("Данные сохранены. До свидания!")





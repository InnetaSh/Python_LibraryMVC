



class LibraryView:
    @staticmethod
    def show_menu():
        print()
        print("*" * 70)
        print("Данные библиотеки".center(70))
        print("*" * 70)
        print("1.Добавлять новую книгу в библиотеку.")
        print("2.Просматривать все книги")
        print("3.Фильтровать книги по жанру")
        print("4.Выдавать книгу пользователю")
        print("5.Возвращать книгу в библиотеку.")
        print("6.Записать пользователя в библиотеку.")
        print("7.Просматривать список пользователей и выданные им книги")
        print("8.Save.Exit")
        print("-" * 70)

    @staticmethod
    def input_data(prompt):
        return input(prompt)

    @staticmethod
    def show_books(books):
        if not books:
            print("Нет доступных книг.")
        else:
            print("\n Список книг:")
            for i, book in enumerate(books, start=1):
                print(f"\n{i}. {book}")

    @staticmethod
    def show_users(users, books):
        if not users:
             print("No books found")
        else:
             print("Список пользователей:".center(70))
             print("-" * 70)
             for i, user in enumerate(users, start=1):
                 print(f"{i}. {user}")
                 if user.issued_books:
                     print("   выданные книги:")
                     for book_id in user.issued_books:
                         book = next((b for b in books if b.book_id == book_id), None)
                         if book:
                             print(f"    - {book.title} ({book.author}, {book.year_of_publication})")
                         else:
                             print(f"    - [ID {book_id}] — книга не найдена")
                 else:
                     print("    Нет выданных книг.")


    @staticmethod
    def show_message(message):
        print(message)

class Book:
    def __init__(self, book_id, title, author,year_of_publication, genre, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.genre = genre
        self.available = available

    def __str__(self):
        return (
            f"ID: {self.book_id}\nНазвание: {self.title}\nАвтор: {self.author}\n"
            f"Год издания: {self.year_of_publication}\nЖанр: {self.genre}\nДоступность: {self.available}"
        )



    def to_dict(self):
        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "year_of_publication": self.year_of_publication,
            "genre": self.genre,
            "available": self.available
        }

    @classmethod
    def from_dict(cls, data):
        book = cls(
            data["book_id"],
            data["title"],
            data["author"],
            data["year_of_publication"],
            data["genre"]
        )
        book.available = data.get("available", True)
        return book
class User:
    def __init__(self, name,library_card_number):
        self.name = name
        self.library_card_number = library_card_number
        self.issued_books = []

    def __str__(self):
        return f"{self.name} : library card number- {self.library_card_number}"





    def to_dict(self):
        return {
            "name": self.name,
            "library_card_number": self.library_card_number,
            "issued_books":self.issued_books
        }

    @classmethod
    def from_dict(cls, data):
        user = cls( data["name"], data["library_card_number"])
        user.issued_books = data.get("issued_books", [])
        return user
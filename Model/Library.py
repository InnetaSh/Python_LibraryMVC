import json



class Library:
    def __init__(self):
        self.books = []
        self.users = []

    @staticmethod
    def load_file(path, cls):
        try:
            with open(path, "r", encoding="utf-8") as myfile:
                data = myfile.read()
                if data:
                    data_list = json.loads(data)
                    return [cls.from_dict(d) for d in data_list]
                else:
                    return []
        except FileNotFoundError:
            return []
        except Exception as ex:
            print(f"Ошибка при загрузке: {ex}")
            return []


    @staticmethod
    def save_file(obj_list, path):
        try:
            with open(path, "w", encoding="utf-8") as myfile:
                data = [obj.to_dict() for obj in obj_list]
                json.dump(data, myfile, ensure_ascii=False, indent=4)
        except Exception as ex:
            print(f"Ошибка при сохранении: {ex}")
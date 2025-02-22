# class ItemBlock:
#     def __init__(self, name, sub_items=None):
#         self.name = name
#         self.sub_items = sub_items
#
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "sub_items": self.sub_items,
#         }
#
#     def __repr__(self):
#         return f"ItemBlock(name={self.name}, sub_items={self.sub_items})"
#
# class Block:
#     def __init__(self, name, comment, items, title):
#         self.name = name  # Название блока
#         self.comment = comment  # Комментарий блока
#         self.items = items  # Список названий
#         self.title = title  # Может быть пустым
#
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "comment": self.comment,
#             "items": self.items,
#             "title": self.title
#         }
#
#     def __repr__(self):
#         return f"Block(name={self.name}, comment={self.comment}, items={self.items})"
#
#
# class Diagnosis:
#     def __init__(self, name):
#         self.name = name  # Название диагноза
#         self.blocks = []  # Список блоков в диагнозе
#
#     def add_block(self, block):
#         self.blocks.append(block)  # Добавляем блок в диагноз
#
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "blocks": [block.to_dict() for block in self.blocks]
#         }
#
#     def __repr__(self):
#         return f"Diagnosis(name={self.name}, blocks={self.blocks})"
#
#
# class Section:
#     def __init__(self, name):
#         self.name = name  # Название секции
#         self.diagnoses = []  # Список диагнозов в секции
#
#     def add_diagnosis(self, diagnosis):
#         self.diagnoses.append(diagnosis)  # Добавляем диагноз в секцию
#
#     def to_dict(self):
#         return {
#             "name": self.name,
#             "diagnoses": [diagnosis.to_dict() for diagnosis in self.diagnoses]
#         }
#
#     def __repr__(self):
#         return f"Section(name={self.name}, diagnoses={self.diagnoses})"

class Item:
    def __init__(self, name, values=None):
        self.name = name  # Название item
        self.values = values if values else []  # Массив строк

    def to_dict(self):
        return {
            "name": self.name,
            "values": self.values
        }

    def __repr__(self):
        return f"Item(name={self.name}, values={self.values})"


class Title:
    def __init__(self, name, values=None):
        self.name = name  # Название title
        self.values = values if values else []  # Массив строк

    def to_dict(self):
        return {
            "name": self.name,
            "values": self.values
        }

    def __repr__(self):
        return f"Title(name={self.name}, values={self.values})"


class Block:
    def __init__(self, name, comment, items=None, titles=None):
        self.name = name  # Название блока
        self.comment = comment  # Комментарий блока

        # items и titles не могут быть одновременно заполнены
        # if items and titles:
        #     raise ValueError("Block cannot have both items and titles at the same time.")

        self.items = items if items else []  # Список объектов Item
        self.titles = titles if titles else []  # Список объектов Title

    def to_dict(self):
        return {
            "name": self.name,
            "comment": self.comment,
            "items": [item.to_dict() for item in self.items] if self.items else None,
            "titles": [title.to_dict() for title in self.titles] if self.titles else None
        }

    def __repr__(self):
        return f"Block(name={self.name}, comment={self.comment}, items={self.items}, titles={self.titles})"


class Diagnosis:
    def __init__(self, name, code):
        self.name = name  # Название диагноза
        self.code = code
        self.blocks = []  # Список блоков в диагнозе

    def add_block(self, block):
        self.blocks.append(block)  # Добавляем блок в диагноз

    def to_dict(self):
        return {
            "name": self.name,
            "code": self.code,
            "blocks": [block.to_dict() for block in self.blocks]
        }

    def __repr__(self):
        return f"Diagnosis(name={self.name}, code={self.code}, blocks={self.blocks})"


class Section:
    def __init__(self, name):
        self.name = name  # Название секции
        self.diagnoses = []  # Список диагнозов в секции

    def add_diagnosis(self, diagnosis):
        self.diagnoses.append(diagnosis)  # Добавляем диагноз в секцию

    def to_dict(self):
        return {
            "name": self.name,
            "diagnoses": [diagnosis.to_dict() for diagnosis in self.diagnoses]
        }

    def __repr__(self):
        return f"Section(name={self.name}, diagnoses={self.diagnoses})"

import uuid


class Avto:
    def __init__(self, model, year, color, km = 0):
        self.__id = uuid.uuid4()
        self.model = model
        self.year = year
        self.color = color
        self.__km = km

    def get_km(self):
        return self.__km

    def get_id(self):
        return self.__id
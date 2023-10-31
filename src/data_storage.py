from abc import ABC, abstractmethod


class SaveABC(ABC):

    @abstractmethod
    def delete_from_list(self):
        pass

    @abstractmethod
    def save_in_list(self):
        pass


class DelAndSave(SaveABC):
    def __init__(self, way_json):
        self.way_json = way_json

    def delete_from_list(self):
        ...

    def save_in_list(self):
        with open(self.way_json, 'w', encoding='utf8') as file:
            ...


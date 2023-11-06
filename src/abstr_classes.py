from abc import abstractmethod, ABC

"""Абстрактный класс для класса data_storage"""


class SaveABC(ABC):

    @abstractmethod
    def delete_from_list_all(self):
        pass

    @abstractmethod
    def delete_from_list_item(self, delete_fail, platform):
        ...

    @abstractmethod
    def save_in_list(self, save_fail, platform):
        pass


"""Абстрактный класс для класса getting_data"""


class VacancyAPI(ABC):

    @abstractmethod
    def return_dikt(self):
        pass

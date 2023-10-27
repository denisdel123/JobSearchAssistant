import os
from abc import ABC, abstractmethod
import requests


class VacancyAPI(ABC):

    @abstractmethod
    def get_vacancies(self, params):
        pass


class PlatformHH(VacancyAPI):
    def __init__(self, api_key):
        self.api_key = api_key

    def get_vacancies(self, params):
        vacancies = requests.get(self.api_key, params=params)
        print(vacancies)
        return vacancies


class PlatformSuperJob(VacancyAPI):
    pass

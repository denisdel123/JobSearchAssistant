from abc import ABC, abstractmethod
import requests


class VacancyAPI(ABC):

    @abstractmethod
    def return_dikt(self):
        pass


class WorkWithPlatformshh(VacancyAPI):
    def __init__(self, name, salary_from, salary_to, link, about_vacancy, currency, salary_bool, create_at, city):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.link = link
        self.about_vacancy = about_vacancy
        self.currency = currency
        self.salary_bool = salary_bool
        self.create_at = create_at
        self.city = city

    @classmethod
    def get_vacancies_hh(cls, params, api_key, city):
        text = {"text": params, 'area': city}
        response = requests.get(api_key, params=text)

        obj_class = []

        list_for_dict = {"salaryFrom": '',
                         "salaryTo": '',
                         "currency": '',
                         "salaryBool": True,
                         "snippet": '',
                         "alternate_url": '',
                         "name": '',
                         'created_at': '',
                         'city': ''
                         }

        if response.status_code == 200:
            result = response.json()

            print(result['items'])

            for j_fail in result['items']:

                salary = j_fail["salary"]

                try:
                    list_for_dict["currency"] = salary["currency"]
                except TypeError:
                    list_for_dict["currency"] = 'не указано'

                if salary:

                    if salary["from"] or salary["to"]:

                        try:
                            list_for_dict["salaryFrom"] = salary['from']
                        except KeyError:
                            list_for_dict["salaryFrom"] = 'не указано'

                        try:
                            list_for_dict["salaryTo"] = salary["to"]
                        except KeyError:
                            list_for_dict["salaryTo"] = 'не указано'

                    else:
                        list_for_dict["salaryBool"] = False

                    list_for_dict["snippet"] = j_fail["snippet"]['requirement']
                    list_for_dict["alternate_url"] = j_fail["alternate_url"]
                    list_for_dict["name"] = j_fail["name"]
                    list_for_dict['created_at'] = j_fail['created_at']
                    list_for_dict['city'] = j_fail['area']['name']
                    print(list_for_dict)

                obj_class.append(cls(list_for_dict["name"], list_for_dict["salaryFrom"], list_for_dict["salaryTo"],
                                     list_for_dict["alternate_url"],
                                     list_for_dict["snippet"],
                                     list_for_dict["currency"],
                                     list_for_dict["salaryBool"],
                                     list_for_dict['created_at'],
                                     list_for_dict['city']))

        else:
            print(f"ошибка {response.status_code}")

        return obj_class

    def return_dikt(self):
        list_dict = {"salaryFrom": self.salary_from,
                     "salaryTo": self.salary_to,
                     "currency": self.currency,
                     "salaryBool": self.salary_bool,
                     "snippet": self.about_vacancy,
                     "alternate_url": self.link,
                     "name": self.name,
                     'created_at': self.create_at,
                     'city': self.city
                     }
        return list_dict

    def __le__(self, other):
        return self.salary_to > other.salary_to

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def __str__(self):
        return f"{self.return_dikt()}"


class WorkWithPlatformsSuperJob(WorkWithPlatformshh):
    def __init__(self, name, salary_from, salary_to, link, about_vacancy, currency, salary_bool):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.link = link
        self.about_vacancy = about_vacancy
        self.currency = currency
        self.salary_bool = salary_bool

    @classmethod
    def get_vacancies_super(cls, params, api_key_url, headers):
        params = {"keyword": params}
        header = {"X-Api-App-Id": headers}
        response = requests.get(api_key_url, params=params, headers=header)

        obj_class = []

        list_for_dict = {"salaryFrom": "",
                         "salaryTo": "",
                         "currency": '',
                         "salaryBool": True,
                         "snippet": '',
                         "alternate_url": '',
                         "name": ''}

        if response.status_code == 200:
            result = response.json()

            for j_fail in result['objects']:

                if j_fail["payment_from"] or j_fail["payment_to"]:
                    try:
                        list_for_dict["salaryFrom"] = j_fail['payment_from']
                    except KeyError:
                        list_for_dict["salaryFrom"] = 'не указано'

                    try:
                        list_for_dict["salaryTo"] = j_fail["payment_to"]
                    except KeyError:
                        list_for_dict["salaryTo"] = 'не указано'
                else:
                    list_for_dict["salaryBool"] = False

                list_for_dict["currency"] = j_fail['currency']
                list_for_dict["snippet"] = j_fail["candidat"]
                list_for_dict["alternate_url"] = j_fail["link"]
                list_for_dict["name"] = j_fail["profession"]

                obj_class.append(cls(list_for_dict["name"], list_for_dict["salaryFrom"], list_for_dict["salaryTo"],
                                     list_for_dict["alternate_url"], list_for_dict["snippet"],
                                     list_for_dict["currency"],
                                     list_for_dict["salaryBool"]))

        else:
            print(f"ошибка {response.status_code}")

        return obj_class

    def return_dikt(self):
        list_dict = {"salaryFrom": self.salary_from,
                     "salaryTo": self.salary_to,
                     "currency": self.currency,
                     "salaryBool": self.salary_bool,
                     "snippet": self.about_vacancy,
                     "alternate_url": self.link,
                     "name": self.name}

        return list_dict

    def __le__(self, other):
        return self.salary_to > other.salary_to

    def __repr__(self):
        return f"{self.__class__.__name__}"

    def __str__(self):
        return f"{self.return_dikt()}"

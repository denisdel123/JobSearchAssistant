import json
from abstr_classes import SaveABC

"""Класс для работы с json file"""


class WorkWithJson(SaveABC):
    def __init__(self, way_json):
        self.way_json = way_json

    """Очистка json file по запросу пользователя"""

    def delete_from_list_all(self):

        my_dict = {"hh": [],
                   "superJob": []}

        with open(self.way_json, 'w', encoding='utf8') as file:
            json.dump(my_dict, file, indent=4)

    """Удаление вакансии по id"""

    def delete_from_list_item(self, file_id, platform):

        plat = 'hh'

        if platform == plat:
            plat = 'superJob'
        else:
            plat = 'hh'

        new_list = {'hh': [],
                    'superJob': []
                    }

        with open(self.way_json, 'r', encoding='utf8') as file:

            result = json.load(file)

            platform_list = result[platform]

            i = 1
            for item in platform_list:
                if item['id'] != file_id:
                    item['id'] = i
                    new_list[platform].append(item)
                    i += 1
                else:
                    continue
            new_list[plat] = result[plat]

            with open(self.way_json, 'w', encoding='utf8') as file:

                json.dump(new_list, file, indent=4)

    """Сохранение вакансии каждая вакансия сохраняется отдельно"""

    def save_in_list(self, save_file, platform):
        list_save = {
            "id": '',
            "salaryFrom": save_file["salaryFrom"],
            "salaryTo": save_file["salaryTo"],
            "currency": save_file["currency"],
            "salaryBool": save_file["salaryBool"],
            "snippet": save_file["snippet"],
            "alternate_url": save_file["alternate_url"],
            "name": save_file["name"],
            'created_at': save_file['created_at'],
            'city': save_file['city']
        }
        with open(self.way_json, 'r', encoding='utf8') as file:
            read_json = json.load(file)

            read_json[platform].append(list_save)
            i = 1
            for item in read_json[platform]:
                item['id'] = i
                i += 1
        with open(self.way_json, 'w', encoding='utf8') as fail:
            json.dump(read_json, fail, indent=4)



import json
from datetime import datetime

from src import getting_data, data_storage

"""Вывод вакансии на консоль и сохранение по запросу пользователя"""


def interaction_with_hh(word, city, api_hh, way_json):
    obj_hh = getting_data.WorkWithPlatformshh.get_vacancies_hh(word, api_hh, city)

    for item in obj_hh:

        res = item.return_dikt()

        name_vacancy = res['name']
        city = res['city']
        create_date = res['created_at']
        link = res['alternate_url']
        snippet = res['snippet']
        salary_from = res['salaryFrom']
        salary_to = res['salaryTo']
        currency = res['currency']
        if salary_from is not None and salary_to is not None:
            salary = f"От: {salary_from} {currency} До: {salary_to} {currency}"
        elif salary_from is not None:
            salary = f"От {salary_from} {currency} До: Не указанно"
        elif salary_to is not None:
            salary = f"От: Не указано До: {salary_to} {currency}"
        else:
            salary = f"От: Не указано До: Не указанно"

        print(f"Наименование вакансии: {name_vacancy}\nГород: {city}\nЗарплата: {salary}\n\
Дата создания: {create_date}\nКраткое описание вакансии: {snippet}\nСсылка: {link}\n")

        print('сохранить вакансии? yes/no')
        answer_save = input(': ')
        if answer_save == 'yes':
            hh_save = data_storage.WorkWithJson(way_json)
            hh_save.save_in_list(res, 'hh')
        else:
            continue


"""Вывод вакансии на консоль и сохранение по запросу пользователя"""


def interaction_with_super(word, city, way_json, url_superJob, header):
    obj_super_job = getting_data.WorkWithPlatformsSuperJob.get_vacancies_super(word, url_superJob, header)

    for item in obj_super_job:

        res = item.return_dikt()

        name_vacancy = res['name']
        city = res['city']
        create_date = res['created_at']
        link = res['alternate_url']
        snippet = res['snippet']
        salary_from = res['salaryFrom']
        salary_to = res['salaryTo']
        currency = res['currency']
        salary = ''
        if salary_from is not None and salary_to is not None:
            salary = f"От: {salary_from} {currency} До: {salary_to} {currency}"
        elif salary_from is not None:
            salary = f"От {salary_from} {currency} До: Не указанно"
        elif salary_to is not None:
            salary = f"От: Не указано До: {salary_to} {currency}"
        else:
            salary = f"От: Не указано До: Не указанно"

        print(f"Наименование вакансии: {name_vacancy}\nГород: {city}\nЗарплата: {salary}\n\
Дата создания: {create_date}\nКраткое описание вакансии: {snippet}\nСсылка: {link}\n")

        print('сохранить вакансию? yes/no')
        answer_save = input(': ')
        if answer_save == 'yes':
            super_save = data_storage.WorkWithJson(way_json)
            super_save.save_in_list(res, 'superJob')
        else:
            continue


"""Сортировка вакансий по дате создания"""


def sort_vacancy_date(way_json):
    obj_look = data_storage.WorkWithJson(way_json)

    with open(way_json, 'r', encoding='utf8') as file:
        vacancies = json.load(file)

    sort = ['hh', 'superJob']
    data = []
    my_dict = {"hh": [],
               "superJob": []}

    with open(way_json, 'w', encoding='utf8') as file:
        json.dump(my_dict, file, indent=4)
    for plat in sort:

        try:
            for item in vacancies[plat]:
                data.append(item['created_at'])

            sorted_data = sorted(data, key=lambda x: datetime.strptime(x, '%Y-%m-%d %H:%M:%S'))

        except Exception:
            print('no element')
            continue

        try:

            for item1 in sorted_data:
                for i in vacancies[plat]:

                    if item1 == i['created_at']:

                        obj_look.save_in_list(i, plat)

                    else:
                        continue


        except Exception:
            print('no element')
            continue


"""Сортировка вакансии по зарплате"""


def sort_vacancy_salary(way_json):
    with open(way_json, 'r', encoding='utf8') as file:
        vacancies = json.load(file)

    list_options = ['hh', 'superJob']
    obj_save = data_storage.WorkWithJson(way_json)

    my_dict = {"hh": [],
               "superJob": []}

    with open(way_json, 'w', encoding='utf8') as file:
        json.dump(my_dict, file, indent=4)

    for plat in list_options:
        sorted_vacancies = sorted(vacancies[plat],
                                  key=lambda x: (x['salaryTo'] if x['salaryTo'] is not None else float('-inf')),
                                  reverse=True)
        print(plat)
        print(sorted_vacancies)

        my_dict[plat] = sorted_vacancies

        for item in my_dict[plat]:
            obj_save.save_in_list(item, plat)


"""Вывод вакансии на консоль"""


def look_list_vacancy(way_json):
    with open(way_json, 'r', encoding='utf8') as file:
        result = json.load(file)

        plat = ['hh', 'superJob']

        for platform in plat:

            if result[platform] is not None:
                for item_hh in result[platform]:

                    vacancy_id = item_hh['id']
                    name_vacancy = item_hh['name']
                    city = item_hh['city']
                    create_date = item_hh['created_at']
                    link = item_hh['alternate_url']
                    snippet = item_hh['snippet']
                    salary_from = item_hh['salaryFrom']
                    salary_to = item_hh['salaryTo']
                    currency = item_hh['currency']

                    if salary_from is not None and salary_to is not None:
                        salary = f"От: {salary_from} {currency} До: {salary_to} {currency}"
                    elif salary_from is not None:
                        salary = f"От {salary_from} {currency} До: Не указанно"
                    elif salary_to is not None:
                        salary = f"От: Не указано До: {salary_to} {currency}"
                    else:
                        salary = f"От: Не указано До: Не указанно"

                    info = f"Платформа {platform}\nid вакансии: {vacancy_id}\nНаименование вакансии: \
{name_vacancy}\nГород: {city}\nЗарплата: {salary}\n\
Дата создания: {create_date}\nКраткое описание вакансии: {snippet}\nСсылка: {link}\n"

                    print(info)
                else:
                    print('список пуст')


"""Удалить вакансии по id"""


def delete_id(way_json, id, platform):
    obj_delete = data_storage.WorkWithJson(way_json)
    obj_delete.delete_from_list_item(id, platform)


"""Удалить все вакансии"""


def delete_all(way_json):
    obj_delete = data_storage.WorkWithJson(way_json)
    obj_delete.delete_from_list_all()


"""Очистка json file перед работой приложения"""


def clin_json(way_json):
    my_dict = {'hh': [],
               'superJob': []}

    with open(way_json, 'w', encoding='utf8') as file:
        json.dump(my_dict, file, indent=4)

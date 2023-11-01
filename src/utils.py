import json

from src import getting_data, data_storage


def interaction_with_user(api_hh, way_json, url_superJob, header):
    print(f"Привет! Я помогу найти работу.")
    print("На каком сайте будем искать работу?\n1 hh.ru\n2 superJob\n3 оба сайта\nвведите число.")
    number = int(input())
    print('в каком городе искать?')
    print('напишите ключевое слово для поиска:')
    word = input()

    # obj_superJob = getting_data.WorkWithPlatformsSuperJob.get_vacancies_super(word, url_superJob, header)

    if number == 1:

        obj_hh = getting_data.WorkWithPlatformshh.get_vacancies_hh(word, api_hh, "111")

        for item in obj_hh:
            res = item.return_dikt()

            obj_save = data_storage.DelAndSave(way_json)
            obj_save.save_in_list(res, 'hh')

        print("показать все вакансии? yes/no")
        answer = input()

        if answer == 'yes':
            with open(way_json, 'r', encoding='utf8') as file:
                result = json.load(file)

                for item in result['hh']:
                    print(f"Наименование вакансии: {item['name']}\nзарплата {item['salaryFrom']} - "
                          f"{item['salaryTo']}\n\nо вакансии {item['snippet']}")

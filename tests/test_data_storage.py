import json
from pathlib import Path

import pytest
from src.data_storage import WorkWithJson

way_json_test = Path(__file__).parent.parent.joinpath("data").joinpath("test_vacancies.json")


@pytest.fixture()
def class_del_and_save():
    return WorkWithJson(way_json_test)


def test_save(class_del_and_save):
    file = {"salaryFrom": '23000',
            "salaryTo": '55000',
            "currency": 'RUB',
            "salaryBool": True,
            "snippet": 'about',
            "alternate_url": 'https',
            "name": 'developer',
            'created_at': '2023-10-23 21:21:21',
            'city': 'Moscow'}

    class_del_and_save.save_in_list(file, 'superJob')
    class_del_and_save.save_in_list(file, 'hh')

    with open(way_json_test, 'r', encoding='utf8') as file:
        res = json.load(file)
        test = res['superJob'][0]

        assert test['salaryFrom'] == '23000'

        test2 = res['hh'][0]

        assert test2['salaryFrom'] == '23000'


def test_delete(class_del_and_save):
    class_del_and_save.delete_from_list_all()
    with open(way_json_test, 'r', encoding='utf8') as file:
        res = json.load(file)
        assert res['hh'] == []
        assert res['superJob'] == []


def test_delete_from_list_item(class_del_and_save):
    list_save = {
        "salaryFrom": '20000',
        "salaryTo": '25000',
        "currency": 'rub',
        "salaryBool": 't',
        "snippet": 'about',
        "alternate_url": 'http',
        "name": 'name',
        'created_at': '2023',
        'city': 'mosc'
    }

    l = ['hh', 'superJob']

    for z in l:
        for g in range(0, 2):
            class_del_and_save.save_in_list(list_save, z)

    with open(way_json_test, 'r', encoding='utf8') as f:
        result = json.load(f)
        test1 = len(result['hh'])

        class_del_and_save.delete_from_list_item(1, 'hh')

    with open(way_json_test, 'r', encoding='utf8') as f:
        result = json.load(f)
        test2 = len(result['hh'])

        assert test2 < test1

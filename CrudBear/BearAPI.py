import requests
from Config.NewBears import *
from CrudBear.CreateJson import *
from conftest import *

class BearApi:

    def create_bear(self, bear_type, bear_name, bear_age):
        """

        :param bear_type: вид медведя
        :param bear_name: имя медведя
        :param bear_age: возраст медведя
        :return:
        Создание нового медведя
        """
        bear_json = CreateJson.bear_json(bear_type, bear_name, bear_age)
        response = requests.post(url + '/bear', json=bear_json)
        if response.status_code == 200:
            assert response.text != "EMPTY"
            return int(response.text)
        else:
            return response.status_code



    def create_bear_and_assert(self, bear_type, bear_name, bear_age):
        """
        :param bear_type: вид медведя
        :param bear_name: имя медведя
        :param bear_age: возраст медведя
        :return:
        Создание медведя и проверка, что он создался правильно
        """
        bear_id = self.create_bear(bear_type, bear_name, bear_age)
        etalon_bear = CreateJson.bear_etalon_json(bear_id, bear_type, bear_name, bear_age)
        bear_json = self.get_bear_by_id(bear_id).json()
        assert etalon_bear == bear_json

    def create_bear_and_assert_negative(self, bear_type, bear_name, bear_age):
        """
        :param bear_type: вид медведя
        :param bear_name: имя медведя
        :param bear_age: возраст медведя
        :return:
        Создание медведя с неправильнымии параметрами
        """
        response = self.create_bear(bear_type, bear_name, bear_age)
        assert response == 500



    def get_all_bears_and_assert(self, allBears):
        """
        :param allBears: Лист из всех медведей для сравнения со списком медведей на сервере
        :return:
        Провереям, что сервер отдает всех медведей созданных на сервере
        """
        response = requests.get(url + '/bear')
        assert 200 == response.status_code
        allBearsFromServer = response.json()
        assert allBears == allBearsFromServer

    def get_bear_by_id(self, id):
        """
        Получаем медведя по его id
        :param id: id медведя
        :return:
        """
        response = requests.get(url + '/bear/%s' % id)
        assert 200 == response.status_code
        assert response.text != "EMPTY"
        return response

    def update_bear_by_id(self, id, bear_type, bear_name, bear_age):
        """

        :param id: id медведя
        :param bear_type: вид медведя
        :param bear_name: имя медведя
        :param bear_age: возраст медведя
        :return:
        Апдейт медведя по его id
        """
        bear_json = {
            "bear_type": bear_type,
            "bear_name": bear_name,
            "bear_age": bear_age

        }
        response = requests.put(url + '/bear/%s' % id, json=bear_json)
        assert "OK" == response.text

    def delete_all_bears(self):
        """
        удаление всех медведей
        :return:
        """
        response = requests.delete(url + '/bear')
        assert 200 == response.status_code


    def delete_bear_by_id(self, id):
        """

        :param id: id медведя
        :return:
        удаление всех медведей
        """
        response = requests.delete(url + '/bear/%s' % id)
        assert 200 == response.status_code
        response = requests.get(url + '/bear/%s' % id)
        assert response.text == "EMPTY"

    def check_bear_by_attributes(self, bear_id, bear_type, bear_name, bear_age):
        """
        Сравнение медведя по его параметрам
        :param bear_id: id медведя
        :param bear_type: вид медведя
        :param bear_name: имя медведя
        :param bear_age: возраст медведя
        :return:
        """
        etalon_bear = CreateJson.bear_etalon_json(bear_id, bear_type, bear_name, bear_age)
        bear_json = self.get_bear_by_id(bear_id).json()
        assert etalon_bear == bear_json


    def create_bear_by_list(self, bear):
        """

        :param bear:передаем dict содержащий параметры медведя
        :return:
        создаем медведя из готового словаря
        """
        response = requests.post(url + '/bear', json=bear)
        assert 200 == response.status_code
        return int(response.text)

    def create_list_of_4_bears(self):
        """
        создаем список медведей из приготовленых словарей
        :return:
        """
        bear1 = {"bear_id": self.create_bear_by_list(NewBears.bear_Jimmy)}
        bear1.update(NewBears.bear_Jimmy)
        bear2 = {"bear_id": self.create_bear_by_list(NewBears.bear_Kate)}
        bear2.update(NewBears.bear_Kate)
        bear3 = {"bear_id": self.create_bear_by_list(NewBears.bear_Terry)}
        bear3.update(NewBears.bear_Terry)
        bear4 = {"bear_id": self.create_bear_by_list(NewBears.bear_Tommy)}
        bear4.update(NewBears.bear_Tommy)
        allBears = [bear1,
                   bear2,
                   bear3,
                   bear4]
        return allBears










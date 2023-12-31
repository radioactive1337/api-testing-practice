import requests
import allure
from jsonschema import validate
from tools.logger import log
from tools.data_loader import jsonschema_loader
from enums.global_enums import ErrorEnums
from tools.json_handler import JsonHandler


class Api:

    def __init__(self):
        self.response = None

    def __str__(self):
        return f"{self.response.status_code}"

    def get(self, url: str, endpoint: str, params: dict = None):
        with allure.step(f"POST request на url: {url}{endpoint}\n"):
            self.response = requests.get(url=f"{url}{endpoint}",
                                         params=params)
        log(response=self.response)
        return self

    def post(self, url: str, endpoint: str, params: dict = None,
             json_body: dict = None):
        with allure.step(f"POST request на url: {url}{endpoint}\n"
                         f"request body: {json_body}"):
            self.response = requests.post(url=f"{url}{endpoint}",
                                          params=params,
                                          json=json_body)
        log(response=self.response, request_body=json_body)
        return self

    def put(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f"PUT request на url: {url}{endpoint}\n"
                         f"request body: {json_body}"):
            self.response = requests.put(url=f"{url}{endpoint}",
                                         params=params,
                                         json=json_body)
        log(response=self.response, request_body=json_body)
        return self

    def patch(self, url: str, endpoint: str, params: dict = None, json_body: dict = None):
        with allure.step(f"PATCH request на url: {url}{endpoint}\n"
                         f"request body: {json_body}"):
            self.response = requests.patch(url=f"{url}{endpoint}",
                                           params=params,
                                           json=json_body)
        log(response=self.response, request_body=json_body)
        return self

    def delete(self, url: str, endpoint: str):
        with allure.step(f"DELETE request на url: {url}{endpoint}\n"):
            self.response = requests.delete(url=f"{url}{endpoint}")
        log(response=self.response)
        return self

    @allure.step("status code is equal to {expected_code}")
    def status_code_should_be(self, expected_code: list | int):
        actual_code = self.response.status_code
        if isinstance(expected_code, list):
            assert actual_code in expected_code, (f"{ErrorEnums.WRONG_STATUS_CODE.value}\n"
                                                  f"{self}")
        else:
            assert actual_code == expected_code, (f"{ErrorEnums.WRONG_STATUS_CODE.value}\n"
                                                  f"{self}")
        return self

    @allure.step("jsonschema is valid")
    def jsonschema_validation(self, path_file: str, name_jsonschema: str = 'schema'):
        json_schema = jsonschema_loader(path_file, name_jsonschema)
        validate(self.response.json(), json_schema)
        return self

    def get_payload(self, key: str):
        response = self.response.json()
        payload = JsonHandler().get_value_by_key(key, response)
        return payload

    @allure.step("Items with key: {key} and value: {value} exist")
    def check_value_in_response(self, key: str, value: str):
        payload = self.get_payload(key)
        assert (value == payload), f"{ErrorEnums.ITEM_DOES_NOT_EXIST.value}"
        return self

    @allure.step("Response validation using pydantic")
    def pydantic_validation(self, pydantic_model):
        response = self.response.json()
        pydantic_model.model_validate(response)
        return self

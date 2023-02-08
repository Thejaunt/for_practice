from __future__ import annotations
import requests
from data_model import Model
import logging
from siteconf import APPID

logging.basicConfig(filename='logfile.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.WARNING)


class FetchData:

    def __init__(self, city: str = '', units: str = 'Metric', limit: int = 1):
        __URL = 'https://api.openweathermap.org/data/2.5/weather?'
        __APPID = APPID
        self.city = city
        self.units = units
        self.limit = limit
        self.url_req = f'{__URL}units={self.units}&limit={self.limit}&q={self.city}&appid={__APPID}'
        self.response = None

    def __repr__(self):
        return f'object {self.city}'

    @property
    def request_json_data(self):  # collects data from openweather.com by city name
        if self.response is None:  # caching the response data into the constructor if successful
            try:
                res = requests.get(self.url_req)
                if res.status_code == 200:
                    self.response = res
                else:
                    res.raise_for_status()
            except requests.exceptions.HTTPError as eh:
                print("[HTTP ERROR] Wrong name of the city or API returned invalid data", eh)
                logging.warning(eh)
            except requests.exceptions.RequestsWarning as er:
                print("[RequestWarning] somthing is wrong", er)
                logging.warning(er)
            except requests.exceptions.RequestException as e:
                print("[RequestException] Something Else", e)
                logging.warning(e)
        return self.response

    @property
    def dict_data(self) -> dict or None:  # simply converts JSON data into a dictionary
        try:
            res = self.request_json_data.json()
            return res
        except AttributeError:
            return None

    def create_model(self) -> object:  # returns a single city obj with weather data as its attributes
        city_model = object
        if self.dict_data is not None:
            print(f'Creating object for {self.city}')
            try:
                city_model = Model(city_name=self.city, data=self.dict_data)
            except TypeError:
                print('Wrong city name or API returned wrong data order in JSON')
        return city_model

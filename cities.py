import json
from service import FetchData


class FetchCityNames:

    def __init__(self, cities_amount: int = 50):
        self.cities_amount = cities_amount

    def create_list_of_cities(self) -> list[str]:
        # creates and return a list with cities from JSON file in local directory
        with open('data.json', 'r') as f:
            list_of_cities = json.load(f)
        res = []
        for _ in range(self.cities_amount):
            """some Chinese cities in the JSON file have their province' name added after the city' name
             which causes a bad response from API.
              In future would be better to make the request by coordinates
              
              I haven't corrected the unsuitable chinese cities(Xi-an) to see how the logger works in this case
              """
            if (' ' in list_of_cities[_]["city"]) and (list_of_cities[_]["country"] == "China"):
                wrong_chinese_city = (list_of_cities[_]["city"]).split(' ')
                res.append(wrong_chinese_city[0])
                continue
            res.append(list_of_cities[_]["city"])
        return res

    def get_list_of_cities_obj(self) -> list[object]:
        # Creates and returns a list of objects(cities) with Weather data attrs
        list_obj_cities = []
        failed_to_get = 0
        for city in self.create_list_of_cities():
            try:
                city_obj = FetchData(f'{city}')
                if city_obj.dict_data:
                    list_obj_cities.append(city_obj.create_model())
                else:
                    failed_to_get += 1
            except Exception as r:
                print(r)
        return list_obj_cities

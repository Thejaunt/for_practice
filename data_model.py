
class Model:

    def __init__(self, city_name: str = '', data: dict = None):
        self.data = data
        self.city_name: str = city_name
        self.temp: float = self.data['main']['temp']
        self.max_temp: float = data['main']['temp_max']
        self.min_temp: float = data['main']['temp_min']
        self.pressure: float = data['main']['pressure']
        self.humidity: float = data['main']['humidity']

    def __repr__(self):
        return f'Model object {self.city_name}'

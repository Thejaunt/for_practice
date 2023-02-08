from cities import FetchCityNames
from dbmanager import PostgesDb
import logging
import time

logging.basicConfig(filename='logfile.log', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.WARNING)


def main():
    while True:
        try:
            city_names = FetchCityNames()
            city_objs = city_names.get_list_of_cities_obj()
            update = PostgesDb(city_objs)
            update.update_data()
        except Exception as err:
            logging.warning(err)
        time.sleep(86400)  # 86400 - amount of seconds in a day


if __name__ == '__main__':
    main()

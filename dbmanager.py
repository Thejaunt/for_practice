import psycopg2
from pgconfig import host, user, password, db_name


class PostgesDb:
    def __init__(self, city_objs):
        self.city_objs = city_objs

    def update_data(self):
        conn = None
        cur = None
        try:
            conn = psycopg2.connect(
                host=host,
                user=user,
                password=password,
                dbname=db_name
            )
            cur = conn.cursor()

            create_script = f''' CREATE TABLE IF NOT EXISTS weather_data (
                                id  BIGSERIAL PRIMARY KEY NOT NULL,
                                city   VARCHAR(50),
                                temperature REAL,
                                min_temperature REAL,
                                max_temperature REAL,
                                humidity REAL,
                                pressure REAL,
                                created_at TIMESTAMPTZ DEFAULT Now()
                                )'''
            cur.execute(create_script)

            for city in self.city_objs:
                update_script = f'''INSERT INTO weather_data
                                (city, temperature, min_temperature, max_temperature, humidity, pressure)
                                VALUES('{city.city_name}', {city.temp}, {city.min_temp},
                                {city.max_temp}, {city.humidity}, {city.pressure})'''
                cur.execute(update_script)
            conn.commit()
        except Exception as ex:
            print(ex)
        finally:
            if cur is not None:
                cur.close()
                print("[INFO] PostgreSQL connection closed")
            if conn is not None:
                conn.close()
                print('Cursor closed')

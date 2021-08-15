from sqlite3.dbapi2 import connect
from urllib import request
import json
from prettytable import PrettyTable
import sqlite3

URL = "http://api.openweathermap.org/data/2.5/weather?q={city name}&lang={lang}&appid={API key}"

CITY = ["Seoul", "Daegu", "Busan"]
LANG = "kr"
API_KEY = # 로그인 후 개인 key 입력

# 연걸
connection_sqlite3 =sqlite3.connect("weather.db")
#커서
cursor_sqlite3 = connection_sqlite3.cursor()
#쿼리
city_weather_table_create = "CREATE TABLE IF NOT EXISTS city_weather (id integer, main text, description text, icon text)"
#실행
cursor_sqlite3.execute(city_weather_table_create)



dataTable = PrettyTable()

for city in CITY:
    with request.urlopen(URL.replace("{city name}", city).replace("{lang}", LANG).replace("{API key}", API_KEY)) as response:
        result_json = response.read()
    parsed_json = json.loads(result_json)
    print(parsed_json["weather"])


    dataTable.field_names = parsed_json["weather"][0].keys()

    for i in parsed_json["weather"]:
        dataTable.add_row(i.values())
        list_values = list(i.values())
        cursor_sqlite3.execute(
        "INSERT INTO city_weather VALUES ('" +
            str(list_values[0]) + "', '" +
            list_values[1] + "', '" +
            list_values[2] + "', '" +
            list_values[3] + "')"
    )

connection_sqlite3.commit()  
print(dataTable)
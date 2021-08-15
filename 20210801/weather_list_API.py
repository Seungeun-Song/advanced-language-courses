from urllib import request
import json
from prettytable import PrettyTable

URL = "http://api.openweathermap.org/data/2.5/weather?q={city name}&lang={lang}&appid={API key}"

CITY = ["Seoul", "Daegu", "Busan"]
LANG = "kr"
API_KEY = 

dataTable = PrettyTable()

for city in CITY:
    with request.urlopen(URL.replace("{city name}", city).replace("{lang}", LANG).replace("{API key}", API_KEY)) as response:
        result_json = response.read()
    parsed_json = json.loads(result_json)
    print(parsed_json["weather"])


    dataTable.field_names = parsed_json["weather"][0].keys()

    for i in parsed_json["weather"]:
        dataTable.add_row(i.values())
print(dataTable)
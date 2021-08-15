from urllib import request
import json
from prettytable import PrettyTable



URL = "http://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"

CITY = "seoul"
API_KEY = 

with request.urlopen(URL.replace("{city name}", CITY).replace("{API key}", API_KEY)) as response:
    # print(response.read())
    # print(type(response.read()))
    result_json = response.read()

parsed_json = json.loads(result_json)

# print("type: ", type(parsed_json))
# print(parsed_json)

# print(parsed_json["weather"])
# print(len(parsed_json["weather"]))

dataTable = PrettyTable()

dataTable.field_names = parsed_json["weather"][0].keys()  #db의 columns naming과 같은

for i in parsed_json["weather"]:
    # print(list(i.values()))
    list_values = list(i.values())
    print(list_values[0], list_values[1], list_values[2], list_values[3])
    dataTable.add_row(parsed_json["weather"][0].values())

print(dataTable)
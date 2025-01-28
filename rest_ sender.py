import requests
from json import loads, dumps
json_primer = '''
{ "name": "Иван",
  "age": 37,
  "mother": {
    "name": "Ольга",
    "age": 58
  },
  "children": [
    "Маша",
    "Игорь",
    "Таня",
    {"проба": "bbbv", "age": 58}
  ],
  "married": true,
  "dog": null
}'''
json_primer = json_primer.encode('utf-8')


re = requests.post("http://127.0.0.1:5000/stub", data=json_primer)
print(re.text)

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
    {"проба": "bbbv", "age": 58},
    {"проба": "bbbv", "age": 58}
  ],
  "married": true,
  "dog": null
}'''
json_primer = json_primer.encode('utf-8')

re = requests.post("http://5.35.10.200:5000/stub", json_primer)
print(re.text)

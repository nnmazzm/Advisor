# რჩევების მიღება id ნომრის მიხედვით
import requests
import json

id_num = input("შეიყვანეთ ID ნომერი: ")

url = f'https://api.adviceslip.com/advice/{id_num}'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    advice = data["slip"]["advice"]
    print("რჩევა:", advice)
else:
    print("შეცდომა: ვერ მოიძებნა რჩევა ამ ID-ით.")

with open('data.json', 'r') as file:
    c = file.read()
    print(c)


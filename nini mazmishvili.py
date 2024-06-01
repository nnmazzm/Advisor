import requests
import json
import sqlite3

id_num = input("შეიყვანეთ ID ნომერი: ")

url = f'https://api.adviceslip.com/advice/{id_num}'
response = requests.get(url)
content = response.json()

if response.status_code == 200:
    advice = content.get("slip", {}).get("advice")
    if advice:
        print("რჩევა:", advice)
    else:
        print("შეცდომა: ვერ მოიძებნა რჩევა ამ ID-ით.")
else:
    print("შეცდომა: ვერ მოიძებნა რჩევა ამ ID-ით.")

with open('data.json', 'w') as file:
    json.dump(content, file, indent=4)

conn = sqlite3.connect('Advices.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS advices (
            id VARCHAR(50),
            advice VARCHAR(255)
            )''')

c.execute("INSERT INTO advices (id, advice) VALUES (?, ?)", (id_num, advice if advice else ""))
conn.commit()
conn.close()

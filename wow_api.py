import requests

# отримуємо дані
url = "http://api.open-notify.org/astros.json"
response = requests.get(url)
data = response.json()

# аналіз
iss_people = [person["name"] for person in data["people"] if person["craft"] == "ISS"]

# результат
print(f"Кількість людей на МКС: {len(iss_people)}")
print("Люди, які зараз на МКС:")
for name in iss_people:
    print(name)

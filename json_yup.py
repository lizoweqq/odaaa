import requests

# отримати
url = "https://dummyjson.com/users"
response = requests.get(url)
data = response.json()["users"]

# аналіз
under_30 = sum(1 for user in data if user["age"] < 30)
green_eyed_women = sum(1 for user in data if user["gender"] == "female" and user["eyeColor"] == "green")
in_san_francisco = sum(1 for user in data if user["address"]["city"] == "San Francisco")

# результат
print(f"кількість користувачів молодше 30 років: {under_30}")
print(f"кількість жінок із зеленими очима: {green_eyed_women}")
print(f"кількість людей, які живуть у San Francisco: {in_san_francisco}")

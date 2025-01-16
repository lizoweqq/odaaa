import requests
import json

# URL API
api_url = "http://api.open-notify.org/astros.json"

# запит API
response = requests.get(api_url)
data = response.json()

# збереження в JSON файл
with open("astros.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

# результат
    print(f"дані з API збережено в файл: {json_file_path}")

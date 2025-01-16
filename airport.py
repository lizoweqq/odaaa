import csv

# сам файл
filename = "D:/Downloads/airport-codes_csv.csv"

# аналіз данних
with open(filename, newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter=';')  #крапка з комою
    ua_airports = [row['name'] for row in reader if row['iso_country'] == 'UA']

# результат
print("Ааеропорти України:")
for airport in ua_airports:
    print(airport)

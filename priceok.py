from pywebio.input import input, NUMBER
from pywebio.output import put_text

# звичанйа ціна квитка
BASE_PRICE = 146

def zoo_ticket_price():
    # запит віку
    age = input("будь ласка, введіть ваш вік:", type=NUMBER)

    # Обчислення ціни
    if age < 6:  # до 6 ьезкоштовно
        price = "безкоштовно"
    elif 6 <= age < 13:  # від 6 до 12 знижка 50%
        price = f"{int(BASE_PRICE * 0.5)} грн (знижка 50%)"
    elif 13 <= age < 18:  # від 13 до 17 знижка 25%
        price = f"{int(BASE_PRICE * 0.75)} грн (знижка 25%)"
    elif 18 <= age < 60:  # від 18 до 60 повна ціна
        price = f"{BASE_PRICE} грн (повна ціна)"
    else:  # більше 60 знижка 30%
        price = f"{int(BASE_PRICE * 0.7)} грн (знижка 30%)"

    put_text(f"Вартість квитка: {price}")

# результат
if __name__ == "__main__":
    zoo_ticket_price()

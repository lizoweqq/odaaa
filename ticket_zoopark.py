from pywebio.input import input, NUMBER
from pywebio.output import put_text

# запит віку
def zoo_ticket_price():
    age = input("будь ласка, введіть ваш вік:", type=NUMBER)

# обчислення ціни
    if age < 6: # до 6 ьезкоштовно
        price = "безкоштовно"
    elif 6 <= age <= 12: # від 6 до 12 знижка 50 % (вартість квитка = 50 грн)
        price = "50 грн (знижка 50%)"
    elif 13 <= age <= 17: # від 13 до 17 знижка 25 % (вартість квитка = 75 грн)
        price = "75 грн (знижка 25%)"
    elif 18 <= age < 60: # від 18 до 60 повна ціна 100
        price = "100 грн (повна ціна)"
    else:  # більше 60 знижка 30% (вартість квитка = 70 грн)
        price = "70 грн (знижка 30%)"

    put_text(f"Вартість квитка: {price}")

# результат
if __name__ == "__main__":
    zoo_ticket_price()

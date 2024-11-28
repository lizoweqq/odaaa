# вітати
print("Вітаємо у ресторані 'Дача'!")

# запитати
name = input("Як до вас звертатися? ")

# меню і ціни
borscht_price = 50
varenyky_price = 70
salad_price = 40
cutlet_price = 60
fish_price = 80

# кільксть
borscht = int(input("Скільки порцій борщу? "))
varenyky = int(input("Скільки порцій вареників? "))
salad = int(input("Скільки порцій салату? "))
cutlet = int(input("Скільки порцій котлет? "))
fish = int(input("Скільки порцій риби? "))

# усього
total_price = (
    borscht * borscht_price +
    varenyky * varenyky_price +
    salad * salad_price +
    cutlet * cutlet_price +
    fish * fish_price
)

# Знижка
discount = total_price * 0.15
final_price = total_price - discount

# описс
borscht_desc = "А чи не бажаєте смачних пампушок? Дуже рекомендуємо взяти 2."
varenyky_desc = "Неможливо пройти повз вареників!"
salad_desc = "Освіжаючий салат."
cutlet_desc = "Котлета прямо з пательні!"
fish_desc = "Чи не хочете спробувати нашу фірмову рибу?"

# опис страв
print("\nОпис страв:")
print("Борщ: " + borscht_desc)
print("Вареники: " + varenyky_desc)
print("Салат: " + salad_desc)
print("Котлета: " + cutlet_desc)
print("Риба: " + fish_desc)

# чек
print("\nЧек:")
print(f"До сплати: {final_price:.2f} грн")
print(f"Дякуємо за замовлення, {name}!")

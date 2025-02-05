class Car:
    def __init__(self, year, brand, model, fuel_consumption, price):
        self.year = year
        self.brand = brand
        self.model = model
        self.mileage = 0  # за замовчуванням 0
        self.fuel_consumption = fuel_consumption
        self.price = price

    def drive(self):
        print(f"Я авто марки {self.model}, їду по справам господаря")

    @property
    def category(self):
        return "Крутяк" if self.price > 15000 else "Тачелла"

# створюємо авто
car1 = Car(2020, "BMW", "X5", 8.5, 20000)
car2 = Car(2018, "Toyota", "Corolla", 6.5, 12000)

# Змінюємо пробіг
car1.mileage = 50000

# перевірка категоріїї
print(car2.category)  # виведе "Тачелла"

# результат
# метод drive
car1.drive()  # виведе "Я авто марки X5, їду по справам господаря"

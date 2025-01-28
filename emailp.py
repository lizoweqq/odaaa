from jinja2 import emailp
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# данні
car_data = {
    "brand": "Tesla",
    "model": "Model 3",
    "year": 2023,
    "price": 35000,
    "seats": 5,
    "options": [
        "Шкіряний салон",
        "Система підігріву сидінь",
        "Apple CarPlay/Android Auto",
        "360-градусна камера огляду",
        "Парктроніки (передні та задні)"
    ]
}

# завантаженняHTML шаблон
with open("template.html", "r", encoding="utf-8") as file:
    template = emailp(file.read())

# генерація
email_content = template.render(**car_data)

# параметри
sender_email = "ваша_пошта@gmail.com"
receiver_email = "отримувач@gmail.com"
password = "ваш_пароль"

# формуваення
msg = MIMEMultipart("alternative")
msg["Subject"] = f"Реклама автомобіля: {car_data['brand']} {car_data['model']}"
msg["From"] = sender_email
msg["To"] = receiver_email

# додавання
msg.attach(MIMEText(email_content, "html"))

# відправка
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Лист успішно надіслано!")
except Exception as e:
    print(f"Помилка при відправці: {e}")

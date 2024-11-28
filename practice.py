bread = input('enter quantity of bread loafs>> ')
bread_quantity = int(bread)
bread_price = 24.35
total_bread = bread_quantity * bread_price

butter = input('enter quantity of butter, g>> ').strip()

butter_price = 320.16
butter_quantity = float(butter)
total_butter = butter_quantity * butter_price

total = total_butter * total_bread
print(total)
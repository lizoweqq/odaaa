"""
симулятор каси магазину
код, наведений нижче, приймає від покупця наступну інформацію про закупівлю 2-х товарів
- назва
- кількість (ціле число)
- ціна за одиницю
на підставі отриманих даних формується чек
всі ціни та вартість мають бути виведені в форматі з копійками, кількість - цілі числа
програма розрахована на використання на території України
"""
import textwrap
from datetime import datetime
from decimal import Decimal
# нзва, кількість і ціна 1 товару
item_1_title = textwrap.shorten('Хліб'.ljust(20, '.'), width=20, placeholder='...')
item_1_quantity = 2
item_1_price = Decimal('25.50')

# нзва, кількість і ціна 2 товару
item_2_title = textwrap.shorten('Молоко'.ljust(20, '.'), width=20, placeholder='...')
item_2_quantity = 1
item_2_price = Decimal('38.20')

#вартість
item_1_total_cost = Decimal(item_1_quantity) * item_1_price
item_1_total_cost_right_format = item_1_total_cost.quantize(Decimal('1.00'))

item_2_total_cost = Decimal(item_2_quantity) * item_2_price
item_2_total_cost_right_format = item_2_total_cost.quantize(Decimal('1.00'))

#підсумок перенесли сюди
total_cost = item_1_total_cost_right_format + item_2_total_cost_right_format

printing_template = '{}\t\t\t\t\t{}\t\t\t\t{}\t\t\t{}'

# printing receipt
print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print('Товар\t\t\t\t\t\t\t\t\tкількість\t\tціна\t\tвартість')
print(printing_template.format(item_1_title, item_1_quantity, item_1_price, item_1_total_cost_right_format))
print(printing_template.format(item_2_title, item_2_quantity, item_2_price, item_2_total_cost_right_format))
print('~' * 80)
print(printing_template.format(
    'ВСЬОГО'.ljust(20),
    item_1_quantity + item_2_quantity,
    '',
    '',
    total_cost
       )
)
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')

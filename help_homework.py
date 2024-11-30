import textwrap
from datetime import datetime
from decimal import Decimal

# goods 1 section
item_1_title = textwrap.shorten(input('Булочка з маком: ').ljust(20, '.'), width=20, placeholder='...')
item_1_quantity = int(Decimal(input('3: ')).quantize(Decimal('1')))  # Округлення кількості до цілих
item_1_zina = Decimal(input('15.0: '))

# goods 2 section
item_2_title = textwrap.shorten(input('Апельсиновий сік: ').ljust(20, '.'), width=20, placeholder='...')
item_2_quantity = int(Decimal(input('2: ')).quantize(Decimal('1')))  # Округлення кількості до цілих
item_2_zina = Decimal(input('45: '))

# Розрахунок вартості товарів
item_1_total_cost = (Decimal(item_1_quantity) * item_1_zina).quantize(Decimal('1.00'))  # Форматування до 2 знаків
item_2_total_cost = (Decimal(item_2_quantity) * item_2_zina).quantize(Decimal('1.00'))  # Форматування до 2 знаків

# Шаблон для друку
printing_template = '{}\t\t\t{}\t\t{}\t\t{}'

# Друк чека
print('\n\n\n')
print('фіскальний чек'.capitalize().center(80, '~'))
print('магазин "все для дому"'.upper().center(80))
print(f'Товар\t\t\t\t\t\t\t\tкількість\t\tціна\t\tвартість')
print(printing_template.format(
    item_1_title,
    item_1_quantity,
    f"{item_1_zina:.2f}",
    f"{item_1_total_cost:.4f}"  # Вартість з 4 знаками
))
print(printing_template.format(
    item_2_title,
    item_2_quantity,
    f"{item_2_zina:.2f}",
    f"{item_2_total_cost:.4f}"  # Вартість з 4 знаками
))
print('~' * 80)

# Розрахунок загальної суми
total_cost = (item_1_total_cost + item_2_total_cost).quantize(Decimal('1.00'))

print(printing_template.format(
    'ВСЬОГО'.ljust(20),
    item_1_quantity + item_2_quantity,
    'x',
    f"{total_cost:.4f}"  # Загальна вартість з 4 знаками
))
print(datetime.now().strftime('%d-%m-%Y %H:%M:%S').rjust(80))
print('\n\n')


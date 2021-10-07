# 1. Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат ХХХ минут

# TODO здесь ваш код
print("task 1")
song1_time = violator_songs_dict.get('Sweetest Perfection')
song2_time = violator_songs_dict.get('Policy of Truth')
song3_time = violator_songs_dict.get('Blue Dress')
amount_of_time = song1_time + song3_time + song2_time
print(amount_of_time)
# ===============================


# 2. Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = {}

# TODO здесь заполнение словаря
print("task 2")
site1 = sites.get("Moscow")
mos_x = site1[0]
mos_y = site1[1]
site2 = sites.get("London")
lon_x = site2[0]
lon_y = site2[1]
site3 = sites.get("Paris")
par_x = site3[0]
par_y = site3[1]
distances['MoscowLondon'] = (mos_x - lon_x) ** 2 + (mos_y - lon_y) ** 2
distances['MoscowParis'] = (mos_x - par_x) ** 2 + (mos_y - par_y) ** 2
distances['londonParis'] = (lon_x - par_x) ** 2 + (lon_y - par_y) ** 2
print(distances)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------


# 3. Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп
print("task 3")
lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost1 = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost1, 'руб')

# Вывести стоимость каждого товара на складе: один раз распечать сколько всего столов, стульев и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

# TODO здесь ваш код
table_cost1 = store[goods["Стол"]][0]['quantity'] * store[goods['Стол']][0]['price']
table_cost2 = store[goods["Стол"]][1]['quantity'] * store[goods['Стол']][1]['price']
table_quantity = store[goods["Стол"]][0]["quantity"] + store[goods["Стол"]][1]['quantity']
print('Стол -', table_quantity, 'шт, стоимость', table_cost1 + table_cost2, 'руб')

coach_cost1 = store[goods["Диван"]][0]['quantity'] * store[goods['Диван']][0]['price']
coach_cost2 = store[goods["Диван"]][1]['quantity'] * store[goods['Диван']][1]['price']
coach_quantity = store[goods["Диван"]][0]["quantity"] + store[goods["Диван"]][1]['quantity']
print('Диван -', coach_quantity, 'шт, стоимость', coach_cost1 + coach_cost2, 'руб')

chair_cost1 = store[goods["Стул"]][0]['quantity'] * store[goods['Стул']][0]['price']
chair_cost2 = store[goods["Стул"]][1]['quantity'] * store[goods['Стул']][1]['price']
chair_cost3 = store[goods["Стул"]][2]['quantity'] * store[goods['Стул']][2]['price']
chair_quantity = store[goods["Стул"]][0]["quantity"] + store[goods["Стул"]][1]['quantity'] + store[goods["Стул"]][2]['quantity']
print('Диван -', chair_quantity, 'шт, стоимость', chair_cost1 + chair_cost2 + chair_cost3, 'руб')
# ------------------------------------------------------------------------------------------------------------------


# 4. в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза',)

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка',)

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)
# TODO здесь ваш код
print("task 4")
print(garden_set.union(meadow_set))
# выведите на консоль все виды цветов
# TODO здесь ваш код
print(garden_set.intersection(meadow_set))
# выведите на консоль те, которые растут и там и там
# TODO здесь ваш код
print(garden_set.difference(meadow_set))
# выведите на консоль те, которые растут в саду, но не растут на лугу
# TODO здесь ваш код
print(meadow_set.difference(garden_set))
# выведите на консоль те, которые растут на лугу, но не растут в саду


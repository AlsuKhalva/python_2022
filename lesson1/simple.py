from itertools import count
from pprint import pprint
from unicodedata import name


# a = 2
# b = 0.5
# print(a+b)

# name1 = 'АЛСУ'
# print('Привет,'+ name1.capitalize()+'!')

# name = input('Введите ваше имя: ')
# print(f'Привет, {name}!')
# age = int(input('Сколько вам лет? '))
# birth_year=2022 - age
# print(f'Вы родились в {birth_year} году.')

# v = int(input('Введите число  от 1 од 10: '))
# print(v + 10)

# name = input('Введите ваше имя: ')
# print(f'Привет, {name}! Как дела?')

# print(float('1'))
# a = float('2.5')
# print(int(a))
# print(bool(1))
# print(bool(''))
# print(bool(0))

# phones = ['iPhone 12', 'Samsung Galaxy S21', 'Xiaomi Mi11']
# # print(phones)
# # count= len(phones)
# # print(count)

# phones.append('iPhone 12')
# print(phones)
# count= len(phones)
# print(count)
# print(phones.count('iPhone 12'))
# print(phones.count('iPhone 9'))
# print(phones[1])
# # print(phones[6])
# print(phones[1:3])
# print(phones[:2])
# print(phones[-1])

# phones = ['iPhone 12', 'Samsung Galaxy S21', 'Xiaomi Mi11', 'iPhone 12']
# # print(phones.index('Xiaomi Mi11'))
# # phones.sort()
# # print(phones)
# # print(phones.index('Xiaomi Mi11'))
# # print('iPhone 12' in phones)
# # print('iPhone 9' in phones)

# del phones[1]
# print(phones)
# phones.remove('iPhone 12')
# print(phones)
# phones.remove('Samsung Galaxy S21')
# print(phones)

# number_list = [3,5,7,9,10.5]
# print(number_list)
# number_list.append('Python')
# print(number_list)
# print(len(number_list))
# print(number_list[0])
# print(number_list[-1])
# print(number_list[2:5])
# number_list.remove('Python')
# print(number_list)

product = {
    'name': 'iPhone 12',
    'stock': 24,
    'price': 65432.1
}
# # print(product)
# # print(len(product))
product['memory'] = 64
# print(product)
# product['name']= 'iPhone 12 Pro'
# print(product)
# print(product['price'])
# print(product['stock'])
# # print(product['discount'])
# print(product.get('name'))
# print(product.get('discount'))
# print(product.get('discount', 0))
# print(product.get('country', 'CN'))
# print(product.get('name', 0))

# del product['stock']
# print(product)
# del product['discount']

phones = ['Samsung Galaxy S21', 'iPhone 12']
product['recomended'] = phones
# pprint(product)
print(product['recomended'])
product['recomended'].append('Xiaomi Mi11')
print(len(product['recomended']))
print(product['recomended'][0])

stock = [
    {'name': 'iPhone 12 Plus', 'stock': 24, 'price': 65432.1, 'recomended': ['Samsung Galaxy S21', 'iPone12']},
    {'name': 'Samsung Galaxy S21', 'stock': 8, 'price': 50000.00, 'discount': 5000},
    {'name': 'Xiaomi Mi11', 'stock': 42, 'price': 38000.5}
]
print(stock)
print(stock[2])
stock[2]['price']= stock[2]['price'] - 8000
print(stock[2]['price'])
print(stock[0]['recomended'][1])
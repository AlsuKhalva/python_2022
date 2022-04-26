def format_price(price):
    price = int(price)
    return f'Цена: {price} руб.'

price1 = format_price(56.4)
print(price1)
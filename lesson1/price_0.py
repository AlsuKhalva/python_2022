def discounted(price, discount, max_discount=20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount>=100:
        raise ValueError('Слишком большая скидка')
    if discount >=max_discount:
        return price
    else:
            price_with_discount = price - (price * discount / 100)
    return(price_with_discount)

# price1 = 100
# discount1 = 10
# discounted(price1, discount1)

# discounted(200, 5)
# discounted(100, 101)

# product = {'name': 'Samsung Galaxy S21', 'price': 50000.00, 'discount': 5}
# product['price_discounted'] = discounted(product['price'], product['discount'])
# print(product)

print(discounted(100, 50))
print(discounted(100, 50, max_discount=60))
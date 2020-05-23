phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}
phone3 = {'name': '', 'stock': 18, 'price': 10000, 'discount': 10}

def discounted(price,discount,max_discount=20,name=''):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(float(max_discount))
        if max_discount > 99:
            raise ValueError ('Слишком большая максимальная скидка')
        if discount >= max_discount or "iphone" in name.lower() or not name:
            print (price)
        else:
            print (price - price * discount / 100)
    except ValueError:
        print("Введите число")
    
discounted(5643,6356)
discounted('iphone',9)
discounted(5643,6356)
discounted(4637,109)
discounted(9883,'samsung')
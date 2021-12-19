### Exercise 1 ###
class Market:
    """
    Desc:
    First arg = price
    Second arg = desc
    Third arg = dim
    """
    def __init__(self, price, desc, dim):
        self.price = price
        self.desc = desc
        self.dim = dim

    def __str__(self):
        return f'{self.price} {self.desc} {self.dim}.'


### Exercise 2 ###
class Customer:
    """
    Desc:
    First arg = First name
    Second arg = Last name
    Third arg = Phone number
    fourth arg = Birthday
    """
    def __init__(self, first_name, last_name, phone, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.birthday = birthday

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.birthday}.'


### Exercise 3 ###
class Order:
    def __init__(self, customer: Customer, products=None):
        self.customer = customer
        self.products = products

    def add_item(self):
        s = 0
        for item in self.products:
            s += item.price
        return s

    def __str__(self):
        res = '\n'.join(map(str, self.products))
        return f'{self.customer}\n{res}\nTotal price: {self.add_item()} UAH'


if __name__ == '__main__':
    x = Market(5, 'apple', '1x1')
    y = Market(7, 'banana', '2x2')
    z = Market(9, 'orange', '3x3')

    customer_1 = Customer('Vlad', 'Vasev', '555-44-55', '13-04-1945')
    customer_2 = Customer('Evgeniy', 'Jukov', '444-11-22', '21-08-1962')

    order_1 = Order(customer_1, [x, z, x])
    order_2 = Order(customer_2, [x, x, x, z, y])

    print(order_1, order_2, sep='\n')

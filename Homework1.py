### Exercise 1 ###
class Market:
    def __init__(self, price, desc, dim):
        """

        :param price:
        :param desc:
        :param dim:
        """
        if not isinstance(price, int) or not isinstance(desc, str) or not isinstance(dim, str):
            raise TypeError('Invalid params')
        if not price or not desc or not dim:
            raise ValueError('Empty price or desc or dim')
        if price < 0:
            raise ValueError('Price lower then 0')

        self.price = price
        self.desc = desc
        self.dim = dim

    def __str__(self):
        return f'{self.price} {self.desc} {self.dim}.'


### Exercise 2 ###
class Customer:
    def __init__(self, first_name, last_name, phone, birthday):
        """

        :param first_name:
        :param last_name:
        :param phone:
        :param birthday:
        """
        if isinstance(first_name, str) and isinstance(last_name, str) and isinstance(phone, str) and isinstance(birthday, str):
            self.first_name = first_name
            self.last_name = last_name
            self.phone = phone
            self.birthday = birthday
        else:
            raise TypeError('Invalid params1')

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.phone} {self.birthday}.'


### Exercise 3 ###
class Order:
    def __init__(self, customer: Customer, products=None):
        """

        :param customer:
        :param products:
        """
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
    try:
        x = Market(5, 'apple', '1x1')
        y = Market(7, 'banana', '2x2')
        z = Market(9, 'orange', '3x3')
    except Exception as error:
        print(error)
    try:
        customer_1 = Customer('Vlad', 'Vasev', '555-44-55', '13-04-1945')
        customer_2 = Customer('Evgeniy', 'Jukov', '444-11-22', '21-08-1962')
    except Exception as error:
        print(error)
    try:
        order_1 = Order(customer_1, [x, z, x])
        order_2 = Order(customer_2, [x, x, x, z, y])
    except Exception as error:
        print(error)
    try:
        print(order_1, order_2, sep='\n')
    except Exception as error:
        print(error)
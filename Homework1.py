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


boots1 = Market(5,'Сандали','4x10')
boots2 = Market(8,'Кроссовки','5x10')
print(boots1, boots2, sep='\n')


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


customer1 = Customer('Anatoliy','Vlasov','+38(096)555-22-31','13.04.1999')
customer2 = Customer('Evgeniy','Onegim','+38(066)666-22-31','13.07.1666')
print(customer1, customer2, sep='\n')


### Exercise 3 ###
class Order:
    """
    Desc:
        __init__ args:
            First arg = First name
            Second arg = Last name
            Third arg = Phone number
            fourth arg = Birthday
        add_item args:
            First arg = product
            Second arg = price
    """
    def __init__(self, first_name, last_name, phone, address):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address

        self.order = []
        self.summ = 0

    def add_item(self, product, price):
        self.order.append(product)
        self.summ += price

    def __str__(self):
        return f"Items: {', '.join(self.order)}" \
               f"\ntotal cost: {self.summ} UAH" \
               f"\nAddress: {self.address}" \
               f"\nName: {self.first_name} {self.last_name}"\
               f"\nPhone: {self.phone}"


client1 = Order("Anatoliy", "Vlasov", "+38(096)555-22-31", "Mayakovskogo 5, kv104")
client1.add_item("pizza", 300)
client1.add_item("burger", 150)
print(client1)

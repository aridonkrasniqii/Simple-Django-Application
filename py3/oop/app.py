# from item import Item
# from phone import Phone
#
# Item.instantiate_from_csv()
# print(Item.all)


class Item:

    def __init__(self, name, price, quantity=-1):
        self.__name = name
        self.__price = price
        self.quantity = quantity

    @property
    # Read Only Attribute
    # Get
    def name(self):
        return self.__name

    @name.setter
    # Set
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long !")
        else:
            self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise Exception("Price should be more than zero")
        else:
            self.__price = value

    def __connect(self):
        pass

    def __prepare_body(self):
        return f"""
            Hello Someone.
            We have {self.name} {self.quantity} times.
            Regards , Aridon Krasniqi
            """

    def __send(self):
        pass

    def send_email(self):
        self.__connect()
        self.__prepare_body()
        self.__send()


item1 = Item('Laptop', 2)
item1.name = 'MyItem'
item1.price = 100
print('Price: ' + str(item1.price))
print(item1.name)

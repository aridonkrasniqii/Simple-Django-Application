import csv


class Item:
    all = []

    def __init__(self, name, price, quantity):
        assert price >= 0, f"Price {self.price} is not greater than zero"
        assert quantity >= 0, f"Quantity {self.quantity} is not greater than zero"

        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculateTotalPrice(self):
        return self.price * self.quantity

    def __repr__(self):
        return f'{self.__class__.__name__} \'{self.name}\' , {self.price} , {self.quantity}'


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, broken_phones=0):
        # Call to super function to have access to all attributes / methods
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, f"Broken phones {self.broken_phones} are not greater than zero"

        self.broken_phones = broken_phones


 

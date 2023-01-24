#
#
#
#

import csv


class Item:
    all = []
    payRate = 0.8

    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def applyDiscount(self):
        self.price = self.price * self.payRate

    def calculateTotalPrice(self):
        return self.price * self.quantity

    # How the object is going to be represented when it is created
    def __repr__(self):
        return f"Item ('{self.name}', {self.price} , {self.quantity})"

    # static method or a class method
    # class methods receive are sending the class reference as a first argument
    @classmethod
    def instantiateFromCsv(cls):
        # cls is generated because is a class method
        # f is content of our file
        with open('./venv/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def isInteger(num):
        # We will count out the floats that are point zero

        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer()  # returns true or false
        elif isinstance(num, int):
            return True
        else:
            return False


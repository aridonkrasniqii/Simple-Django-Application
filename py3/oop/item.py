import csv


class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity: int):
        assert quantity >= 0, "Quantity is not greater than zero"
        assert price >= 0, "Price is not greater than zero"
        self.name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}' ,{self.price} , {self.quantity})"

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price += self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open('./venv/items.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(name=item.get('name'),
                 price=float(item.get('price')),
                 quantity=int(item.get('quantity')))



Item.instantiate_from_csv()
print(Item.all)

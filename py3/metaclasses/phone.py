from item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, broken_phones=0):
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken phones {broken_phones} is not equal or greater than zero"

        self.broken_phones = broken_phones

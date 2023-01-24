from item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, broken_phones: int):
        super().__init__(
            name, price, quantity
        )
        assert broken_phones >= 0, "Broken phones are not greater than zero"

        self.broken_phones = broken_phones

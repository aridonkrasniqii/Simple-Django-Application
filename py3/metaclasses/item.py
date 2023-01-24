import csv


class Item:
    pay_rate = 0.8  # The pay rate after 20% discount
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        assert price > 0, f"Price {price} is not greater than or equal to zero !"
        assert quantity > 0, f'Quantity {quantity} is not greater than or equal to zero !'
        self.__name = name
        self.__price = price
        self.__quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.__price * self.__quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.__price}' , {self.__price} , {self.__quantity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as file:
            reader = csv.DictReader(file)

            items = list(reader)

            for item in items:
                Item(
                    name=item.get("name"),
                    price=float(item.get("price")),
                    quantity=int(item.get("quantity"))
                )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # for i.e: 5.0, 10.0
        pass
        if isinstance(num, float):
            # count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    @property
    # Property Decorator = Read-Only Attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            raise Exception("The name is too long !")
        else:
            self.__name = name

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity):
        self.__quantity = quantity

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    # private method
    def __connect(self, smpt_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello Someone.
        We have {self.name} {self.quantity} times.
        Regards, JimShapedCoding
        """

    def __send(self):
        pass

    def send_email(self):
        self.__connect('11.10.11.0')
        self.__prepare_body()
        self.__send()



Item.instantiate_from_csv() 
print(Item.all)
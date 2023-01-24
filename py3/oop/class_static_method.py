# When to use class methods and when to use static methods ?


class Item:
    
    @staticmethod
    def is_integer():
        """
        This should do something that has a relationship
        with class, but not something that must be unique
        per instance !
        :return:
        """

    @classmethod
    def instantiateFromSomething(cls):
        """
        The reason that we use class methods is to instantiate instances
        from some structured data, csv , database etc
        :return:
        """



print("aridon kransiqi")




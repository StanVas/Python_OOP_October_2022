class Product:
    def __init__(self, name: str, price: float):
        self.__name = name
        self.__price = price

    # we make it accessible, so we can see it and use it,
    # but we can't modify it because we don't have @setter
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

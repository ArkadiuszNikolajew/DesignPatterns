class Product:

    def __init__(self, name: str, price: float = 0) -> None:
        self.name = name
        self._price = price

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("Price below 0 is not possible")
        self._price = value

from product import Product
import payment_strategies


class ShoppingCart:

    def __init__(self) -> None:
        self.items: list = []

    def add_product(self, product: Product) -> None:
        self.items.append(product)

    def remove_product(self, product: Product) -> None:
        self.items.remove(product)

    def total_price(self) -> float:
        total = 0
        for item in self.items:
            total += item.price
        return total

    def pay(self, method: payment_strategies.PaymentStrategy) -> None:
        total_price = self.total_price()
        print(f'{method.pay(total_price)}')

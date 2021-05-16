import abc


class PaymentStrategy(abc.ABC):

    @abc.abstractmethod
    def pay(self, price: float) -> str:
        pass


class CreditCardStrategy(PaymentStrategy):

    def __init__(self, card_number: str, owner: str, cvv: str, expire_date: str) -> None:
        self.card = card_number
        self.owner = owner
        self.cvv = cvv
        self.expire_date = expire_date

    def pay(self, price: float) -> str:
        return f'{price} paid with card {self.card}'


class BlikStrategy(PaymentStrategy):

    def __init__(self, email: str, code: str) -> None:
        self.email = email
        self.code = code

    def pay(self, price: float) -> str:
        return f'{price} paid with BLIK'

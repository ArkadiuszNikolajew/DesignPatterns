from product import Product
from shopping_cart import ShoppingCart
from payment_strategies import BlikStrategy, CreditCardStrategy

if __name__ == '__main__':
    product1 = Product('Banana', 4.99)
    product2 = Product('Apple', 2.99)
    cart = ShoppingCart()
    cart.add_product(product1)
    cart.add_product(product2)
    cart.pay(BlikStrategy('a@exapmple.com', '123456'))
    cart.pay(CreditCardStrategy('4111 1111 4555 1142', 'Jon Snow', '456', '09/27'))

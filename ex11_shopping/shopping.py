"""Store imitation."""

# TODO: create class for custom exception.


class Product:
    """Represents product model."""

    def __init__(self, name: str, price: int) -> None:
        """
        Class constructor. Each product has name and price.

        :param name: product name
        :param price: product price
        """
        pass

    def __str__(self) -> str:
        """
        Product object representation in string format.

        :return: string
        """
        pass

    def __repr__(self) -> str:
        """
        Product object representation in object format.

        :return: string
        """
        pass


class Customer:
    """Represents customer model."""

    def __init__(self, name: str, age: int, money: int) -> None:
        """
        Class constructor. Each customer has name, age and money when being created.

        Customer also has storage for bought items.
        :param name: customer's name
        :param age: customer's age
        :param money: customer's money
        """
        pass

    def add_item(self, product: Product, amount: int) -> None:
        """
        Add bought items to customer's items.

        :param product: product
        :param amount: amount
        """
        pass

    def pay(self, money_to_pay: int) -> None:
        """
        Checks if customer has enough money to pay for the product.

        Returns nothing, but raises exception if customer has not enough money to pay.
        In other case reduces amount of customer's money.
        :param money_to_pay: money amount needed to be paid
        """
        pass

    def __str__(self) -> str:
        """
        Customer object representation in string format.

        :return: string
        """
        pass


class Store:
    """Represents store model."""

    def __init__(self) -> None:
        """Class constructor."""
        pass

    def buy(self, product: Product, amount: int, customer: Customer) -> str:
        """
        Represents how customer buys product.

        :param product: product the customer wants
        :param amount: pieces of product
        :param customer: customer who wants to buy
        :return: message
        """
        pass

    def allowed_to_buy(self, product: Product, customer: Customer):
        """
        Checks if customer is allowed to buy some particular products.

        Permission depends on customer's age

        Customers under 18 are not allowed to buy alcohol and tobacco.
        Must raise exception if customer has no permission to buy chosen product.
        :param product: product to buy
        :param customer: customer who makes the purchase
        """
        pass

    def check_product_availability(self, product: Product, amount: int):
        """
        Checks if chosen amount of product is present in stock.

        Must raise exception if no product found or not enough in stock.
        :param product: product to be bought
        :param amount: amount of product
        """
        pass

    def add_product(self, product: Product) -> None:
        """
        Adding product to store.

        :param product:  product name
        """
        pass

    def __str__(self) -> str:
        """
        Store's object representation in string format.

        :return: string
        """
        pass


if __name__ == "__main__":
    john = Customer("John", 20, 300)
    bobby = Customer("Bobby", 17, 150)
    sandy = Customer("Sandy", 12, 100)

    store = Store()

    beer = Product("beer", 50)
    water = Product("water", 30)
    choco = Product("chocolate", 45)
    pretzel = Product("pretzel", 35)

    store.add_product(beer)
    store.add_product(water)
    for _ in range(3):
        store.add_product(choco)
        store.add_product(pretzel)

    print(store.buy(beer, 1, john))  # -> Thank you for the purchase!
    print(beer not in store.products)  # -> True
    print(john)  # -> John's items: beer; money: 250.

    tobacco = Product("tobacco", 55)
    store.add_product(tobacco)
    print(store.buy(tobacco, 1, bobby))  # -> You are too young to buy Product: tobacco, price: 55!

    print(store.buy(water, 2, sandy))  # -> Item is not available in chosen amount!

    candy = Product("candy", 25)
    print(store.buy(candy, 1, bobby))  # -> Item not found!

    store.buy(choco, 2, bobby)
    print(store.products.count(choco))  # -> 1
    print(bobby.money)  # -> 60
    store.buy(water, 1, bobby)
    print(bobby)  # -> Bobby's items: chocolate(2), water; money: 30


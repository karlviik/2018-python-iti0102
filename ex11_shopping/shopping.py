"""Store imitation."""


class ProductCannotBeSold(Exception):
    """Exception raised when it's not allowed or possible to make the sale."""

    pass


class Product:
    """Represents product model."""

    def __init__(self, name: str, price: int) -> None:
        """
        Class constructor. Each product has name and price.

        :param name: product name
        :param price: product price
        """
        self.name = name
        self.price = price

    def __str__(self) -> str:
        """
        Product object representation in string format.

        :return: string
        """
        return f"Product: {self.name}, price: {self.price}"

    def __repr__(self) -> str:
        """
        Product object representation in object format.

        :return: string
        """
        return self.name


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
        self.name = name
        self.age = age
        self.money = money
        self.items = {}

    def add_item(self, product: Product, amount: int) -> None:
        """
        Add bought items to customer's items.

        :param product: product
        :param amount: amount
        """
        try:
            if product.name not in self.items.keys():
                self.items[product.name] = amount
            else:
                self.items[product.name] += amount
        except KeyError:
            raise IndexError

    def pay(self, money_to_pay: int) -> None:
        """
        Check if customer has enough money to pay for the product.

        Returns nothing, but raises exception if customer has not enough money to pay.
        In other case reduces amount of customer's money.
        :param money_to_pay: money amount needed to be paid
        """
        if money_to_pay > self.money:
            raise ProductCannotBeSold("You do not have enough money to pay for chosen product!")
        else:
            self.money -= money_to_pay

    def __str__(self) -> str:
        """
        Customer object representation in string format.

        :return: string
        """
        try:
            itemlist = []
            for item, amount in self.items.items():
                if amount > 1:
                    item += f"({amount})"
                itemlist.append(item)
            if len(itemlist) > 1:
                stringitemlist = ", ".join(itemlist)
            else:
                stringitemlist = itemlist[0]
            return f"{self.name}'s items: {stringitemlist}; money: {self.money}."
        except KeyError:
            raise IndexError


class Store:
    """Represents store model."""

    def __init__(self) -> None:
        """Class constructor."""
        self.money = 0
        self.products = {}

    def buy(self, product: Product, amount: int, customer: Customer) -> str:
        """
        Represent how customer buys product.

        :param product: product the customer wants
        :param amount: pieces of product
        :param customer: customer who wants to buy
        :return: message
        """
        try:
            try:
                self.check_product_availability(product, amount)
                self.allowed_to_buy(product, customer)
                customer.pay(amount * product.price)
                customer.add_item(product, amount)
                self.products[product.name] -= amount
                self.money += product.price * amount
                return "Thank you for the purchase!"
            except ProductCannotBeSold as errormessage:
                return errormessage
        except KeyError:
            raise IndexError


    def allowed_to_buy(self, product: Product, customer: Customer):
        """
        Check if customer is allowed to buy some particular products.

        Permission depends on customer's age

        Customers under 18 are not allowed to buy beer and tobacco.
        Must raise exception if customer has no permission to buy chosen product.
        :param product: product to buy
        :param customer: customer who makes the purchase
        """
        try:
            if customer.age < 18 and (product.name == "beer" or product.name == "tobacco"):
                raise ProductCannotBeSold(f"You are too young to buy {product.name}!")
        except KeyError:
            raise IndexError

    def check_product_availability(self, product: Product, amount: int):
        """
        Check if chosen amount of product is present in stock.

        Must raise exception if no product found or not enough in stock.
        :param product: product to be bought
        :param amount: amount of product
        """
        try:
            if product.name not in self.products.keys():
                raise ProductCannotBeSold("Item not found!")
            elif self.products[product.name] < amount:
                raise ProductCannotBeSold("Item is not available in chosen amount!")
        except KeyError:
            raise IndexError

    def add_product(self, product: Product) -> None:
        """
        Adding product to store.

        :param product:  product name
        """
        try:
            if product.name not in self.products.keys():
                self.products[product.name] = 1
            else:
                self.products[product.name] += 1
        except KeyError:
            raise IndexError

    def __str__(self) -> str:
        """
        Store object representation in string format.

        :return: string
        """
        try:
            itemlist = []
            for item, amount in self.products.items():
                if amount > 1:
                    item += f"({amount})"
                if amount:
                    itemlist.append(item)
            if len(itemlist) > 1:
                stringitemlist = ", ".join(itemlist)
            elif len(itemlist):
                stringitemlist = itemlist[0]
            else:
                stringitemlist = ""
            return f"Store items: {stringitemlist}; store money: {self.money}."
        except KeyError:
            raise IndexError


if __name__ == "__main__":
    john = Customer("John", 20, 300)

    store = Store()

    choco = Product("chocolate", 45)

    for _ in range(2):
        store.add_product(choco)

    print(store.buy(choco, 1, john))  # -> Thank you for the purchase!
    print(john)  # -> John's items: beer; money: 250.
    print(store)
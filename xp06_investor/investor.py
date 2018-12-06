"""Get a decent investing plan based on math and stuff."""
import csv


def get_currency_rates_from_file(filename: str) -> tuple:
    """
    Read and return the currency and exchange rate history from file.
    See web page:
    https://www.eestipank.ee/valuutakursside-ajalugu

    Note that the return value is tuple, that consists of two things:
    1) currency name given in the file.
    2) exchange rate history for the given currency.
        Note that history is returned using dictionary where keys represent dates
        and values represent exchange rates for the dates.

    :param filename: file name to read CSV data from
    :return: Tuple that consists of currency name and dict with exchange rate history
    """
    # Opens the file.
    with open(filename) as csv_file:
        # Saves the file as a csv.reader object and separates the lines in file to lists of strings which were separated by the delimiter.
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Loops over each line in file.
        for row in csv_reader:
            # Prints the list of strings in that line.
            if row[0] == "":
                currency = row[1]
            elif row[1] != "":


    return ("USD", {
        "01.01.2017": 1.0234,
        "02.01.2017": 1.0101,
        "03.01.2017": 1.0099
    })


def exchange_money(exchange_rates: dict) -> list:
    """
    Find best dates to exchange money for maximum profit.

    You are given a dictionary where keys represent dates and values represent exchange
    rates for the dates. The amount you initially have is 1000 and you always use the
    maximum amount during the exchange.
    Be aware that there is 1% of service fee for every exchange. You only need to return
    the dates where you take action. That means the first action is always to buy the
    second currency and the second action is to sell it back. Repeat the sequence as
    many times as you need for maximum profit. You should always end up having the
    initial currency. That means there should always be an even number of actions. You can
    also decide that the best decision is to not make any transactions at all, if
    for example the rate is always dropping. In that case just return an empty list.

    :param exchange_rates: dictionary of dates and exchange rates
    :return: list of dates
    """
    return [
        "01.01.2017",
        "03.01.2017"
    ]

print(get_currency_rates_from_file("currency-rates.csv"))
"""Get a decent investing plan based on math and stuff."""
import csv
import datetime


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
    rates = {}
    # Opens the file.
    with open(filename) as csv_file:
        # Saves the file as a csv.reader object and separates the lines in file to lists of strings which were separated by the delimiter.
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Loops over each line in file.
        for row in csv_reader:
            if row[0] == "":
                currency = row[1]
            elif row[1] != "":
                rates[row[0]] = float(row[1])
    print(rates)
    return currency, rates


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
    def actualscanner(index):
        while True:
            if dateprices[index][1]:
                top = dateprices[index][0]
                break
            index += 1
        do_i_have_profit = False
        pricelist = []
        index += 1
        indexlimit = len(dateprices)
        while True:
            newprice = dateprices[index]
            if not do_i_have_profit:  # if  yet do not have a profitable bottom
                if newprice[1] and newprice[0][1] > top[1]:  # if I've gotten a top that is higher than current top
                    return index, pricelist  # return the index and pricelist
                elif not newprice[1]:  # if I've gotten a bottom
                    if newprice[0][1] < 0.9801 * top[1]:  # if the bottom is profitable
                        do_i_have_profit = True  # change the flag to true
                        pricelist = [top, newprice[0]]  # and add the top and profitable bottom pair to pricelist
                    elif not pricelist:  # if the list is empty and I got an unprofitable bottom
                        pricelist = [newprice[0]]  # add it to the list alone
                    elif pricelist[0][1] < newprice[0][1]:  # if current solo unprofitable bottom is higher than scanned unprofitable bottom
                        pricelist = [newprice[0]]  # overwrite the other one (could have combined, but clarity)
            else:  # if I do have a pair in pricelist
                if newprice[1]:  # if dealing with a top
                    if newprice[0][1] > top[1]:  # if scanned top higher than current top:
                        return index, pricelist
                    elif newprice[0][1] > pricelist[-1][1] / 0.99:  # if scanned top has potential to be profitable:
                        index, newprices = actualscanner(index)
                        index -= 1  # to counteract the +1 at the end of loop
                        if len(newprices) == 1:  # if returned newprice list only has a bottom:
                            if newprices[0][1] < pricelist[-1][1]:  # if that bottom is lower than current bottom
                                pricelist[1] = newprices[0]  # replace it
                        else:
                            pricelist += newprices
                else:  # if dealing with a bottom
                    if pricelist[-1][1] > newprice[0][1]:  # if scanned bottom is lower than last bottom saved
                        pricelist[-1] = newprice[0]  # replace it
            index += 1
            if index >= indexlimit:
                break
        return index, pricelist

    exchange_rates["31.12.9999"] = float("inf")
    goingup = True
    last = [[0, 0], 0]
    maxprice = 0
    minprice = float("inf")
    dateprices = []
    for date, price in sorted(exchange_rates.items(), key=lambda x: datetime.datetime.strptime(x[0], "%d.%m.%Y").date()):

        price = float(price)
        if goingup:
            if last[0][1] > price:
                dateprices.append(last)
                goingup = False
                if maxprice < last[0][1]:
                    maxprice = last[0][1]
        else:
            if last[1] < price:
                dateprices.append(last)
                goingup = True
                if minprice > last[0][1]:
                    minprice = last[0][1]
        last = [[date, price], goingup]

    print(maxprice, minprice)
    if maxprice / minprice * 0.99 ** 2 <= 1:
        return []

    index = 0
    endlist = []
    while True:
        index, lists = actualscanner(index)
        if len(lists) > 1:
            endlist += lists
        print(endlist)
        if index >= len(dateprices):
            break

    dates = []
    tomato = False
    potato = 1000
    for sublist in endlist:
        dates.append(sublist[0])
        if not tomato:
            tomato = True
            potato = potato * sublist[1] * 0.99
        else:
            tomato = False
            potato = potato / sublist[1] * 0.99
            print(potato)
    return dates


if __name__ == '__main__':
    a, b = get_currency_rates_from_file("currency-rates.csv")
    print(exchange_money(b))

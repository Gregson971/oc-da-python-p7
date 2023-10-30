import pandas as pd
from itertools import combinations
from tabulate import tabulate
from pyinstrument import Profiler

MAXIMUM_SPENDING_AMOUNT = 500


def get_data(path):
    """
    Get the data from the csv file
    :param path: path to the csv file
    :return: data
    """
    # Read the data
    df = pd.read_csv(path)

    # Convert the data to a dictionary
    data = df.to_dict('records')

    return data


def find_best_combination(data):
    """
    Find the best combination of shares
    :param data: data
    :return: best_combination
    """

    best_combination = None
    best_profit = 0

    for i in range(len(data)):
        for combination in combinations(data, i):
            total_price = get_total_price(combination)
            total_profit = get_total_profit(combination)
            if total_price <= MAXIMUM_SPENDING_AMOUNT and total_profit > best_profit:
                best_profit = total_profit
                best_combination = combination

    return best_combination


def get_total_profit(data):
    """
    Calculate the total profit
    :param data: data
    :return: profit
    """

    total = sum((item['profit'] / 100) * item['price'] for item in data)

    return round(total, 2)


def get_total_price(data):
    """
    Calculate the total price
    :param data: data
    :return: price
    """

    total = sum(item['price'] for item in data)

    return round(total, 2)


def display_results(best_combination):
    """
    Display the results
    :param best_combination: best_combination
    :return: None
    """

    if best_combination:
        print("Best combination possible:")
        print()
        print(tabulate(best_combination, headers="keys", tablefmt="fancy_grid"))
        print()
        print(f"Number shares bought: {len(best_combination)}")
        print(f"Total price: {get_total_price(best_combination)}€")
        print(f"Total profit: {get_total_profit(best_combination)}€")
    else:
        print("Aucune combinaison trouvée avec le budget donné.")


# Main function
if __name__ == '__main__':
    profiler = Profiler()
    profiler.start()

    data = get_data('data/dataset_test_shares.csv')
    best_combination = find_best_combination(data)
    display_results(best_combination)

    profiler.stop()
    profiler.print()

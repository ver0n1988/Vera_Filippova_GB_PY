bakery = "./bakery.csv"


if __name__ == "__main__":

    import sys

    user_prices = list(map(lambda y:  f"{float(y):100.2f}", filter(
        lambda x: x.replace(".", "").isdigit(), sys.argv[1:])))

    with open(bakery, 'a', encoding='utf-8') as file_1:
        print(*user_prices, sep='\n', file=file_1)
import utils

if __name__ == "__main__":
    while True:
        cur_code=input('введите наименование валюты: ')
        print(utils.currency_rates(cur_code))


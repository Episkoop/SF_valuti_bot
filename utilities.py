import requests
import json
from config import keys


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Одинаковые валюты: {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}, используйте комманду /help')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}, используйте комманду /help')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не верное количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
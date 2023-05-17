import  requests
import json
from config import keys




class ConvertionExcepcion(Exception):
    pass

class CriptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExcepcion(f'Невозмоно перевести одинаковые валюты {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExcepcion(f'Неудалось обработать валюту {quote}.')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExcepcion(f'Неудалось обработать валюту {base}.')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExcepcion(f'Неудалось обработать количествою{amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base
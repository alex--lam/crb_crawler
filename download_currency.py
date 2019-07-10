import requests
from currency import currency
from datetime import datetime
from parser_cbr import CurrencyParser
from xml_writer import XmlWriter
import sys


class Loader:
    url: str = 'http://www.cbr.ru/currency_base/dynamics/'

    def download(self, currency_id: str, date_from: str, date_to: str):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
        }
        params = self.__get_params__(currency_id,
                                     self.__format_date(date_from),
                                     self.__format_date(date_to))
        req = requests.get(self.url, headers=headers, params=params)
        parser = CurrencyParser()
        curr = parser.parse_currency(req.text)


    def __get_params__(self, currency_id: str, date_from, date_to):
        return {
            "UniDbQuery.FromDate": date_from,
            "UniDbQuery.ToDate": date_to,
            "UniDbQuery.VAL_NM_RQ": currency[currency_id],
            "UniDbQuery.Posted": True
        }

    def __format_date(self, date: str):
        if date is None or date == "":
            return datetime.now().strptime("%d.%m.%Y")
        return date

    def write_currency_to_file(self, rows):
        return XmlWriter.write_to_mysql_format(rows);


#Loader().download("USD", "10.10.2018", "20.10.2018")
Loader().download(sys.argv[1], sys.argv[2], sys.argv[3])
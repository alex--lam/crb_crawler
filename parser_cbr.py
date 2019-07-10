from bs4 import BeautifulSoup


class CurrencyParser:
    def parse_currency(self, html: str):
        soup = BeautifulSoup(html, features="html.parser")
        table = soup.select("table.data td")
        i = 1 #skip first
        result = []
        while i < len(table):
            result.append({
                "date": table[i].text,
                "amount": table[i+1].text,
                "cost":  table[i+2].text,
            })
            i += 3
        return result

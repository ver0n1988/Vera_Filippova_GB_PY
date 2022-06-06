import requests


def currency_rates(cur_code="", url="http://www.cbr.ru/scripts/XML_daily.asp"):
    if not (cur_code and url):
        return None

    cur_code = cur_code.upper()
    req = requests.get(url)

    if req.ok:
        cur = req.text.split(cur_code)

        if len(cur) == 1:
            return None

        value = cur[1].split("</Value>")[0].split("<Value>")[1]
        value = float(value.replace(",", "."))

        return (value)

    else:
        return None

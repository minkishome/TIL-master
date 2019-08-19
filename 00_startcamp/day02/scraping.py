import requests
import bs4

url = 'https://finance.naver.com/marketindex/?tabSel=exchange#tab_section'
response = requests.get(url).text

# 요청을 통해서 ___에 있는 것을 가져오겠다. 뱉어내겠다.

# python scraping.py

text = bs4.BeautifulSoup(response, 'html.parser')

exchange_rate = text.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(exchange_rate.text)

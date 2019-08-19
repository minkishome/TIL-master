from iexfinance.stocks import Stock

company = Stock('AAPL', token = token)

print(company.get_quote())

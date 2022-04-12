import yfinance as yf

msft = yf.Ticker("MSFT")

# get stock info
msft.info

for m in msft.info:
  print(m, msft.info[m])

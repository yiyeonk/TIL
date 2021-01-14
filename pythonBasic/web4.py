import urllib.request as req
from bs4 import BeautifulSoup


url = "https://finance.naver.com/marketindex/?tabSel=exchange#tab_section"
res = req.urlopen(url).read().decode('euc-kr')

soup = BeautifulSoup(res, "html.parser")
print(soup)


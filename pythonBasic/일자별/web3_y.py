from bs4 import BeautifulSoup

html = """
<html><body>
<h1>스크래핑</h1>
<p>웹 페이지 분석</p>
<p>원하는 부분 추출</p>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
# 클래스(대문자 시작)
print(soup.html.body.h1)
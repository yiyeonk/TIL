# # sub함수
# #
# #
# # 대한민국, 한국, 코리아 ... => 대한민국
#
# # import re
# # if re.match("\d{4}$","12345"):
# #     print("정상 전화번호")
# # else :
# #     print("비정상 전화번호")
# #
# #
# # #re.sub("패턴","바꿀문자열", "문자열",바꿀횟수)
# # print(re.sub("apple|orange", "fruit","apple tree banana orange"))
# #
# # # "1 2 apple 3 banana 4 7 9 30 tree"
# # # 수치데이터 => "num"으로 변경
# # print(re.sub("[0-9]+", "num","1 2 apple 3 banana 4 7 9 30 tree",1))
# #
# # print(re.sub("[0-9]+", "num","1 2 apple 3 banana 4 7 9 30 tree",3))
# #
# #
# # # print(re.sub("apple|orange", "fruit","apple tree banana orange",1))
# # # print(re.sub("apple|orange", "fruit","apple tree banana orange",count=1))
# #
# #
# # print(re.sub("apple|orange", "fruit","apple tree banana orange"))
# # print("="*50)
# # pat=re.compile("apple|orange")
# # print(pat.sub("fruit","apple tree banana orange",1))
#
# #[0-9]:\d, 공백/탭/엔터문자:\s, 문자/숫자:\w
#
# #https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png
#
#
# import urllib.request
# # url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# # urllib.request.urlretrieve(url, "test.png")
# # print("저장되었습니다")
#
# import ssl
#
# #context = ssl._create_unverified_context() #mac
#
# # url="https://www.multicampus.com/img/saas/main/logo/CUS0001/pc_main.png"
# # mem=urllib.request.urlopen(url).read()
# # #mem=urllib.request.urlopen(url, context=context).read() #mac
# #
# # with open("test2.png", "wb") as f:
# #     f.write(mem)
# #     print("저장되었습니다")
#
#
# # http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp
# #
# # 웹에서 사용하는 언어
# # -서버와 클라이언트 간에 데이터를 주고 받을 때 사용하는 언어(HTML)
# # 클라이언트(페이지 요청, 웹브라우저에 www.naver.com) -> 웹서버 -> 메인페이지 제공(index.html)->
# #
# # HTML: HyperText Markup Language
# # XML : Extensible Markup Language
#
# # jsp, asp, php 등 : 동적 페이지
# # 구조화된 문서(xml):정적 페이지
# # 비구조화된 문서(html):정적 페이지
# #
# # 클라이언트(날씨 클릭)-> 웹서버(날씨 페이지(동적,jsp) 생성) -> 생성된 페이지를 html문서로 만들어 제공
# # -> 웹브라우저 해석 -> 결과를 화면에 출력
# #
# # 출력 : 오늘의 날씨는 맑습니다. 기온은 섭씨 영상 2도입니다
# #
# # 정적페이지
#
# # 검색어 : 노래 제목, 멤버들, ...
# #
# # 비구조화된 문서 : 웹페이지 내용에 대해 기계가 해석하지 못하는 문서->검색어를 기반으로 검색
# # EX) BTS가 서울 강남구에서 공연을 했습니다.
# #
# # 구조화된 문서 : 웹페이지 내용에 대해 기계가 해석 가능한 문서->검색어의 의미를 기반으로 검색
# # =>검색 폭 넓음, 검색 결과에 대한 정확도 높음
# # <가수>
# #     <그룹명>BTS</그룹명>
# #     <도시이름>서울</도시명>
# #     <구이름>강남구</구이름>
# #     <멤버이름>.....</멤버이름>
# # </가수>
#
# import urllib.parse as parse
# import urllib.request as request
# addr="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
# values={'stdId':'109'}
#
# params=parse.urlencode(values)
# url=addr+"?"+params
# print(url)
#
# data=request.urlopen(url).read()
# data=data.decode('utf-8')
# print(data)

#제주시의 1월16일 자정 온도

#웹스크래핑 :BeautifulSoup패키지




from bs4 import BeautifulSoup

# html="""
# <html>
# <body>
# <h1>스크레핑</h1>
# <p>웹 페이지 분석</p>
# <p>원하는 부분 추출</p>
# </body>
# </html>
# """
# soup=BeautifulSoup(html, "html.parser")
# #클래스
# print(soup.html.body.h1.string)
# p1=soup.html.body.p
# # p2=p1.next_sibling #줄바꿈 문자
# # print(p2.next_sibling.string)
# p2=p1.next_sibling.next_sibling.string
# print(p2)
# #print(soup.html.body.p.string)
# #붕어빵봉투=붕어빵기계(크림, 10센티)
#

html2="""
<html>
<body>
<h1 id='title'>스크레핑</h1>
<p id='body'>웹 페이지 분석</p>
<p>원하는 부분 추출</p>
</body>
</html>
"""

soup=BeautifulSoup(html2, "html.parser")
#print(soup.html.body.h1.string)
print(soup.find(id='title').string)
print(soup.find(id='body').string)

#raw text
html3="""
<html><body>
<ul>
<li><a href="http://www.naver.com">naver</a></li>
<li><a href="http://www.daum.net">daum</a></li>
</ul>
</body></html>
"""
soup=BeautifulSoup(html3, "html.parser")
print(soup) #문자열 -> html파서로 분석할 수 있는 객체로 변환
print(html3) #문자열을 저장하고 있는 변수
#<태그명 속성명=속성값 속성명=속성값...>

links=soup.find_all("a")
#print(html3.find_all("a"))

for i in links:
    href=i.attrs['href']
    na=i.string
    print(na, "-->", href)


html4="""
<p><a href="aaa.html" name="kkk">aaa page</a></p>
"""

soup=BeautifulSoup(html4, "html.parser")
print(soup.p.a.string)
print(soup.a.string)
print(soup.a.attrs)
mydict=soup.a.attrs

print('href' in mydict)
# if 'href' in mydict:
#     ..
# else:
#     ..

#퀴즈1

dic=soup.a.attrs
print(dic)
print(dic.values())
print(list(dic.values())[1])

#soup.a.attrs.get('name')

import urllib.request as req

url="http://www.weather.go.kr/weather/forecast/mid-term-rss3.jsp"
res=req.urlopen(url)
#print(res) #res는 페이지 내용이 담겨있는 포장지(봉투)
soup=BeautifulSoup(res, "html.parser")
#print(soup)

# print("문서 제목:",soup.title.string)
# print(soup.find("title").string)
# print(soup.find_all("title")[0].string)

#모든 wf 태그의 내용을 출력

#print(soup.find('wf').string)
#print(len(soup.find_all("wf"))) #534개


# 정상응답 => 200:ok
# 문서를 찾지 못한경우 => 40x
# 서버 자체 오류 => 50x



from bs4 import BeautifulSoup

html4 = """
<html><body>
<div id="lang">
    <h1>programming</h1>
    <ul class="items">
        <li>python</li>
        <li>java</li>
        <li>cpp</li>
    </ul>
</div>
</body></html>
"""
soup=BeautifulSoup(html4, "html.parser")
#print(soup.select("div"))

#여러개를 추출
#print(soup.select("div#lang > h1")[0].string)

#한 개를 추출
#print(soup.select_one("div#lang > h1").string)

mylist=soup.select("div#lang > ul.items > li")
#print(soup.select_one("div#lang > ul.items > li"))
for i in mylist:
    print(i.string)




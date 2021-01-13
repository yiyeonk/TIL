# # [^0-9] : [not 0-9]
# # \d : 숫자[0-9]와 같음
# # \D : not \d의 의미 == [^0-9]
# # \s : 공백, 탭, 엔터 문자 등
# # \S : not \s
# # \w : 문자+숫자를 의미, [a-zA-Z0-9_]와 같음
# # \W : not 문자 +숫자를 의미, [^a-zA-Z0-9_]와 같음
#
# # ? or . : 문자가 1개만 있는ㄴ지 판단
# # ?는 문자가 0개 또는 1개인지 판단 = {0,1} = 최소 0개 이상 최대 1개 = 있어도 되고 없어도 됨
# # .은 문자가 1개인지 판단
#
# # ab?c => a뒤에 있어도 없어도 됨 + c는 반드시 나와야함
#
# import re
# print(re.match('h?','h'))  # h 다음에 문자가 1개또는 0개 나오면 됨
# print(re.match('h?','he'))
# print(re.match('ab?c','abc'))
# print(re.match('ab?c','ac'))
# print(re.match('h.','hello'))
# #
# #
# print(re.match('a.b','abb'))
# print(re.match('a[.]b','abb'))
# print(re.match('[123]','32321'))  # []안에 있는 문자 중 1개가 매치되면 출력
#
# print(re.match('a.b','abbbbb'))  # .은 모든 문자 1개
# print(re.match('a[.]b','a.b'))  # [.]은 특수문자(마침표)
# print(re.match('a.b','abb'))
# print(re.match('a.b','abb'))
#
# # 빅데이터(파일)
#
#
# fn = "abc.txt"
# res = re.match("[a-zA-Z0-9]+[.]+[a-zA-z]+", fn)
# if res:
#     print("정상적인 파일명")
# else:
#     print("잘못된 파일명")
#
# print(re.match("do*g", "dg"))  # o가 0번 이상 반복
# print(re.match("do*g", "dog")) # o가 0번 이상 반복
# print(re.match("do*g", "dooooog")) # o가 0번 이상 반복
# print(re.match("do*g", "doooookg")) # None
#
# print(re.match("do+g", "dg"))  # None
# print(re.match("do+g", "dog")) # o가 0번 이상 반복
# print(re.match("do+g", "dooooog")) # o가 0번 이상 반복
# print(re.match("do+g", "doooookg")) # None
#
# # 반복 : {최소, 최대} : 최소~최대 횟수 반복
# # {최소,} : 최소 횟수 이상 반복
# # {,최대} : 최대 횟수 이하 반복
#
# print(re.match("do{2}g","dog"))  # o문자가 반드시 2번 반복
# print(re.match("do{2}g","doog"))  # o문자가 반드시 2번 반복
# print(re.match("do{2}g","doooooog"))  # o문자가 너무 많이 반복 -> None
#
# print(re.match("do{2,5}g","dog"))  # None : o문자가 반드시 2번 이상 5번 이하 반복
# print(re.match("do{2,5}g","doog"))  # o문자가 반드시 2번 반복
# print(re.match("do{2,5}g","doooooog"))  # None : o문자가 5번 초과


# 휴대폰 전화번호
# 3자리-4자리-4자리(모두 숫자)
# 010-1234-5678  # 정상 전화번호
# 010-1234-567  # 비정상 전화번호
# abc-1234-5678 # 비정상 전화번호
# 01c-1234-5678 # 비정상 전화번호
import re
#
# num = "010-1234-567"
# res = re.match("[0-9]{3}[-][0-9]{4}[-][0-9]{4}",num)
# if res:
#     print("올바른 번호")
# else:
#     print("잘못된 번호")


# match, search, \
# findall : 정규식과 매치되는 모든 문자열을 리스트로 리턴
# finditer : 정규식과 매치되는 모든 문자열을 반복가능한 객체 형태로 리턴

# print(re.match("[a-z]+", "python"))
#
# pat = re.compile("[a-z]+")  # 정의한 패턴을 pat에 저장
# res = pat.match("python")
# print(res)
#
# print("="*50)
# print(re.match("[a-z]+","python"))
# print(re.search("[a-z]+","python"))
#
# print(re.match("[a-z]+","7python"))
# print(re.search("[a-z]+","7python8java9cpp"))
#
# # search 결과는 1개의 매치 객체가 리턴
# print(re.findall("[a-z]+", "7python8java9cpp"))
#
# pat = re.compile("[a-z]+")  # 정의한 패턴을 pat에 저장
# res = pat.findall("7python8java9cpp") # 패턴객체(pat)가 가지고 있는 match함수를 이용하여
# print(res)


# res=re.finditer("[a-z]+", "7python8java9cpp")  # 반복 가능한 객체로 리턴
# for i in res:
#     print(i)
#     print(i.start())  # 매치된 대상의 시작 위치 : 13
#     print(i.end())  # 매치 끝 위치 : 7
#     print(i.group())  # 매치된 문자열
#     print(i.span()) # 매치 시작, 끝 위치
#
# # . : 점(.) 메타문자는 모든 문자 1개와 매치. 예외(줄바꿈 문자:\n)
# print(re.match("a.b","a0b"))
# print(re.match("a.b","a\nb")) # None
#
# pat = re.compile("a.b", re.DOTALL)  # \n문자도 포함
# print(pat.match("a\nb"))
#
# pat = re.compile("[a-z]")
# print(pat.match("python"))
# print(pat.match("Python"))
# print(pat.match("PYTHON"))
#
#
# pat = re.compile("[a-z]",re.I)  # ignorecase : 대소문자 무시
# print(pat.match("python"))
# print(pat.match("Python"))
# print(pat.match("PYTHON"))

import re
# print(re.search("\section", "kldjdifl akjdoifekj ds ection klskds"))
# # 패턴 : \s는 엔터, 공백, 탭 등 문자
#
# print(re.search("\\\section", "kldjdifl akjdoifekj ds \ection klskds"))
# print(re.search("\\\section", "kldjdifl akjdoifekj ds \ection klskds"))
# # \ 문자가 문자열 자체임을 나타내기 위해서 역슬래쉬 \\\
#
# print(re.search(r"\\section", "kldjdifl akjdoifekj ds \ection klskds"))
# # r"\\section" => \section
#
# print(re.match("ab[0-9]?c","abc"))
# print(re.match("ab[0-9]?c","ab9c"))
# print(re.match("ab.c","ab9c"))

# print(re.match("h{3}","hhhiii"))
# # hi가 3번 반복 => 그룹화 "(문자/숫자)"
# print(re.match("(hi){3}","hihihihelloworld"))
# print(re.match("(hi){3,5}","hihihihelloworld"))
#
# print(re.match("[0-9]{2,3}-[0-9]{3,4}-[0-9]{4}","02-1234-5678"))
#
# print(re.match("[ㄱ-ㅎ]+", "ㅋㅋㅋㅋ캬캬캬캬ㅋㅋㅋㅎㅎㅎㅎ"))
# print(re.match("[^ㄱ-ㅎ가-힣]+", "ㅋㅋㅋㅋ캬캬캬캬ㅋㅋㅋㅎㅎㅎㅎ"))
# print(re.findall("[ㄱ-ㅎ가-힣]","문자열")) # 한글만 모두 추출
# print(re.findall("[^ㄱ-ㅎ가-힣]","문자열")) # 한글을 제외한 모든 문자 추출

news="""
(서울=연합뉴스) 신선미 기자 = 국내 신종 코로나바이러스 감염증(코로나19) '3차 대유행'이 완만한 감소세로 접어든 가운데 이번 주 신규 확진자 발생 추이가 주목된다.

신규 확진자 감소세 지속이냐 재확산이냐의 흐름을 가늠해 볼 수 있기 때문이다.

지난달 말까지만 해도 연일 1천명 안팎으로 발생하던 신규 확진자는 새해 들어 600명대로 줄었다가 11일 400명대 중반까지 더 떨어진 뒤 12일에는 500명대로 소폭 증가한 상태다.

큰 틀의 통계만 보면 확실한 감소 내지 안정국면으로 접어드는 것 아니냐는 관측이 나온다.

하지만 신규 확진자가 400명∼500명대까지 낮아진 데는 주말과 휴일 검사건수 감소 영향도 있어 아직 상황을 낙관하기에는 이르다는 게 감염병 전문가들의 공통된 의견이다.

방역당국 역시 긴장의 끈을 풀기에는 위험 요인이 너무 많다며 국민 개개인의 지속적인 방역 협조를 당부하고 있다.
"""

# print(re.findall("[ㄱ-ㅎ가-힣]+",news))
#
# print(re.findall("[ㄱ-ㅎ가-힣]+[0-9]+", news)) # 한글+숫자로 구성된 문자열 출력
# print(re.findall("[0-9]+[ㄱ-ㅎ가-힣]+", news))
# print(re.findall("[0-9]+[명|천]+", news))  # 숫자+명 or 천으로 조합된 문자열 출력
#
# print(re.match("[0-9]+","hello119"))
# print(re.search("[0-9]+$","hello119"))
#
# print(re.search("[*]","3*5"))   #곱하기 문자가 있는지 판단
# print(re.search("[*]+","3**5"))   # 별이 두개 출력
# print(re.search("\*","3*5"))   # 특수문자 앞에 역슬래쉬(\)를 붙여주면 됨
# print(re.search("\*+","3**5"))
#
# print(re.search("\$\([a-z]+\)","$(document)"))
# print(re.search("[$()a-z]+","$(document)"))

# # "abcabcabc ok" 문자열 있을 때 abc가 있는지 조사
# print(re.search("(abc)+","abcabcabc ok"))
#
# print(re.search("\w+\s+\d+[-]\d+", "kim 010-1234-5678"))
# # 이름 + " " + 전화번호
# res = re.search("\w+\s+\d+[-]\d+", "kim 010-1234-5678")
# print(res.group())
# # print(res.group().split()[0])

# # 그룹핑
#
res = re.search("(\w+)\s+(\d+[-]\d+[-]\d+)", "kim 010-1234-5678")
print(res)
print(res.group(0))  # 전체가 출력

# print(res.group(1)) # 소괄호 하나가 그룹
# print(res.group(2))  # 두번째 그룹은 없으므로 에러
#
# # 그룹 이름을 부여
# res = re.search("(?P<name>\w+)\s+(?P<num>\d+[-]\d+[-]\d+)", "kim 010-1234-5678")
# # 작성형식: (?P<그룹명>...)
#
# print(res.group('name'))
# print(res.group('num'))
#
# print(re.findall("hello|hi", "hello how are you bye hi hi"))
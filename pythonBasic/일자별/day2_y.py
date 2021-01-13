# # 문자열
# # print(s[::3])  # offset: 몇 칸을 건너뛸 것인지, 양수(좌->우), 음수(우->좌)
#
# tel = "010-1234-5678"
# # replace: 문자(열) 치환
# print(tel.replace("-",""))  # ctrl + space bar
#
# print(1,2,3, sep="&")
#
# # bool 연산자(T/F)
# print(3>2)  # 비교 연산자
# print(3!=2) # != not equal
#
# a = 1; b = 1
# print(a==b) # == 는 두 값이 같은지를 비교
# print(a is b) # is 는 두 객체(주소가 동일)를 비교
#
# # 참고
# print(1 == 1.0)  # 정수와 실수라는 점에서 차이, 값은 같음. => True
# print(1 is 1.0)  # is는 두 객체가 같은지 비교. 1은 정수객체, 1.0은 실수객체 => False
#
# # 논리 연산자 : and(모두 참 -> 참), or(하나 이상 참 -> 참), not(참->거짓, 거짓->참)
# print(True and False)
#
# # 0:False, 1: True, 0이 아닌 모든 수가 True
# print(bool(1))
# print(bool('test')) # 문자열 True
# print(bool(''))  # 빈 문자열 False
#
# print("%10s" % "hi")  # %10s 10칸 공란
# print("hello%10s" % "hi")
# print("%-10shello" % "hi")
# print("%.4f"%3.141592)  # 소수 이하 5째 자리에서 반올림 -> 4째 자리까지 표혐
# print("%10.4f" % 3.141592) # 10자리를 확보한 다음 출력(우측 맞춤)

# num = 3
# day = "three"
#
# print("I eat {0} apples".format(num)) # 포맷팅
#
# print("I ate {0} eggs. so I was sick for {1} days.".format(num, day))
# print("I ate {num} eggs. so I was sick for {day} days.".format(num=5, day=3))
# print("I ate {0} eggs. so I was sick for {day} days.".format(5, day=3))
#
# print("".format("hi"))
# print("{0:<10}".format("hi"))  # 10자리 확보 후 왼쪽 정렬
# print("{0:>10}".format("hi"))  # 10자리 확보 후 오른쪽 정렬
# print("{0:-^10}".format("hi"))  # 10자리 확보 후 가운데 정렬, 빈자리가 '-'로 채워짐
#
# print("{0:4f}".format(3.141592))

# a = "hello"
# print(a.count('l'))  # 해당 문자의 개수
# # 위치 확인
# print(a.find('l')) # 위치:2 / 여러개 있는 경우에는 맨 처음 나온 위치가 출력
# print(a.find('x'))  # -1: 문자가 없는 경우
# print(a.index('l'))
# print(a.index('x')) # 에러발생: 문자가 없는 경우
#
# # 문자열 삽입
# print(",".join("abcd"))
# print(",".join(['a','b','c','d']))
# # 리스트에 저장되어 있는 각가의 문자들이 컴마(,)와 결합하여 하나의 문자열이 됨

# a = "hi"
# print(a.upper())  # 대문자 변환
# a = a.upper()
# a.lower()  # 소문자 변환
#
# # 공백제거
# n1 = "   대한민국"
# n2 = "대한민국   "
# n3 = "   대한민국  "
# print(n1.lstrip())  # 왼쪽
# print(n1.rstrip())  # 오른쪽
# print(n1.strip())  # 양쪽

# s = "Life is too short"
# # replace : 문자(열) 치환
# print(s.replace("Life", "Your leg"))
# print(s.split())  # 공백문자로 분리 => list 형태로 출력
# s = "Life$is$too$short"
# print(s.split("s"))  # method(=function)

# 문자 바꾸기
# str.maketrans('바꿀문자', '새문자') 작성하여 변환테이블 생성
# t = str.maketrans('aeiou', '12345')
# print('apple'.translate(t)) # apple 문자열을 t 변환테이블을 참조하여 변환하세요

# 정규표현식 : 문자열 전처리
str = ", python,."
# print(str.lstrip(","))
# print(str.lstrip(", ")) # 큰따옴표 안에 제거대상 문자를 나열
# l(r)strip("삭제대상 문자들")

# import string
# print(str.strip(string.punctuation+" "))
# # punctuation(구두점) : !"#$%&'()*+-,./:;<=>?@[\]^_`{|}~
#
# print('python'.ljust(10))  # 10자리 확보 후 좌측 정렬
# print('python'.rjust(10))  # 10자리 확보 후 우측 정렬
# print('python'.center(10))  # 10자리 확보 후 우측 정렬
#
# # 매서드(함수), 체이닝(chaining) -> 코드가 간결해짐
#
# print('python'.rjust(10))
# s = 'python'.rjust(10)
# print(s.upper())
#
# print('python'.rjust(10).upper())
#
# # 패딩(padding: 특정 값으로 빈자리를 채우는 것)
# print("hello".zfill(10))  # zero fill
#
# # 함수: 우리 프로그램에 기본적으로 적재가 되는 함수(ex. print) = 내장함수
# # 별도로 적재를 해야 하는 함수(ex. import 함수) = 외장함수
# import random
# print(random.random())  # 난수 발생, 별도로 적재를 해야 하는 함수
# #     모듈명.함수명()
# print(random.randint(1,10))

# print("apple pineapple".find('p'))
# print("apple pineapple".find('pp'))
# print("apple pineapple".rfind('p'))

# list : 다양한 자료형(정수, 실수, 불린, 문자, 요소 등을 저장할 수 있음)
# x = [10, 20, 30]
# a = [1,2,['life','is', ['too','short']]] # a 변수에는 요소가 몇 개? 3
# print(a[2]) # ['life','is']
# print(a[2][1]) # 'is'
# print(a[2][2][0])
#
# b = [] # 빈 리스트 생성
# b = list() # 빈 리스트 생성
#
# b = [1,2,3]
# print(b[0]+b[2])
#
# a = [1,2,['life','is', ['too','short']]]
# print(a[-1][2][0])
# print(a[-1][-1][-2])

# # list sclicing
# x = [10,20,30,40,50]
# print(x[1:4])
# print(x[::-1])
#
# s = "abcdefg"
# print(s[2:5])

# a = [1,2,3,['x','y','z'],4,5]
# print(a[-3][:2])

# print(list(range(5)))  # 0~5-1까지 숫자를 생성
# print(list(range(10,0,1)))

# list 연산
# a = [1,2]
# b = [3,4]
# print(a+b)
# print("ab"+"cd")
#
# print(a*3) # [1,2] 리스트가 3번 반복
# print("ab"*3)
# print(len(a)) # a 길이
# # print(a[0]+"hi") # error!  정수와 문자열은 더할 수 없으므로
# print(type(a[0]))

# a = [1, 2]
# print(str(a[0])+"hi")  # 숫자 1 -> 문자열"1"
# str 함수 : 정수, 실수를 문자열로 변환

# # 리스트 요소 값 삭제
# del a[2]
# print(a)
#
# a = list(range(1,10))
# print(a)
# del a[:5]  # 0~4번 index까지 삭제
# print(a)
#
# a = [1,2,3]
# # print(a+4)
# print(a+[4])
# # a.append([5,6,7])  # 리스트가 추가
# a. extend([5,6,7])   # 확장
# print(a)
#
# b = [1,2,3]
# b += [4,5]   # 확장의 방법
# print(b)

# # 정렬 : 정해진 순서(내림/오름차순)로 데이터를 나열
# a = [3,7,5,1]
# a.sort()  # a에 저장된 자료를 정렬(오름차순)하고 결과를 a에 저장
# a.reverse()   # 내림차순 정렬(오름차순 정렬 후)
# print(a)

# # 리스트의 특정 위치에 데이터 추가 : insert
# a = [7,8,9]
# # 1과 2사이에 4추가
# a.insert(1, 4)
# print(a)
# 
# # list의 요소를 제거 : del, remove, pop
# # del : 특정 위치에 저장된 값을 제거
# a = [10,20,30]
# del a[1]
# print(a)
# 
# # remove : 특정 값을 제거
# a = [10,20,30,10,20,30]
# a.remove(30) # 첫번째 '30'만 제거
# a.remove(30) # 두번째 '30' 제거
# print(a)

# pop
a = [10,20,30]
a.pop()  # 가장 마지막 위치에 있는 데이터를 제거
print(a)

# overflow

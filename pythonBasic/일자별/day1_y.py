# # 파이썬
# # 매우 인간적인 언어
# # 프로그래밍(언어:파이썬,...)->프로그램(application, app(앱))
# # 프로그래밍?우리가 생각하는 것을 컴퓨터에 지시하는 행위
# # 1001 000100001 (2진수 X) -> print("hi")
#
# print("hi")
#
# # alt + f10, ctrl+shift+f10, shift+f10
# # 기본적으로 프로그램 실행시 : ctrl+shift+f10
# # 리스트:[], 튜플:(), 딕셔너리, 셋:{}
# if 4 in [1,2,3,4]: print("4가 있어요")
#
# languages = ['python', 'perl', 'c', 'java']
# # 변수 = 데이터 => 데이터를 변수에 저장해라
#
# for lang in languages:
#     if lang in ['python', 'perl']:
#         print("%6s need interpreter" % lang)
#     elif lang in ['c', 'java']:
#         print("%6s need compiler" % lang)
#     else:
#         print("should not reach here")
#
# # python으로 만드는 것 : 유틸리티, gui, web, DB, 데이터분석(파이썬에 추가적으로 패키지를 설치=pandas), IOT
# # import pandas as pd
#
# print("hello, world"); print('bye')
#
# a = 1 # assign(할당, 왼쪽 <- 오른쪽)
# a = 1+2
#
# # 파이썬에서는 들여쓰기가 중요
#
# if a==10:
#     print('10')
#     print("ten")
# print("코드블록 밖")
#
# # 코드블록 : 들여쓰기가 동일한 코드 집합
# # 파이썬은 수치연산에 강력함
# print(5/3)
# print(5//3)  # 몫
# print(6//3.0)
# print(7 % 4) # 나머지
# print(2 ** 3) # 거듭제곱
# print(2 ** 10000)
#
# print(int(3.3))
# print(int(5/2))
# print('10')  # 문자, 일영 이라고 읽음
# print(int('10')+1)
#
# print(type(10))
# print(type('123'))
#
# print(divmod(9, 4)) # 몫과 나머지를 동시에 구함
# res = divmod(9, 4) # 튜플 1개, 요소 2개(몫, 나머지)
# print("결과:", res)
# print("1번째 요소: ", res[0]) # res 튜플에 저장된 1번째 요소값을 출력
# # 튜플(리스트)에서 데이터의 위치는 0번부터 시작~
#
# res1, res2 = divmod(9, 4)
# print("1번째 요소: ", res1)
# print("2번째 요소: ", res2)
#
# # 0~9 / 0~1 / 0~7 / 0~9abcdef
# # a+1 -> b+2 -> d+2 -> f+1 -> 10... (자리올림됨)
# print(11)  # 11, 10진수
# print(0b11)  # 3, 2 진수 11 -> 10 진수로 변환되어 출력 -> 3
# print(0o10) # 8, 8진수
# print(0o17) # 15, 8진수
#
# print(5)
# print(float(5))
# print("Kim's computer")
# print("안\t\t\t녕!\n반가워요\n잘있어요") # \n : new line
# print("naver","kakao","samsung",sep = "$")
# print("안녕", end=" "); print("하세요")
# print((1+2)*3)
#
# a = 1
# b = 2
# c = 3
# a, b, c = 1, 2, 3
# a = b = c = d = 1
# print(a,b,c,d)
#
# x, y = 1, 2
# a = y
# y = x
# x = a
# print(x, y) # 2, 1
# x, y = 1, 2
# x, y = y, x
# print(x, y)
#
# a = 1 # 메모리에 a라는 공간을 만들고, 1을 저장해라
# print(a)
#
# # 메모리에 있는 변수를 제거
# del a
# print(a)
#
# # 변수만 만들고 값을 저장하고 싶지 않은 경우
# b = None
# print(b)

# x = 10
# x += 10  # x = x+10
# print(x)

# x = input("출력하고 싶은 값을 입력하고 엔터치세요: ")  # 입력을 받은 뒤 엔터 키를 누르면 다음 문장으로 이동
# print("당신이 입력한 값은: ", x)

# x = input("첫 번째 수 입력: ")
# y = input("두 번째 수 입력: ")
# print("덧셈 결과는", x+y)
# # input 함수로 입력받은 모든 데이터는 '문자'로 간주
#
# x = int(input("첫 번째 수 입m력: "))
# y = int(input("두 번째 수 입력: "))
# print("덧셈 결과는", x+y)

# a, b=input("두 수를 입력하세요:").split()  # 3 2 => 공백으로 split => 3은 a, 2는 b에 전달
# print(a)
# print(b)

# print("안 녕 하세 요".split())

# # Quiz
# # 숫자 두 개 입력: 1 2 (엔터) => 3
#
# x, y = input("숫자 두 개 입력").split()
# print(int(x)+int(y))

# # mapping : 사상 x -> f -> y
# # 함수출력 = map(함수, 함수입력)
# x1, x2 = map(int, input("숫자 두 개 입력: ").split())  #['1','2'] -> int함수 -> [1,2]
# print(x1+x2)

# 입력값을 컴마로 구분
# x1, x2 = map(int, input("숫자 두 개 입력: ").split(","))
# print(x1+x2)

# # 문자 데이터 입력
# x = 'hello'
# x = """인생은 짧다, 그래서 파이썬이 필요하다."""
# x = '''인생은 짧다,
# 그래서 파이썬이 필요하다.'''
# print(x)
#
# a = "python"
# print(a*3)  # a변수에 저장된 값을 3번 반복
# print("="*50)
# print("일기장")
# print("="*50)

# 인덱싱 : 변수에 저장된 문자열에 대해 위치를 지정하여 참조하는 행위

# x = "life is too short"
# print(len(x))  # 공백문자 포함 문자열 길이
# print(x[5:7])  # 위치(인덱스)는 0부터 시작, 범위 지정하여 슬라이싱[시작위치:끝위치+1]
# print(x[-3]) # '-'기호는 뒤에서부터 참조
# print(x[-5:]) # 끝위치를 지정하지 않으면, 문자열의 마지막까지 참조
# print(x[:4]) # 맨 앞에서부터 [3] 인덱스까지 추출
# print(x[:]) # 전체
# print(x[8:-3])  # '-3'위치는 포함 안됨

# x = "pithon"
# # x[1] = "y" # 에러 : 문자열의 요소값은 변경이 안됨
# x = x[0:1]+"y"+x[2:]
# print(x)
#
# x = "ten"
# d = 3
# per = 30
# print("I eat %s eggs. so I was sick for %d days. %d%%" % (x,d, per)) # 문자열 포매팅(변화가 있는 부분을 일정한 형식을 맞추기 위해)
# %d: decimal, 10진수
# %s: string, 문자
# %f: float, 실수

# 과제_day1

# Q1.
letters = 'python'
print(letters[0], letters[2])

# Q2.
cn = "24가 2210"
print(cn[-4:])

# Q3.
s = "파이썬파이썬파이썬"
print(s[0],s[3],s[6])

# Q4.
num_str = "720"
print(int(num_str))

# Q5.
data = "15.79"
print(float(data))

# Q6.
price = 48584
month = 36
total = price*month

print("총 금액은", total, end=""); print("원 입니다.")
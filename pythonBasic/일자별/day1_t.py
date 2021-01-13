# 파이썬?
# 매우 인간적인 언어
# 프로그래밍(언어:파이썬,...)->프로그램(application, app(앱))
# 프로그래밍?우리가 생각하는 것을 컴퓨터에 지시하는 행위
#
# 1001 000100001 (2진수 x) -> print("hi")

#블록 설정 -> ctrl + /  -> 블록 전체가 주석(참고문)으로 간주됨

# print("hi")
#
# if 5 in [1,2,3,4]: print("5가 있어요")


#alt+f10, ctrl+shift+f10, shift+f10

#기본적으로 프로그램 실행시 : ctrl+shift+f10

#리스트:[], 튜플:(), 딕셔너리,셋:{}

# languages = ['python', 'perl', 'c', 'java']
# #변수 = 데이터    => 데이터를 변수에 저장해라
#
# for lang in languages:
#     if lang in ['python', 'perl']:
#         print("%6s need interpreter" % lang)
#     elif lang in ['c', 'java']:
#         print("%6s need compiler" % lang)
#     else:
#         print("should not reach here")
#
# #유틸리티, gui, web, db, 데이터분석(파이썬에 추가적으로 패키지를 설치, 파이썬+pandas), iot
#
# #import pandas as pd
#
# print('hello, world');print('bye')
#
# a=1 # assign( 할당,  왼쪽<-오른쪽)
# a=1+2
#
# #파이썬에서는 들여쓰기가 중요
#
# #backspace key : 엔터키 위에 <-, tab
# if a==4:
#     print('4')
#     print('four')
# print("코드블록 밖")
# #코드블록 : 들여쓰기가 동일한 코드 집합
#
#
# print(5/3) #1.6666666
#
# print(5//3) #1몫
# print(6//3) #2
# print(6//3.0) #2.0
#
# print(7 % 4) #나머지
# print(2 ** 3) #거듭제곱
#
# print(2 ** 10000 * 3 ** 10000) #2의 10000승

# print(int(3.3))
# print(int(5/2))
# print('10') #일영   이라고 읽음
# print(int('10')+2)#문자열 일영 -> 숫자 10 변환 -> 더하기 2 => 12
#
# print(type(10))
# print(type('123'))
#
# print(divmod(9, 4)) #9를 4로 나눈 몫과 나머지 => (2, 1)   ==  (몫, 나머지)
# #    함수(인수1, 인수2)
#
# res=divmod(9, 4) #res=(2, 1)  튜플 1개, 요소 2개(몫, 나머지)
# print("결과:",res)
# print("1번째 요소 : ", res[0]) #res 튜플에 저장된 1번째 요소값을 출력
# print("2번째 요소 : ", res[1]) #res 튜플에 저장된 2번째 요소값을 출력
# #튜플(리스트)에서 데이터의 위치는 0번부터 시작~
# res1, res2=divmod(9, 4)
# print("1번째 요소 : ",res1)
# print("2번째 요소 : ", res2)
#
# # 0~9
# # 0~1
# # 0~7
# # 0~9abcdef
# #a+1 -> b +2 => d +2 => f +1 => 10 ...
# # print(11) #11, 10진수
# # print(0b11) #3, 2진수 11 -> 10진수 변환되어 출력 -> 3
# # print(0o17) #15, 8진수
# #
# #
# # print(5)
# # print(float(5))
# # print(float(1+2))
# # print(float('3.14')*2) #'3.14' -> 3.14 -> *2 -> 6.28
# # print(type(3.14))
# # #print(int('2'))
# #
# # # Kim's computer
# # print("Kim's computer")
# #
# # print('hello')
# # print("Kim's computer")
# #
# # print('he said. "how are you?"')
# #
# # #print("안녕! 반가워요 잘있어요")
# # # print("안녕!")
# # # print("반가워요")
# # # print("잘있어요")
# # print("안\t\t\t녕!\n반가워요\n\n잘있어요")  #\n : new line
# #
# # #naver$daum$samsung
# # print("naver", "kakao", "samsung") #공백으로 연결되어 출력
# # print("naver", "kakao", "samsung", sep="$")
# #
# # print("안녕");print("하세요")
# #
# # print("안녕")
# # print("하세요")
# #
# # print("안녕",end="^^")
# # print("하세요")
# #
# # print((1+2)*3)
# #
# # a=1
# # b=2
# # c=3
#
# #a,b,c=1,2,3
# a,b,c,d=1,2,3,4
# print(a,b,c,d)
#life is too short

# a=b=c=d=1
# print(a,b,c,d)
#
# x,y=1,2
# a=y
# y=x
# x=a
# print(x,y) #2 1

# x,y=1,2
# x,y=y,x
# print(x,y)
# a=1 #메모리에 a라는 공간을 만들고, 1을 저장해라
# print(a)

#메모리에 있는 변수를 제거
# del a
# print(a)

#변수만 만들고 값을 저장하고 싶지 않은 경우
# b=None  #사과바구니 자체가 없음
# print(b)
# b=''  #b라는 이름의 사과바구니에 사과가 1개도 없음
# #''는 None이 아님
# print(b)
#
# x=10
# x+=10 #   x=x+10
# print(x)
#
# x-=5 #x=x-5
# x*=5 #x=x*5
# x/=5
# x%=5

#다음, 네이버, 구글(바) 선생님-> 논문
#파파고 선생님, 유(튜브)선생님



# x=input("출력하고 싶은 값을 입력하고 엔터치세요? ") #입력을 받은 뒤 엔터 키를 누르면 다음 문장으로 이동
# print("당신이 입력한 값은 : ", x)

# x=input("첫 번째 수 입력 : ")
# y=input("두 번째 수 입력 : ")
# print("덧셈 결과는 ", x+y)
#input함수로 입력받은 모든 데이터는 '문자'로 간주

# x=1
# y=2
# print("덧셈 결과는 ", x+y)
#print('1'+'2')


# x=int(input("첫 번째 수 입력 : "))   # 1-> '1' -> int('1') ->1
# y=int(input("두 번째 수 입력 : "))
# print("덧셈 결과는 ", x+y)

# x=float(input("첫 번째 수 입력 : "))   # 1-> '1' -> int('1') ->1
# y=float(input("두 번째 수 입력 : "))
# print("덧셈 결과는 ", x+y)

# a,b,c=input("세 단어를 입력하세요:").split() #3 2 => 공백으로 split => 3은 a, 2는 b에 전달
# print(a)
# print(b)
# print(c)

#print("안 녕 하세 요".split())

# 숫자 두 개 입력 : 1 2 (엔터)
# 3
# x,y=input("숫자 두 개 입력 : ").split()
# print(int(x)+int(y))

#에러 발생 "1 2" -> int(1, 2)

# x,y=input("숫자 두 개 입력 : ").split()
# print(int(x)+int(y))

# x1, x2= map(int,  input("숫자 두 개 입력 : ").split())   #['1', '2'] -> int함수 -> [1, 2]
# #x1=1, x2=2가 저장됨
# print(x1+x2)
#mapping:사상  x -> f -> y

#함수출력=map(함수, 함수입력)
# x1,x2=map(int, ['3', '4'])
# print(x1+x2)

#입력값을 컴마로 구분
# x1, x2= map(int,  input("숫자 두 개 입력 : ").split(","))
# #"1,2"-> ['1','2'] -> [1,2] -> x1=1, x2=2
# print(x1+x2)

#x='hello'

#x="""인생은 짧다, 그래서 파이썬이 필요하다."""
#x='''인생은 짧다, 그래서 파이썬이 필요하다.'''

#x='인생은\n짧다\n그래서 파이썬이\n필요하다.'

# x="""
# 인생은
# 짧다
# 그래서 파이썬이
# 필요하다.
# """
# print(x)

# a="python"
# print(a*3) #a변수에 저장된 값을 3번 반복

# print("="*50)
# print("일기장")
# print("="*50)
#
# x="life is too short"
# print(x[8:-3]) #-3 위치는 포함 안함

#"20201229" => 년/월/일



#print(x[5]+x[6])
#print(x[5:7]) #범위 지정하여 슬라이싱 [시작위치: 끝위치+1]
# 5<= x <7

#short
# print(x[12:17])
# print(x[12:]) #끝위치를 지정하지 않으면, 문자열의 마지막까지 참조
# print(x[:4]) #맨 앞에서부터 4-1=3번 인덱스까지 추출
#
# print(x[:]) #전체
# print(x)


# print(len(x))
# print(x[1]) #위치(인덱스)는 0부터 시작
#
# #인덱싱 : 변수에 저장된 문자열에 대해 위치를 지정하여 참조하는 행위
# print(x[-3]) #-기호는 뒤에서부터 참조



# x="pithon"
# #print(x)
# #print(x[1])
# #x[1]="y" #에러 : 문자열의 요소값은 변경이 안됨
#
# x=x[0:1]+"y"+x[2:]
# print(x)


# x=2
# print("I eat %d eggs" % x) #문자열 포매팅, %d(decimal)

x="five"
d=2
per=30
print("I eat %s eggs. so I was sick for %d days. %d%%" % (x, d, per))
#%f:실수





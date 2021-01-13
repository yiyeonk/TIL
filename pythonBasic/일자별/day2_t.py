# letters='python'
# x,y=letters[0], letters[2]
# print(x,y)
#
# cn="24가 2210"
# print(cn[-4:])
#
# s="파이썬파이썬파이썬"
# #print(s[0],s[3],s[-3])
# print(s[::3])
# #offset:몇 칸을 건너뛸것인지, 양수(좌->우), 음수(우->좌)
# print(s[::-1])
#
# s='python'
# print(s[::-1])
#
# tel="010-1234-5678"
# #데이터수집->전처리->분석->...
# #replace함수 : 문자(열) 치환
# print(tel.replace("-",""))   #ctrl + space bar
#
# ##4.문자열 '720'를 정수형으로 변환해보세요 num_str = "720"
#
# num_str = "720"
#
# print(int(num_str))
#
# ##5.문자열 "15.79"를 실수(flot)타입으로 변환해보세요
#
# data = "15.79"
#
# print(float(data))
#
#
#
# a,b=48584,36
#
# print(a*b)
#
#
# print(1,2,3, sep="&")
#
# print(3>2)
#
# print(2==2)
#
# print(3==2)
#
# print(3!=2) #!= not equal
#
# print('python'=='Python')
#
# print('Python'=='Python')
#
# print()
#
# print(1==1)
#
#
# # #참고(몰라도 됨)
# # print(1==1.0) #정수와 실수라는 점에서 차이, 값은 같습니다. 그래서 == 비교하면 True
# # print(1 is 1.0) #is는 두 객체가 같은지 비교. 1은 정수객체, 1.0은 실수객체. 그래서 두 객체는 다르므로 False
# # # 홍길동나이==임꺽정나이 (나이를 비교)
# # # 홍길동 is 임꺽정 (사람을 비교)
#
# #논리 연산자 : and(모두 참 -> 참), or(하나 이상 참 -> 참), not(참->거짓,거짓->참)
#
# # print(True and False)
# # print(False or False)
# # print(not False)
#
#
# print(1==1 and 2!=1)
# print(3>1 or 1<2)
# print(not 1>2)
#
# #0:False, 1:True, 0이 아닌 모든 수가 True
# print(bool(1))
# print(bool(0))
# print(bool(0.5))
# print("="*50)
# print(bool('test')) # 문자열도  True
# print(bool('')) #빈문자열은 False
#
# print(bool(0 or 'test'))
# print(bool(0 and 'test'))
#
# # False or False => False
# # True and True => True
# #0:거짓, 1:참
#
# print("hi")
# print("          hi")
# print("hi          ")
#
# print("%10s" % "hi")
# print("hello%10s" % "hi")
#
# print("%-10shello" % "hi")
#
# print("%.4f" % 3.141592) #소수 이하 5째 자리에서 반올림 -> 4째 자리까지 표현
# print("%10.4f" % 3.141592) #10자리를 확보한 다음 출력(우측 맞춤)
#
#
# num=3
# s="two"
# day="three"
# print("I eat %d apples" % num)
# print("I eat %s apples" % s)
#
# print("I eat {0} apples".format(num))
# print("I eat {0} apples".format(s))
#
# print("I ate {0} eggs. so I was sick for {1} days.".format(num, day))
# print("I ate {1} eggs. so I was sick for {0} days.".format(num, day))
#
# print("I ate {num} eggs. so I was sick for {day} days.".format(num=5, day=3))
# print("I ate {0} eggs. so I was sick for {day} days.".format(5, day=3))
#
# print("{0}".format("hi"))
# print("{0:-<10}".format("hi")) #10자리 확보 후 왼쪽 정렬
# print("{0:->10}".format("hi")) #10자리 확보 후 오른쪽 정렬
# print("{0:-^10}".format("hi")) #10자리 확보 후 가운데 정렬
# print("{0:-^10}".format("hi")) #10자리 확보 후 가운데 정렬
#
# print("{0:.4f}".format(3.141592))
# print("{0:10.4f}".format(3.141592))
#
# a="hello"
# print(a.count('l'))
#
# #위치 확인
# print(a.find('l')) #위치:2, 여러개 있는 경우에는 맨 처음 나온 위치가 출력
# print(a.find('x')) #-1:문자가 없는 경우
#
# print(a.index('l'))
# print(a.index('x')) #에러발생 : 문자가 없는 경우
#
#

# #문자열 삽입
# print(",".join("abcd"))
# print(",".join(['a','b','c','d']))
# #리스트에 저장되어 있는 각각의 문자들이 컴마(,)와 결합하여 하나의 문자열("a,b,c,d")이 됨
# print("".join(['a','b','c','d']))#"abcd"
#
# #South Korea, south korea, SOUTH KOREA,...
#
# a="hi"
# print(a.upper())
# a=a.upper()
# print(a)
# a=a.lower()
# print(a)
#
# #"  대한민국" "대한민국  " "대한민국" ...
# n1="  대한민국"
# n2="대한민국  "
# n3="  대한민국  "
# print(n1.lstrip())
# print(n2.rstrip())
# print(n3.strip())
#
# s="Life is too short"
# #replace: 문자(열)을 치환
# print(s.replace("Life", "Your leg"))
# print(s.split()) #공백문자로 분리
#
# s="Life$is$too$short"
# print(s.split('s')) #method(=function)
# print('1,2,3'.split(','))

# t=str.maketrans('aeiou', '12345')
# print('apple'.translate(t))#apple 문자열을 t변환테이블을 참조하여 변환하세요
# #문자바꾸기
# #str.maketrans('바꿀문자', '새문자') 작성하여 변환테이블(t) 생성
#
# #정규표현식 : 문자열 전처리
#
# str=", python,."
# print(str.lstrip(","))
# print(str.lstrip(" "))
# print(str.lstrip(", ")) #큰따옴표 안에 제거대상 문자를 나열
# print(str.lstrip(" ,"))
# print(str.lstrip(" ,."))
#
# print(str.rstrip(" ,."))
# #[l|r]strip("삭제대상문자들")
# print(str.strip(" ,."))
#
# import string
# print(string.punctuation)
# # punctuation(구두점) :   !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
#
# print(str.strip(string.punctuation))
# print(str.strip(string.punctuation+" "))
#
# print('python'.ljust(10)) #10자리 확보 후 좌측 정렬
# print('python'.rjust(10)) #10자리 확보 후 우측 정렬
# print('python'.center(10)) #10자리 확보 후 가운데 정렬
#
# #메서드(함수) 체이닝(chaining) -> 코드가 간결해짐
#
# print('python'.rjust(10))
# s='python'.rjust(10)
# print(s.upper())
#
# print('python'.rjust(10).upper())
#
# #패딩(padding:특정 값으로 빈자리를 채우는 것)
#
# print("hello".zfill(10)) #zero fill
# print("345".zfill(10)) #zero fill
#
# print("apple pineapple".find('p'))
# print("apple pineapple".find('pp'))
#
# print("apple pineapple".rfind('p'))
# print("apple pineapple".rfind('pp'))
#
# print("apple pineapple".rindex('p'))
# print("apple pineapple".rindex('pp'))
#






#함수:우리 프로그램에 기본적으로 적재가 되는 함수(print),
#별도로 적재를 해야 하는 함수(import 한 다음에 사용)
# import random
#
# print("hi") #기본적으로 적재가 되는 함수(내장함수)
# print(random.random()) # 난수 발생, 별도로 적재를 해야 하는 함수(외장함수)
# #     모듈명.함수명()
# print(random.randint(1,10))


#
# #리스트?
# x=[10,20,30]
# print(x)
#
# #x리스트의 0번 index 요소값:10
# #print(x[3])
#
# y=['life', 'is', 'too', 'short']
# print(y[1])
#
# #리스트에 다양한 자료형(정수,실수,불린,문자,을 저장할 수 있음
# z=[1, 2, 'life', 'is', 'too', 'short', True, 3.14]
# print(z[2])
# print(z[7])
#
# #리스트에는 리스트를 요소값으로 할 수 있음
# a=[1,2,['life', 'is', ['too','short']]] #a 변수에는 요소가 몇 개?3(0번~2번)
# print(a[2]) #['life', 'is']
# print(a[2][1]) #'is'
#
# #'too' 출력
# a=[1,2,['life', 'is', ['too','short']]]
# print(a[2]) #['life', 'is', ['too', 'short']]
# print(a[2][2]) #['too', 'short']
# print(a[2][2][0])
#
#
# b=[] #빈 리스트 생성
# b=list() # 빈 리스트 생성
#
# b=[1,2,3]
# print(b[0]+b[2])
#
# #
# # 홍길동=[30, 1, ['코딩', '산책', '영화']]
# # 홍길동=[30, 1, ['코딩', '산책', ['코만도', '람보']]]
#
# a=[1,2,['life', 'is', ['too','short']]]
# print(a[2])
# print(a[-1])
#
# print(a[-1][2])
# print(a[-1][-1])
#
# print(a[-1][2][0])
# print(a[-1][-1][-2])
#
#
# #리스트 slicing
# x=[10,20,30,40,50]
# print(x[1:4])
# print(x[1:])
# print(x[:2])
# print(x[::-1])
# print(x[::-2])
#
# s="abcdefg"
# print(s[2:5])
#
# a=[1,2,3,['x','y','z'],4,5]
# #['x','y'] 출력
# print(a[3])
# print(a[-3])
#
# print(a[3][0:2])
# print(a[3][:2])
#
# print(list(range(5))) #0~5-1까지 숫자를 생성
#
# print(list(range(3,10)))
#
# print(list(range(3,10,2)))
#
# print(list(range(10,0,-1)))
#
# #리스트 연산(+,*)
# a=[1,2]
# b=[3,4]
# print(a+b)
# print("ab"+"cd")
#
# print(a*3) #[1,2] 리스트가 3번 반복
# print("ab"*3)
# print(len(a))
#
# #print(a[0]+"hi") #1hi? 에러 발생!!!(정수와 문자열은 더할 수 없으므로)
# print(type(a[0]))
# print(type("hi"))
# a=[1,2]
# print(str(a[0])+"hi") # 숫자 1 -> 문자열 "1"
#str 함수 : 정수나 실수를 문자열로 변환해주는 함수

#리스트 요소 값 변경
# a=[1,2,3]
# a[2]=4
# print(a)
#
# #리스트 요소 값 삭제
# del a[2]
# print(a)
#
# a=list(range(1,10))
# print(a)
# del a[:5] #0~4번 index까지  삭제
# print(a)
#
# a=[1,2,3]
# print(a)
# #print(a+4)
# print(a+[4])
# print(a)
# a.append(4) #a+[4]
# print(a)
#
# # a.append([5,6,7]) #리스트가 추가
# # print(a)
#
# a.extend([5,6,7]) #확장 a=a+[5,6,7]
# print(a)
#
# b=[1,2,3]
# # b.extend([4,5])
# # print(b)
# #b=b+[4,5]
# b+=[4,5]
# print(b)
#
# #정렬:정해진 순서(내림/오름차순(0->9, ㄱ->ㅎ, a->z)로 데이터를 나열
#
# a=[3,7,5,1]
# a.sort() #a에 저장된 자료를 정렬(오름)하고 결과를 a에 저장
# print(a)
#
# # 아래와 같이 출력하면 안됨
# # a=[3,7,5,1]
# # print(a.sort()) #None
#
# a=['b','k','d']
# a.sort()
# print(a)
#
# #내림차순
# a=[3,7,5,1]
# a.sort() #a에 저장된 자료를 정렬(오름)하고 결과를 a에 저장
# a.reverse()
# print(a)
#
# a=['b','k','d']
# a.sort()
# a.reverse()
# print(a)
#
# #리스트의 특정 위치에 데이터 추가 : insert
# a=[7,8,9]
# #7과8사이에 4추가
# a.insert(1,4)
# print(a)
#
# #리스트의 요소를 제거 : del, remove, pop
#
# #del:특정 위치에 저장된 값을 제거
# a=[10,20,30]
# del a[1]
# print(a)
#
# #remove : 특정 값을 제거
# a=[10,20,30,10,20,30]
# a.remove(30) #첫번째 30만 제거
# a.remove(30) #두번째 30 제거
# print(a)
#
# #pop:가장 마지막 위치에 있는 데이터를 제거
# a=[10,20,30]
# a.pop() #가장 마지막 위치에 있는 데이터를 제거
# print(a)
# a.pop()
# print(a)
# a.pop()
# print(a)

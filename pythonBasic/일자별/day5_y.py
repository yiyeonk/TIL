# # 함수 호출 구문
#
# def add(a, b):  # 사용자 함수
#     sum = a+b
#     print("add함수")
#     return sum
#
# res = add(1,2)  #parameter(인수)
#
# # 수행순서
# # 함수는 스스로 수행하지 않는다. 호출해야만 수행
# # 1) add(1,2) 호출
# # 2) add 함수 수행 -> sum 리턴
# # 3) sum이 res에 저장
#
# # 입력값이 없는 함수
# def say():
#     return()  # 함수가 수행한 결과를 함수로 호출해주는 경우로 돌려주는? 어떤값으로 되돌아 가라
# say()
# print(s)

# # 출력값이 없는 함수(return문이 없는 함수)
# def add(a,b):
#     print("두 수의 합은: ", a+b)
#     return   # 생략되어 있음
#
# add(3,4)
# res = add(3,4)
# print(res)   # None 출력값이 없기 때문에

# # 입력값/출력값 없는 함수
# def say():
#     print("안녕")
# say()
#
# # 매개변수의 초기값을 설정하여 함수 호출
# def add(a,b):
#     return a+b
# res = add(b=2,a=3)  # 매개변수 이름값을 지정: 파이썬에서 가능
# print(res)
#
# def add(a,b=3):  # b 초기값을 지정해줌/ 외부에서 전달되는 인수가 있으면 초기값이 지정되어 있더라도 외부에서 전달되는 인수 우선
#     print(b)
#     print(a)
#     return a+b
# res = add(2)  # 따라서 매개변수의 개수와 안맞아도 출력 가능
# print(res)

# # 함수로 전달되는 인수의 개수가 정해져 있지 않은 경우
# def add(*arg): # 매개변수명(arguments) 앞에 *을 붙이면 튜플로 인식
#     print(arg)
#     res = 0
#     for i in arg:
#         res += i
#     return res
# r = add(1,2,3)
# print(r)

# def mul(*arg):
#     res = 1
#     for i in arg:
#         res *= i
#     return res
#
# res = mul(1,2,3) # 인수가 가변적
# print(res)
#
# def addmul(op, *arg):
#     if op == "add":
#         res = 0
#         for i in arg:
#             res += i
#     elif op =="mul":
#         res = 1
#         for i in arg:
#             res *= i
#     return res
#
# # addmul(연산종류, 피연산자들)
# res = addmul("add", 1,2,3,4) # 인수가 가변적
# print(res)
# res = addmul("mul", 1,2,3,4,5) # 인수가 가변적
# print(res)

# def am(a,b):
#     return a+b, a*b   # 함수의 결과는 항상 1개. 튜플형식으로 출력(덧셈, 곱셈) 리턴
# # res = am(3,4)
# # r1 = res[0]
# # r2 = res[1]
# # print(r1)
#
# r1, r2 = am(3,4)
# print(r1); print(r2)

# def prn(a):
#     if a == "안녕":
#         return
#     print("반가워")
#
# prn("안녕")

# def say(name, age, man=True):  # 매개변수를 작성하세요, 기본값이 있는 것은 맨 뒤에 작성
#     print("내이름은", name)
#     print("나이는", age)
#     if man:
#         print("성별은 남")
#     else:
#         print("성별은 여")
# say("홍길동", 25)
# say("홍길동", 25, True)
# say("김말순", 26)
# say("김말순", 26, False)

# a = 1  # 함수 밖에 있는 a
# def mytest(a):  # 매개변수 a는 함수 안에서만 사용되는 변수임. 함수 밖에 있는 a가 아님
#     a += 1
#     return a
# b = mytest(10)
# print(b)
#
# def mytest2(z):
#     z += 1
#     print(z)
# mytest2(3)
# z = 5
# print(z)

print("-"*56) # 구분선

# # scope : 변수가 사용되는 범위
# # local variable : 함수안에서 사용되는 변수
# # global variable :
#
# a = 1
# def mytest3(a):
#     a += 1 # 함수 안에서 밖에 있는 변수를 증가하고 싶다면? 2가지 방법 존재(return, global)
# mytest3(a)
# print(a)
#
# # 1. return 사용
# a = 1
# def mytest3_1(a):
#     a += 1
#     return a
#
# a = mytest3_1(a)
# print(a)
#
# # 2. global 사용: 함수 안에서 함수 밖의 변수를 직접 사용
# a = 1
# def mytest3_2():
#     global a
#     a += 1
#
# mytest3_2()
# print(a)
#
# print("-"*56) # 구분선
#
# # lambda: def와 동일한 기능 수행하는 예약어
# # 함수 정의시 일반적으로는 def를 사용, 함수가 복잡하거나 def를 사용하지 못하는 곳에서는 람다 사용
#
# # 1. def를 이용한 일반적인 함수 정의
# def myadd(a,b):
#     return a+b
# res = myadd(2,3)
# print(res)
#
# # 2. 람다를 이용한 함수 정의
# myadd2 = lambda a,b: a+b
# # 함수명 = lambda 매개변수1, 매개변수2, .... : 매개변수를 이용한 계산식
# res = myadd2(2,3)
# print(res)
#
# def mymax(*arg):
#     print(max(arg))
# mymax(5,1,3,2)
#
# def mymax2(*arg):
#     num = 0
#     for i in arg:
#         if num == 0 or num > i:
#             num = i
#         print(i)
# mymax(2,7,9)   # 9
#
# def mymax_t(*arg):
#     # print(len(arg))
#     m = 0
#     for i in range(len(arg)):
#         if m < arg[i]:
#             m = arg[i]
#         return m
#
# print("최대값 : ", mymax_t(5,1,3,2))
# print("최대값 : ", mymax_t(2,7,9))

print("-"*56) # 구분선

# # 일반 함수 형식
# def pt(x):
#     return x+10
# print(pt(1))
#
# # 람다 함수 형식
# pt = lambda x:x+10
# print(pt(1)

# # 람다 함수 자체를 바로 호출
# # (lambda 매개변수들:수식)(인수들)
# print((lambda x:x+10)(1))
# print((lambda x,y:x+y)(1,2))
#
# # 람다 함수 내에서는 변수를 생성할 수 없음
# # print((lambda x:y=2; x+y)(1)) #문법오류
# y = 2
# print((lambda x:x+y)(1))

# # 함수의 인수 부분에 간단한 함수를 적용하고자 하는 경우
# def pt(x):
#     return x+10
# print(list(map(pt, [1,2,3]))) # map -> list

# def pt2(x):
#     # print(x)
#     return x+10
# print(list(map(pt2, [1,2,3])))
#
# print(list(map(lambda x:x+10, [1,2,3])))
#
# # 람다식으로 매개변수가 없는 함수 표현
# print((lambda : 1)())
#
# x = 10
# print((lambda : x)())

# Quiz
# 확장자가 c 이거나 h인 파일 이름을 모두 화면에 출력
# print((lambda : fl)())
fl = ['test.c', 'test2.h', 'sample.py','sample2.c']

# for i in fl:
#     if i[-1] == 'c' or i[-1] == 'h':
#         print(i)

for i in fl:
    res = i.split(".")
    if res[1]=="c" or res[1]=="h":
        print(i)


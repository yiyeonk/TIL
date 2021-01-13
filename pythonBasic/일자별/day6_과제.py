# # 1. 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
# def is_odd(*arg):
#     for i in arg:
#         if i % 2 == 0:
#             return "짝수"
#         else:
#             return "홀수"
# print(is_odd(78))
#
# # 2. 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
#
# with open("test.txt","w") as f:
#     f.write("Life is too short")

# # 3. 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.
# # Life is too short
# # you need java
#
# # list = ["Life is too short\n", "you need java"]
# with open("test.txt","w") as f:
#     f.write("Life is too short\nyou need java")
#
# with open("test.txt","r") as f:
#     s = f.read()
#     s = s.replace('java','python')
#
# # 4. "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
# def print_coin():
#     print("비트코인")
#
# # 5. 4에서 정의한 함수를 호출하라.
# print_coin()
#
# # 6. 4에서 정의한 print_coin 함수를 100번호출하라.
# for i in range(100):
#     print_coin()

# # 7. "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# def print_coins():
#     for i in range(100):
#         print("비트코인")
#
# print_coins()

# # 8. 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# def print_with_smile(string):
#     print(string+":D")
#
# print_with_smile("Hello")

# 9. 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라
# prince = [10,20,500,300,7000,10,20,500,1300,7000]
# def print_upper_price(lst):
#     for element in lst:
#         return element
#     print(element *1.3)
#
# print_upper_price([10,20,500,300,7000,10,20,500,1300,7000])

# #10. 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# def print_even(num):
#     for i in num:
#         if i % 2 == 0:
#             print(i)
#         else:
#             pass
#
# print_even([1,2,3,4])

# # 11. 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# def print_keys(dic):
#     for keys in dic.keys():
#         print(keys)
#
# print_keys({"이름":"홍길동", "나이":30})

# # 12. 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# def print_mxn(string, num):
#     hello_mxn = int(len(string)/num)
#     for i in range(hello_mxn+1):
#         print(string[i*num:i*num+num])
#
# print_mxn("hello",2)
#
# # 13. 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# def calc_monthly_salary(annual_salary):
#     month_salary = int(annual_salary/12)
#     print(month_salary)
#
# calc_monthly_salary(12000000)

# 14. 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
def make_url(str):
    print("www."+str+".com")

make_url("abc")
#
# 15. 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
def make_list(str):

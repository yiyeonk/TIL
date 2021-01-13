# # map (함수, 자료)
#
# # 퀴즈1 : 전달받은 값의 2배를 출력
# def twoTimes(n):
#     num = []
#     for i in n:
#         i = i * 2
#         num.append(i)
#     return num
#
# res = twoTimes([1,2,3])
# print(res) #[2,4,6]
#
# # 퀴즈 답 : 1-2
# return[2*i for i in n]
#
# # 퀴즈 답: 1-3
# res = list(map(lambda x:x*2, n))
# return res

# # 퀴즈 1. map 활용
# def twoTimes(n):
#     return n*2
#
# res = list(map(twoTimes, [1,2,3]))
# print(res) #[2,4,6]
#
# print(pow(3,2))  # 제곱
# print(3**2)   # 제곱
#
# print(round(3.141592, 4))
#
# print(list(zip([1,2],[3,4],[5,6],[7,8])))

# filter : 특정 조건으로 걸러진 요소들을 묶어서 리턴, map과의 차이점이라면, 함수의 결과가 참/거짓인자에
# 따라 요소를 포함할지를 결정

#
# # 짝수 리스트를 출력
# t = list(range(1,11))
# print(t)
#
# # 1. for
# def isEven(n):
#     return True if n % 2 ==0 else False  # n이 2로 나누어 떨어지면 T, 아니면 F 리턴
# res = []
# for v in t:
#     if isEven(v):
#         res.append(v)
# print(res)
#
# # 2. filter
# print(list(filter(isEven, t)))
#
# # 3. lambda
# print(list(filter(lambda x: x%2==0, t)))

# os 모듈 : 디렉토리, 파일의 경로 등 시스템 정보 확인/제어
# import os
# print(os.environ)
# print(os.getcwd())  # 현재 워킹디렉토리(작업경로) 확인
# os.mkdir("sample")  # 현재 작업 위치에 폴더 생성
# os.rmdir("sample")  # 폴더 삭제
# os.rename("sample", "test")  # 폴더명 변경
# os.renames("hello.txt","hi.txt")  # 파일명 변경

# import shutil   # 파이썬문서
# shutil.copy("hi.txt","hicopy.txt")  # 파일복사

# 특정 폴더 내에 있는 폴더 또는 파일 목록 등을 조사
import glob
print(glob.glob("C:/Users/yiyeon/TIL/pythonBasic/day*"))
print(glob.glob("C:/Users/yiyeon/TIL/pythonBasic/*.py"))

# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
# movie_rank.append("배트맨")
# print(movie_rank)
#
# #insert(인덱스, 추가하고자 하는 데이터)
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)
# del movie_rank[3]
# print(movie_rank)
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)
#
# num=[5,1,4,3,2]
# print(max(num))
# print(min(num))
# print(sum(num))
# print(len(num))
# avg=sum(num)/len(num)
# print(avg)
#
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# print(price[1:])
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(nums[1::2])
#
# nums = [1, 2, 3, 4, 5]
# print(nums[::-1])
#
# interest = ['삼성전자', 'LG전자', 'Naver']
# print(interest[0], interest[2])
#
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("/".join(interest))
# print("\n".join(interest))
#
# interest="/".join(interest)
# print(interest)
#
# print(interest.split("/"))
#
# data = [2, 4, 3, 1, 5, 10, 9]
# data.sort()
# print(data) #data변수에는 정렬된 결과가 저장되어 있음
#
# data = [2, 4, 3, 1, 5, 10, 9]
# print(sorted(data))
# print(data)#data변수에는 정렬 전의 data가 그대로 저장되어 있음
#
# x=3
# x%2
#
# 홍길동="881120-1068234"
# print(홍길동[:6])
# print(홍길동[7:])
#
# a = [1, 3, 5, 4, 2]
# a.sort( )
# a.reverse( )
#
# a = (1, 2, 3)
# a = a + (4,)
#
# a = {'A':90, 'B':80, 'C':70}
# print(a.pop('B')) #리스트의 경우에는 마지막 요소가 추출
# #딕셔너리에서는 추출하고자 하는 데이터의 키를 인수로 지정

# a = dict()
# #print(a)
#
# #딕셔너리의 키는 변하지 않는 값을 사용
# a['name'] = 'python'
# #a[250] = 'python'
# #a[('a',)] = 'python'
#
# #a[[1]] = 'python' #[1]는 리스트이므로 변하는 값 -> 딕셔너리의 키로 사용할 수 없음
# print(a)
#
# #dic.keys()
#
#
# dic={'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}
# print(dic.keys())
# print(dic.values())
# print(dic.items())
#
# dic.clear() #모든 요소들을 제거
# print(dic) #{}
#
# dic={'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}
# print(dic['아이디'])
# print(dic.get('체력'))#키에 연결된 값을 추출
# # 딕셔너리.get('키') == 딕셔너리['키']
# #print(dic['민첩']) #KeyError: '민첩'
# #print(dic.get('민첩')) #None(거짓)
#
# #"", None, 0 등은 거짓으로 분류됨
# #
# # if "a":
# #     print('민첩 능력이 있습니다')
# # else:
# #     print("민첩 능력치가 존재하지 않습니다")
#
#
# dic={'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}
# print(dic.get('민첩',0)) #민첩 키가 존재하지 않으면 디폴트값으로 0을 출력
#
#
# #집합(set):{}, 순서가 없음, 중복 불허
s1=set([1,2,2,3])#리스트 자료를 기초로 집합(중복 제외)을 생성
print(s1)
#
# s2=set("hihello")#리스트 자료를 기초로 집합(중복 제외)을 생성
#print(s2)
#print(list(s2))
#
# # list()
# # tuple()
# # dict()
# s3=set()
# print(s3)
#

#
#
# s1=set([1,2,2,3])#리스트 자료를 기초로 집합(중복 제외)을 생성
# print(s1)
# #print(s1[2]) # 에러 발생: 리스트나 튜플은 순서가 있음 -> 인덱싱을 통해 데이터 접근 o
# #반면에 셋(set)은 순서가 없음 -> 인덱싱을 할 수 없음 => 만약 인덱싱으로 접근하고 싶다면? 리스트 or  튜플로 변환한 다음 인덱싱 수행
# s11=list(s1)
# print(s11[2])
#
# s1=set([1,2,3,4,5,6])
# s2=set([4,5,6,7,8,9])
# #교집합
# print(s1&s2)
# print(s1.intersection(s2))
# #합집합
# print(s1|s2)
# print(s1.union(s2))
# #차집합
# print(s1-s2)
# print(s1.difference(s2))
# print(s2-s1)
# print(s2.difference(s1))

# s3=set()
#s3.add(3)
#s3.add(3,4) 오류
#s3.add([3,4]) 오류
#add 함수는 데이터 1개만 추가 가능

#update 함수 : 여러 개를 추가
# s3.update([1,2,3,5,6])
# print(s3)
#
# s3.update([1,2,3,15,16])
# print(s3)
#
# s3.remove(2)
# print(s3)
#
# #불 자료형: 참(True) or 거짓(False)
# #참: "test", [1,2], 1, ...
# #거짓: "",  None, 0, [], (), {}
#
# a=[1,2,3]
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)
# print(a.pop())
# print(a)
# # print(a.pop()) 에러발생
# # print(a)
#
# #while 조건:     #조건이 참인 동안에 문장 수행을 반복하세요(조건이 거짓이 될 때까지)
#     # 문장1
#     # 문장2
#     # ...
#
# a=[1,2,3]
# while a:  #True : a 리스트에 pop 대상 데이터가 남아 있는 경우
#     print(a.pop()) #3 2 1
#
# print("반복문을 종료합니다")
#
# # if 조건:
# #     문장1
# #     문장2
# # else:
# #     문장1
# #     문장2
# if []:  #if 조건   만약에 조건을 만족하면
#     print("참")
# else: #만족하지 않으면
#     print("거짓")
#
#
#
# print(bool([]))
# print(bool("dsfdfs"))
# print(bool(0))
#
# a=[1,2,3]
# #변수=리스트? 리스트(객체)는 메모리에 생성되고, 변수 a는 리스트가 저장된 메모리상의 주소를 가지게 됨
#
# #a변수가 가리키는 메모리의 주소를 확인
# print(id(a)) #메모리의 3005064741760 번지에 [1,2,3]이 저장되어 있다는 의미
#
# b=[2,3,4]
# print(id(b))#메모리의 3005065050624 번지에 [2,3,4]이 저장되어 있다는 의미
#
# print("="*50)
# a=[1,2,3]
# b=a #a가 가지고 있는 값은 엄밀히 얘기하자면 [1,2,3]이 저장되어 있는 "주소값"
# print(a)
# print(b)
#
# print(id(a))
# print(id(b)) #두 값이 같음 (= a가 가지고 있는 주소값이 b에 복사(저장))
#
# a[1]=5
# print(a)
# print(b)
#
# #is : 두 변수가 가리키는 메모리상의 대상이 동일한 지 확인
# print(a is b) #a와 b가 가리키는 메모리상의 대상이 동일한가요?
#
# a=[1,2]
# b=[1,2]
# print(id(a))
# print(id(b))
# print(a is b) #False 주소가 같냐?
# print(a==b) #True
#
#
# a=[1,2]
# b=[1,2]
# print(a==b) #값이 같냐?
#
#
#
# a=[1,2]
# b=a
# a[1]=10 #2->10
# print(a)
# print(b)
#
# #b변수를 만들때, a변수의 값은 가져오면서도 a와는 다른 주소를 가리키도록 하고 싶다면
# #1번째 방법 [:] 이용
# a=[1,2,3]
# b=a[:] #b=a은 동일한 대상(데이터)를 가리킴
# print(id(a))
# print(id(b))
# print(a)
# print(b)
# a[1]=10
# print(a)
# print(b)
#
# #2번째 방법 copy모듈에 있는 copy함수를 이용
#
# # 패키지(폴더):모듈(파일) 또는 패키지의 묶음
# # 모듈:관련 함수들의 묶음
#
# #from 모듈명 import 함수명
# #모듈로 부터 함수를 가져와라
# from copy import copy
# a=[1,2]
# b=copy(a) #b=a[:] 와 같음
# print(id(a))
# print(id(b))
# print(a is b)
#
#
# # if 조건문:
# #     코드
#
# x=1
# if x==1:
#     print("x는 1이다")
#     print("x는 홀수이다")
# print("출력됩니다") #if 문과는 별개의 문장
#     #pass #코드를 수행하지 않고 넘어감
#     #print("x는 1이다")
#
# x=5
# if x>=1:
#     print("1이상")
#     if x>=5:
#         print("5이상")
#     if x==10:
#         print("10")
# print("출력")
#
#
# money=False
# if money:
#     print("버스")
#     print("택시")
# else:
#     print("도보")
#
# #or, and, not : 여러 조건을 표현
#
# money=6000
# card=True
# #if money>=5000 and card: #or:또는, and:그리고(이고, 이면서)
# #if card != False:
# if not money<=5000:
#     print("택시")
# else:
#     print("버스")
#
# #x in 리스트(튜플,문자열)
#
# print(4 in [1,2,3])
# print(4 not in [1,2,3])
#
# print('a' in ('a','b'))
#
# print('h' in "hello")
#
# # if 조건:
# #     문장
# # else:
# #     문장
# if 조건:
#     문장
# elif 조건:
#     문장
# elif 조건:
#     문장
# else:
#     문장
#
#
# money=1000
# card=True
# if money > 3000:
#     print("택시")
# elif card: #3000 원 이하의 돈을 가지고 있지만, 카드를 가지고 있다면
#     print("버스")
# else: #돈이 3000원 이상도 없고, card도 없는 경우
#     print("도보")

#자율주행차 동작의 일부를 if구문으로 작성한다면, if가 몇개 필요할까?  무한대
# if  앞에 뭔가 있다면:
#     결과=확률계산
#     if 결과가 0.5 이상:
#         멈춰
#     else:
#         달려

#
# if 조건: 문장
# else:문장

# s=60
# if s>=60:
#     msg="pass"
# else:
#     msg="fail"
# print(msg)

# s=60
# #퇴근을 5초 당겨주는 궁극의 코드(현실은 당겨진 5초 동안에 다른 일을 하게 됨)
#
# msg="pass" if s>=60 else "fail"
# #조건문이 참인 경우 if 조건문 else 조건문이 거짓인 경우
# #만약에 s가 60 이상이면 "pass" 를 msg에 대입하고, 아니면 "fail"를 msg에 대입
#
# print(msg)
#
# #반복문 : for, while
# i=0
# # while i<10: #"i 변수 값이 10보다 작다" 라는 조건을 만족하는 동안에, 문장을 반복하세요
# #     i=i+1
# #     print(i,"번째 반복 수행")
#
# while True: #무한 루프(loop)
#     i=i+1
#     print(i,"번째 반복 수행")
#     #조건을 만족했을때 반복 종료
#     if i>10:
#         break #반복문을 빠져나가라

# # prompt="""
# # 1.추가
# # 2.삭제
# # 3.종료
# # 번호 입력:"""
# # #print(prompt)
# #
# # num=0
# # while num !=3:
# #     print(prompt)
# #     num=int(input())
#
# a=0
# while a<10:
#     a=a+1
#     if a%2==0: continue #continue는 while의 시작위치로 이동
#     print(a)
#
# a=0
# while a<10:
#     a=a+1
#     if a%2==0: break #break는 반복문을 벗어나게 됨
#     print(a)
#
# #while문을 이용하여 1~100사이의 자연수 중 4의 배수의 합을 출력
# i=0
# sum=0
# while i<100:
#     i=i+1
#     if i%4==0:
#         sum=sum+i
# print(sum)
#
# i=1
# sum=0
# while i<=100:
#     if i%4==0:
#         sum=sum+i
#     i=i+1
# print(sum)
#
# #for문
# # for 변수 in 리스트(튜플,문자열):
# #     문장1
# #     문장2
#
# #mylist=[1,2,3]
# mylist=["하나", "둘", "셋"]
# for i in mylist:
#     print(i)
#
# for i in "bigdata":
#     print(i)
#
# for i in [(1,2),(3,4),(5,6)]:
#     print(i)
#
# for i in (1,2,3):
#     print(i)
#
# for i,j in [(1,2),(3,4),(5,6)]:
#     print(i)
#     print(j)
#     print("="*50)
#
# for i in range(5):
#     print(i)
#
# for i in range(3,10):
#     print(i)
#
# for i in range(3,10,2):
#     print(i)
#
#
# a=[5,6,7,8]
# for i in range(len(a)):
#     print(i)
#
# #for & range 사용
# # 2 4 6 8 10 12 14 16 18
# print("="*50)
# for dan in range(2,10): #dan=2 to 9
#     for i in range(1, 10): #i=1 to 9
#         print(dan*i, end=" ") #
#     print("") #줄 바꿈
#
# # 2 4 6 8 10 12 14 16 18
# # 3 6 9 12 15 18 21 24 27
# # 4 8 12 16 20 24 28 32 36
# # 5 10 15 20 25 30 35 40 45
# # 6 12 18 24 30 36 42 48 54
# # 7 14 21 28 35 42 49 56 63
# # 8 16 24 32 40 48 56 64 72
# # 9 18 27 36 45 54 63 72 81
#
# import random
# print(random.random()) #0~1
# # print(random.randrange(1,7)) #1~6
# # print(random.randrange(1,7))
#
# print(random.randint(1,46)) #1~45
# print(random.randrange(1,46)) #1~45
#
# #다른점
# print(random.randrange(1,46,2)) #1~45까지 2씩 증가시킨 수 중에서 난수 발생












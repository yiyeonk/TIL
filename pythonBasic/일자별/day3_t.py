# a=[10,20,30]
# s=a.pop()
# print(s)
# #print(a)

# a=[10,20,30]
# a.pop() #가장 마지막 위치에 있는 데이터를 제거
# a.pop()
# a.pop()
# print(a)


#튜플, 시퀀스?, 딕셔너리

#튜플은 리스트와 거의 동일
#차이점?튜플은 값을 변경(생성, 삭제, 수정)할 수 없음, ()사용
# t1=(1,2,3) #튜플
# print(t1)
# print(type(t1))
# #del t1[1] #참조할때는 [](대괄호) 사용,  index 1의 값 제거, 에러발생!
#
# # t1[0]=5 에러
#
# print(t1[2]) #인덱싱
#
# print(t1[1:])#슬라이싱
#
# t2=('a',3,4)
# print(t1+t2)
#
# t3=(5,6)
# print(t3*5)
#
# print(len(t3))
#
# person=('kim',20,60.5,True)
# print(person)
#
#
# #t4=(7) 정수
# t4=(7,)
# print(t4)
# print(type(t4))
#
# # a=(2+3*4) ==  a=(14)
# # print(a)
#
# #t5=(5,8)
# t5=5,8 #되도록이면 튜플을 나타내는 기호(소괄호)로 묶어서 표현할 것
# print(t5)
# print(type(t5))
#
# t6=(1,2,(3,4))
# print(t6)
#
# print(range(5))
# print(list(range(5)))
#
# print(range(5))
# print(tuple(range(5)))
#
# print(tuple(range(5,20)))
#
# print(tuple(range(1,101,2)))
#
# # 튜플 -> 리스트 변환
# # 리스트 -> 튜플 변환
#
# x=tuple(range(1,10))
# print(x)
#
# #x에 저장된 5->50으로 변경하고 싶은 경우
# #x[4]=50 에러...
# #튜플->리스트->요소값 변경
# print(list(x))
# tempx=list(x)
# print(tempx)
# tempx[4]=50
# print(tempx)
#
# y=[1,2,3]
# tempy=tuple(y)
# print(type(tempy))
#
# s="hello"
# print(list(s))
# #리스트에 문자열을 주면 문자 리스트가 만들어 짐
# print(tuple(s))
# #튜플에 문자열을 주면 문자 튜플이 만들어 짐
#
# a,b,c=1,2,3
# print(a)
# print(type(a))
#
# a,b,c=[1,2,3]
# print(a)
# print(type(a))
#
# a,b,c=(1,2,3)
# print(a)
# print(type(a))
#
# k=(1,2,3)
# a,b,c=k
# print(a)
# print(type(a))
#
# #시퀀스 자료형 : 연속적으로 저장
# #리스트, 튜플, 문자열, range, bytes, bytearray 등은 모두 다 값들이 연속적으로 저장되어 있는 시퀀스 자료형
# #[1,2,3] (1,2,3) "hello" range(3)
#
#
# #시퀀스 자료형(리스트, 튜플, 문자열, range, bytes, bytearray)의 공통 기능
#
# #데이터 존재 유무 확인
# #작성방법 : 찾고자하는값 in 시퀀스객체
#
# #a=[0,10,...,90]
# a=list(range(0,91, 10))
# #a에 30이 있는지 확인?
#
# print(30 in a) # True
# print(45 in a) # False
#
# #a에 30이 없는지 확인?
# print(30 not in a) # False
# print(45 not in a) # True
#
# print("5가 있나요?", 5 in (1,2,3,4,5))
# print("5가 없나요?", 5 not in (1,2,3,4,5))
#
# print("hello 문자열에 h문자가 있나요?", 'h' in "hello")
#
# print(1 in range(5))
#
# # 시퀀스 객체 연결(range는 불가능)
# a=[1,2]
# b=[3,4]
# print(a+b)

#print(range(0,4)+range(4,6)) 에러
#range객체들을 연결할 수 없으므로, range->list로 변경한 다음 연결
print(list(range(0,4))+list(range(4,6)))
print("hi"+"hello")

#문자열 연결 : +
#문자열과 숫자 연결안됨
#print("hi"+100) #에러 발생

#문자열과 숫자 연결 => 숫자(정수,실수) -> 문자(열)로 변경을 먼저...
# print("hi" + str(100))
# print("hi" + str(100.111))
#
# #시퀀스 반복(*), 단, range는 *연산자 사용 불가
# #시퀀스객체 * 정수 or  정수 * 시퀀스객체
# print([1,2,3] * 5)
# print(5*[1,2,3])
#
# #단, range는 *연산자 사용 불가
# #print(range(0,5,1)*3)
#
# #range 객체를 튜플 또는 리스트로 변경한 다음 반복
# print(list(range(0,5,1))*3)
#
# print("hello"*5)
# print("ㅋ"*100)
#
# #len(시퀀스객체) : 시퀀스 데이터(요소) 개수
# a=[10,20,30,40]
# print(len(a))
# b=(1,2,3,4)
# print(len(b))
# print(len(range(1,10,2)))
# print(len("hello"))
# print(len("h'el'lo"))
#
# print(len("안녕하세요")) #len함수는 길이를 구함.
# #파이썬 2.7 버전에서는 바이트 수가 나옴(15)
# #파이썬 3.xx 버전에서는 글자의 수가 나옴(5)
#
# s="안녕하세요"
# print(len(s.encode('utf-8')))
# #utf-8에서는 한글 한 글자가 3byte, 3*5 = 15 바이트
#
# print(s.encode('utf-8'))
#
# #시퀀스 객체는 대괄호[] 기호로 참조
# a=[5,6,7,8,9]
# print(a[3])
# print(a[-2])
#
# a=(5,6,7,8,9)
# print(a[3])
# print(a[-2])
#
# r=range(1,10,2)
# print(r[2])
#
# s="hello"
# print(s[3])
# print(s[-4])
#
# print(s)
#
# print(r[-4])
#
# #print(s[5])
#
# #del 시퀀스객체[인덱스] : 튜플, range, 문자열도 삭제 안됨
# b=[10,20,30,40]
# del b[1]
# print(b)
#
# # h="hello"
# # del h[2] 에러 발생
# # print(h)
#
#
#
#
# #시퀀스객체[시작인덱스:끝인덱스]
# a=[10,20,30,40]
# print(a[0:3])
# print(a[0:0])
# print(a[0:1])
# print(a[1:-1:1])
# print(a[3:1:-1])
#
# print(a[0:len(a)]) #a[0:4]=a[0]~a[3]
# print(a[:3:2]) #a[0]~a[2], 2칸씩 건너뛰기 -> a[0], a[2] 참조
#
# r=range(20)
# print(r[3:8])
# print(r[:15:3])
# print(list(r[:15:3]))
#
# s="hello python"
# print(s[:10])
# print(s[:10:2])
#
# #slice 객체를 이용하여 slicing
# print(range(20)[slice(3,9,2)])
# #range(20): range(20)객체[]
#
# print(list(range(5,20)[slice(3,9,2)]))
#        range=[5,6,7,8,9,10,11,12,13,...,19]
#                     3   5     7

print(list(range(20)[3:9:2]))
print(list(range(20)[slice(3,9,2)]))

a=list(range(10))
print(a)

a[1:4]='a'
print(a)
print("="*50)
a=list(range(10))
a[1:4]=['a','b','c']
print(a)

a=list(range(10))
a[2:7:2]=['x','y','z']
print(a)

a=list(range(10))
#a[2:7:2]=['x','y']
#a[2:7:2]=['x','y','z','zz']

print(a)
del a[2:9:2]
print(a)

#IT(프로그램 개발자) 직무 유형 : SI(시스템통합), SM(시스템유지보수)


#딕셔너리(사전):단어-의미 구조와 유사하게 이름=홍길동, 생일=20200104 등과 같은 형식으로 표현
#                          딕셔너리? 키(KEY)와 값(VALUE)의 쌍으로 표현
#                    표현 예)딕셔너리={키:값, 키:값, ...}
#딕셔너리는 시퀀스 객체가 아님. 데이터 참조 방법이 다름
#키는 변하지 않는 값(상수), 값에는 변하는 값을 표현
#상수:문자상수(따옴표로 묶어서), 숫자상수(1,2,3,4,...)

d={'name':'kim', 'addr':'seoul', 'age':25, 'nn':['별명1', '별명2']}
#{키:값,...}, 키는 작은(큰)따옴표로 묶어서 표현, 값은 수치는 그대로, 문자는 작은(큰)따옴표로

myname='lee'
myname='park'
print(myname)

d2={1:"hi"}
print(d2)
#나이=26

#[1,10,15,20,30,70] 데이터들 사이에 연관 관계가 없음
#리스트(튜플) 구조로 연관 관계가 있는 데이터를 표현하기가(이해하기도) 어려움
#ex) 게임 캐릭터 정보를 리스트로 표현
# ['홍길동', 10, 100, 20, 200, 50, ...]

#딕셔너리 : 연관 데이터를 저장하기 위한 용도의 자료형
#ex) 게임 캐릭터 정보를 딕셔너리로 표현
# {'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50, ...}
#딕셔너리변수명={키1:값1, 키2:값2,...}


dic={'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}
print(dic)

#키가 중복되면, 마지막 키와 값만 저장
dic={'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50, '아이디':'임꺽정'}
dic={'아이디':['홍길동', '이순신', '임꺽정'], '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}

print(dic)

#키에는 딕셔너리, 리스트 등 자료구조가 올 수 없음
# dic={[10,20]:30}
# print(dic) #에러

a=[]
print(a)
b=list()
print(b)

#빈 딕셔너리 생성
a= {}
print(a)
b=dict()
print(b)

dic={'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}
c1=dict(아이디='홍길동',레벨=10, 체력=100, 마나=20, 공격력=200, 방어력=50) #올바른 문법
#한글 변수도 가능
#c=dict('아이디'='홍길동',레벨=10, 체력=100, 마나=20, 공격력=200, 방어력=50) 오류
c2=dict(zip(['아이디','레벨','체력','마나','공격력','방어력'],['홍길동',10,100,20,200,50])) #올바른 문법
#dict(zip([키리스트], [값리스트]))
print(dic)
print(c1)
print(c2)
#print(dict(zip(['a','b'],[1,2])))#zip 객체를 dict로 변환

#리스트 내부에 (키, 값) 형식의 튜플로 표현
c3=dict([('아이디','홍길동'),('레벨',10), ('체력',100), ('마나',20), ('공격력',200),('방어력',50)])
print(c3)
#dict([(튜플1),(튜플2),...])

#중괄호로 표현
c4=dict({'아이디':'홍길동','레벨':10, '체력':100, '마나':20, '공격력':200,'방어력':50})
print(c4)

# print(c)
# print(dic)

#딕셔너리 데이터 추가/삭제
a={'nn':'bear'}
print(a)
#딕셔너리 a에 데이터 추가
a['addr']='seoul'
a[100]=300
#딕셔너리변수명[키이름]=값
print(a)
a['hobby']=['a','b','c']

print(a) #{'nn': 'bear', 'addr': 'seoul', 100: 300, 'hobby': ['a', 'b', 'c']}
#del a[2] 에러
del a[100]
print("삭제 후 : ", a)

#del 딕셔너리변수명[키] => 키와 값을 모두 제거

#{홍길동:프로그래밍, 임꺽정:분석, 이순신:딥러닝}

# 이름=[홍길동, 임꺽정, 이순신]
# 취미=[프로그래밍, 분석, 딥러닝]
# print(이름[0])
# print(취미[0])

#딕셔너리 활용 -> json 파일 포맷(웹)





dic={'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}
print(dic)
print(dic.keys())#키만 추출
print(dic.values())#값만 추출
#키와 값을 추출
print(dic.items())

print("="*50)
mykey=dic.keys()
print(mykey)
#print(mykey[0])
listmykey=list(mykey)
print(listmykey)

#mykey=dict_keys(리스트객체)


dic={'아이디':'홍길동', '레벨':10, '체력':100, '마나':20, '공격력':200, '방어력':50}
dic['저항력']=100
print(dic)
print(dic['마나'])

#print(dic['민첩성']) 없는 키를 참조하려고 하면 에러 발생
#딕셔너리에 키가 있는지 확인?
#print(dic.keys())
print('민첩성' in dic) #not in
print('마나' in dic) #not in

print(len(dic))
























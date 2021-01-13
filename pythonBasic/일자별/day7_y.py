# 1~10까지 짝수만 저장
# evenNum=[]
# for i in range(1,11):
#     if i % 2 == 0:
#         evenNum.append(i)
#
# print(evenNum)
#
# # 리스트 컴프리헨션
# [i for i in range(1,11) if i% 2 == 0]
#
# print([(x,y)for x in ['쌈밥', '치킨', '피자']])
#
# [x for x in range(10) if x <5]
#
#
# a = [1,-5,4,2,-2,10]
# # a에 저장된 값이 0보다 크면 a값을, 작으면 0을 저장하고 출력
#
# print([i if i > 0 else 0 for i in a])
#
# a = [1,2,3,4,5]
# print(["pass" if i ==1 else "fail" if i==2 else "no" for i in a])

# for v in d3.values():
#     print(v)
#
# for k,v in d3.items():
#     print(k,v)

# keys=['a','b','c','d']
# print(dict.fromkeys(keys))
#
# for key, value in dict.fromkeys(keys).items(): #dict.fromkeys(keys)는 딕셔너리
#     print(key, value)
#
# d4={key:value for key, value in dict.fromkeys(keys).items()}
# print(d4)

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

newx = {k:v for k, v in x.items() if k!='b'}
print(newx)



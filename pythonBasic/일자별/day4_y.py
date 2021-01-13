# Q1.
a = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
print(set(a))

# Q2.
i = 0
sum = 0

while i < 1000:
    i = i + 1
    if i % 3 == 0 and i % 7 == 0:
        sum = sum + i
print(sum)

# Q3-1.
i = 1
while i < 6:
    print('*'*i)
    i += 1

# Q3-2.
i = 1
while i < 6:
    print(('*'*i).rjust(6))
    i += 1

# Q3-3.
i = 1
while i < 10:
    print(('*'*i).center(9))
    i += 2

# Q4.
for i in range(101):
    print(i)

# Q4-1.

for i in range(2,101):
    num = True
    for j in range(2,i):
        if i % j == 0:
            num = False
            break
    if num:
        print(i, end=" ")

# Q5.
a = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
sum = 0

for i in a:
    sum = sum + i
mean = sum/len(a)
print(mean)

# Q6.
import random

# print(random.sample(range(1,46),6))



# Q7.

coffee = 10
price = 300

while True:
    pay = int(input('돈을 넣어 주세요: '))
    if pay > 300:
        print("거스름돈 %d원을 주고 커피 제공" % (pay-price))
        coffee -= 1
    elif pay == 300:
        print("커피 제공")
        coffee -= 1
    else:
        print("돈을 다시 돌려주고 커피를 주지 않습니다")
        print("남은 커피의 양은 %d개 입니다." % coffee)
        print("돈을 넣어 주세요")
        break
print("종료합니다.")

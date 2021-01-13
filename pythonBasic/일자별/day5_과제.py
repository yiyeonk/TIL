# 1. 리스트에서 20 보다 작은 3의 배수를 출력하라
list = [13, 21, 12, 14, 30, 18]

for i in list:
    if i < 20 and i % 3 == 0:
        print(i)

# 2. 리스트에서 세 글자 이상의 문자를 화면에 출력하라
list = ["I", "study", "python", "language", "!"]

for i in list:
    if len(i) >= 3:
        print(i)

# 3. 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라.
list = ['hello.py', 'ex01.py', 'intro.hwp']

for i in list:
    i = name,ext = i.split(".")
    i.remove(ext)
    print(i)


# 4. my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]

for i in range(3):
    print(my_list[i:i+2])

# 5. 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.
my_list = ["가", "나", "다", "라"]

for i in range(3,0,-1):
    print(my_list[i], my_list[i-1])

# 6.리스트에 5일간의 저가, 고가 정보가 저장돼 있다. 고가와 저가의 차를 변동폭이라고 정의할 때, low, high 두 개의 리스트를 사용해서 5일간의 변동폭을 volatility 리스트에 저장하라.
low_prices  = [100, 200, 400, 800, 1000]
high_prices = [150, 300, 430, 880, 1000]

volatility = []
for i in range(len(high_prices)):
    volatility.append(high_prices[i]-low_prices[i])
print(volatility)


# 7.리스트에 저장된 데이터를 아래와 같이 출력하라.
apart = [ [101, 102], [201, 202], [301, 302] ]

for i in apart:
    for j in i:
        print(j,"호")
    print("----")

# 8. 구글 입사 test
# 1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가?
# 8이 포함되어 있는 숫자의 갯수를 카운팅 하는 것이 아니라 8이라는 숫자를 모두 카운팅 해야 한다.
# (※ 예를들어 8808은 3, 8888은 4로 카운팅 해야 함)

count = 0

for i in range(10001):
    temp = str(i)
    for j in temp:
        if j == '8':
            count += 1

print(count)
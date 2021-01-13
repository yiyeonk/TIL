# 과제_day1

# Q1.
letters = 'python'
print(letters[0], letters[2])

# Q2.
cn = "24가 2210"
print(cn[-4:])

# Q3.
s = "파이썬파이썬파이썬"
print(s[0]+s[3]+s[6])
print(s[::3])  # offset: 몇 칸을 건너뛸 것인지, 양수(좌->우), 음수(우->좌)

# Q4.
num_str = "720"
print(int(num_str))

# Q5.
data = "15.79"
print(float(data))

# Q6.
price = 48584
month = 36
total = price*month

print("총 금액은", total, end=""); print("원 입니다.")
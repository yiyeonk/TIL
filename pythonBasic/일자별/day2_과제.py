# Q1.
ticker = "btc_krw"
print(ticker.upper())

# Q2.
ticker = "BTC_KRW"
print(ticker.lower())

# Q3.
a = "hello world"
print(a.split())

# Q4.
ticker = "btc_krw"
print(ticker.split("_"))

# Q5.
date = "2020-12-30"
print(date.split("-"))

# Q6.
data = "039490     "
print(data.rstrip())

# Q7.
name1 = "김민수"
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))

# Q8.
print("이름: {0} 나이: {1}".format(name1, age1))
print("이름: {0} 나이: {1}".format(name2, age2))

# Q9.
price = "5,969,782,550"
price = int(price.replace(",",""))
print(type(price))

# Q10.
분기 = "2020/12(E) (IFRS연결)"
print(분기[:7])

# Q11.
string = 'abcdfe2a354a32a'
print(string.replace("a","A"))

# Q12.
pin = "881120-1068234"
print(pin[-7])

# Q13.
a = "a:b:c:d"
print(a.replace(":","#"))

# Q14.
print(" ".join(['Life', 'is', 'too', 'short']))





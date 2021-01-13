# Q1.
movie_rank = ['닥터 스트레인지', '스플릿', '럭키']
print(movie_rank)

# Q2.
movie_rank.append('배트맨')
print(movie_rank)

# Q3.
movie_rank.insert(1,'슈퍼맨')
print(movie_rank)

# Q4.
del movie_rank[3]
print(movie_rank)

# Q5.
movie_rank.pop()
movie_rank.pop()
print(movie_rank)

# Q6.
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# Q7.
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums[::2])

# Q8.
nums = [1,2,3,4,5]
print(nums[::-1])

# Q9.
interest = ['삼성전자', 'LG전자', 'Naver']
print(" ".join(interest[::2]))

# Q10.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# Q11.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# Q12.
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

# Q13.
pin = '881120-1068234'
print(pin.split("-"))

# Q14.
print((1,2,3)+(4,))

# Q15.
a = dict()
print(a)

a['name']='python'
a[('a',)] = 'python'
a[[1]] = 'python' # 키에는 리스트가 올 수 없음
a[250] = 'python'

# Q16.
a = {'A': 90, 'B': 80, 'C': 70}
print(a.pop("B"))
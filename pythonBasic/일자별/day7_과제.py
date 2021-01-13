#
#
# s={1, 3, 4, 8, 13, 17, 20}
#
# def shortest(s):
#     distance=[]
#     s = list(s)
#     pair = list(zip(s[:-1],s[1:]))
#     for i in range(len(s)-1):
#         distance.append(abs(s[i]-s[i+1]))
#         res = min(distance)
#         newpair = list(zip(s[:-1],s[1:],distance))
#     print([i[:2] for i in newpair if i[2] == res])
#
# shortest(s)


#
# # 회문 : 유전자 염기서열 분석
# # mgram: 언어패턴
#
# #2.
# w = input("단어입력 : ")
# isPalindrome=True  # 회문 여부, 초기값은 true
# w = w.replace(" ","")  # 공백제거
# for i in range(len(w)//2):
#     if w[i] != w[-1-i]:  # 왼쪽문자와 오른쪽 문자가 다른 경우
#         isPalindrome = False
#         break
# print(isPalindrome)

# w = input("단어입력 : ")
# print(w==w[::-1])
# print(w)
# print(w[::-1])
#
# print(list(w)) == list(reversed(w))
# # nurses run => nursesrun
# # 공백문자 -> 전처리: 제거

w = 'level'
print(w)
print(w==''.join(reversed(w)))
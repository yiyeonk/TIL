# # Q1. [문자열 바꾸기] 다음과 같은 문자열이 있다. > a:b:c:d
# # 문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오. > a#b#c#d
# a = "a:b:c:d"
# a = a.split(":")
# print("#".join(a))
#
# # Q2. 리스트 평균 구하기
# # 다음은 A학급 학생의 점수를 나타내는 리스트이다.
# # 다음 리스트에서 60점 이상 점수의 평균을 구하시오.
#
# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]
# score = []
#
# for i in A:
#     if i >= 60:
#         score.append(i)
#
# print(sum(score)/len(score))
#
# # Q3. [평균값 구하기] 다음과 같이 총 10줄로 이루어진 sample.txt 파일이 있다.
# # sample.txt 파일의 숫자 값을 모두 읽어 총합과 평균 값을 구한 후,
# # 평균 값을 result.txt 파일에 쓰는 프로그램을 작성하시오.
# num = ["70\n","60\n","55\n","75\n","95\n","90\n","80\n","80\n","85\n","100"]
#
# with open("sample.txt","w") as f:
#     f.writelines(num)
#
# with open("sample.txt","r") as f:
#     number = f.read().split("\n")
#     number = [int(i) for i in number]
#
# print(type(number))
#
# sum = sum(number)
# mean = sum/len(number)
#
# with open("result.txt", "w") as f:
#     res = "total:{0}\nmean:{1}".format(sum, mean)
#     f.writelines(res)
#
# # Q4. [모스 부호 해독] 문자열 형식으로 입력받은 모스 부호(dot:. dash:-)를 해독하여 영어 문장으로 출력하는 프로그램을 작성하시오.
# # 글자와 글자 사이는 공백 1개, 단어와 단어 사이는 공백 2개로 구분한다.
# # 예를 들어 다음 모스 부호는 "HE SLEEPS EARLY"로 해석해야 한다.
#
# morse_dic= {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E',
#             '..-.':'F','--.':'G','....':'H','..':'I','.---':'J',
#             '-.-':'K','.-..':'L','--':'M','-.':'N','---':'O',
#             '.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T',
#             '..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
#
# code = '.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'
# key=code.split(" ")
#
# for i in key:
#     res=[]
#     for j in morse_dic:
#         if i==j:
#             res.append(morse_dic[j])
#     print("".join(res), end=" ")

# print("-"*10+"선생님 코드"+"-"*10)
#
# dic = {
#     '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F',
#     '--.':'G','....':'H','..':'I','.---':'J','-.-':'K','.-..':'L',
#     '--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R',
#     '...':'S','-':'T','..-':'U','...-':'V','.--':'W','-..-':'X',
#     '-.--':'Y','--..':'Z'
# }
#
# def morse(src):
#     res = []
#     for word in src.split("  "): # 공백문자 2개로 분리 / 입력된 문장에 저장된 단어 3개
#         for c in word.split(" "): # c에는 문자가 저장
#             res.append(dic[c])  # key에 대한 값
#         res.append(" ")  # 단어와 단어가 공백문자로 구분
#     return "".join(res)
#
# print(morse('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))





# print("-"*10+"필사"+"-"*10)
# # Q5. ngram 기반 두 문장 유사도 구하기(n=2, n=3)
# text1 = "오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
# text2 = "멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"
#
# def N_gram(text,n):
#     result = []
#     text=text.replace(" ", "")
#     for a in range(len(text) - n + 1):
#         result.append(text[a : a + n])
#     return result
#
# def percent_text(text1,text2,n):
#     count = 0
#     r=[]
#     nText1=N_gram(text1,n)
#     nText2=N_gram(text2,n)
#     for i in nText1:
#         for j in nText2:
#             if i ==j:
#                 count += 1
#                 r.append(i)
#     similary = count / len(nText1) * 100
#     print("첫번째 문장과의 유사도는 {:.2f}% 입니다.".format(similary))
#
# percent_text(text1,text2,2)
# percent_text(text1,text2,3)


# print("-"*10+"선생님 코드"+"-"*10)

def ngram(s, num):
    res = []    # list를 set을 이용해서 풀어보기
    slen=len(s)-num+1  # ngram에 해당하는 길이
    for i in range(slen):
        ss = s[i:i+num]  # 두글자씩 쪼개서 출력
        res.append(ss)
    return res


def diff_ngram(sa, sb, num):
    a=ngram(sa, num)
    b=ngram(sb, num)
    # print(a)
    # print(b)
    cnt = 0 # 일치한 단어의 개수를 저장하기 위한 변수
    r=[] # 일치한 단어를 저장하기 위한 변수
    for i in a:
        for j in b:
            if i == j:  # 두 단어가 일치한다면
                cnt += 1
                r.append(i)
    return cnt/len(a), r


a="오늘 멀티캠퍼스에서 너무 쉬운 프로그래밍을 공부했다"
b="멀티캠퍼스에서 공부했던 오늘의 프로그래밍은 너무 쉬웠다"

r2, word2 = diff_ngram(a, b, 2)  # 바이그램(bi-gram)
print("2-gram", r2, word2)  # 유사도, bigram으로 묶인 단어셋

r3, word3 = diff_ngram(a, b, 3)  # 바이그램(bi-gram)
print("2-gram", r3, word3)  # 유사도, bigram으로 묶인 단어셋

# 수정사항
# 1) 중복 허용 안되도록
# 2) 두 문장에서 길이가 긴 문장의 단어 개수를 분모

# 축약어 풀어쓰기

# 축약어를 풀어서 일반적인 문장으로 변환하는 프로그램

table = {"B4": "Before",
         "TX": "Thanks",
         "BBL": "Be Back Later",
         "BCNU": "Be Seeing You",
         "HAND": "Have A Nice Day"}

message = input("번역할 문장을 입력하시오: ")
words = message.split()
result = ""
for word in words:
    if word in table:
        result += table[word] + " "
    else:
        result += word

print(result)

#임의로 3개의 패스워드를 생성하여 출력하는 함수
#패스워드는 알파벳 소문자와 숫자를 랜덤하게 조합한다.
#패스워드는 6자리로 출력한다.

import random

def genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""

    for i in range(6):
        index = random.randrange(len(alphabet))
        password = password + alphabet[index]
    return password

print(genPass())
print(genPass())
print(genPass())

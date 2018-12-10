# 회문 검사하기

# 회문이란 앞으로 읽으나 뒤로 읽으나 동일한 문장이다.
# 사용자로부터 문자열을 입력받고 회문인지 검사하는 프로그램을 작성해보자.

def check_pal(s):
    low = 0
    high = len(s) - 1

    while True:
        if low > high:
            return True

        a = s[low]
        b = s[high]

        if ( a!= b ):
            return False
        low += 1
        high -= 1

s = input("문자열을 입력하세요: ")
s = s.replace(" ", "")

if(check_pal(s) == True):
    print("회문입니다.")
else:
    print("회문이 아닙니다.")

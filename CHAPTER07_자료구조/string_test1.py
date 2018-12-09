# 문자열의 검사

s = input("연도를 입력하세요: ")
if not s.isdigit():
    print("숫자만 입력해주세요!")
else:
    print(s)

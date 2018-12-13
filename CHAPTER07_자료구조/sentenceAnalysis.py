# 문자열 분석

# 문자열 안에 있는 문자, 숫자, 공백의 개수를 계산하는 프로그램을 작성해보자.

sentence = input("문자열을 입력하세요: ")

table = {"alphas": 0, "digits": 0, "spaces": 0}

for i in sentence:
    if i.isalpha():
        table["alphas"] += 1
    if i.isdigit():
        table["digits"] += 1
    if i.isspace():
        table["spaces"] += 1

print(table)

# 예시
# 문자열 입력: lee eun hak
# {'alphas': 9, 'digits': 0, 'spaces': 2}

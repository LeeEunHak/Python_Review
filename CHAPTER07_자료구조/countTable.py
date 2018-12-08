# 글자 빈도수 세기

# 문자열을 입력받아서 각 문자들의 빈도를 출력하는 프로그램

string = input("문자열을 입력하세요: ")

countTable = {}
for letter in string:
    countTable[letter] = countTable.get(letter, 0) + 1

print(countTable)

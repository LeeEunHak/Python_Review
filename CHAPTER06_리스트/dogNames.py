# 리스트에 강아지들의 이름을 저장하였다가 출력하는 프로그램
# 리스트는 문자열로 저장할 수 있다.

dogNames = []
while True:
    name = input("강아지의 이름을 입력하세요(종료시에는 엔터키) ")
    if name == "":
        break
    dogNames.append(name)

print("강아지들의 이름:")
for name in dogNames:
    print(name, end=", ")

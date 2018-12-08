# 단어 카운터

# 파일에 저장된 각각의 단어가 몇 번이나 나오는지 계산하는 프로그램

fname = input("파일이름: ")
file = open(fname, "r")

table = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1

print(table)

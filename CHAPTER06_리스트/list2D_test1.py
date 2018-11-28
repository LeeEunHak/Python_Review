# 2차원 리스트 만들어보기

rows = 3
cols = 5

s = []

for row in range(rows):
    s += [[0]*cols]

print("s =", s)

#실행 결과
# s = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

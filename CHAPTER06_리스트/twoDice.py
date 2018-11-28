# 2개의 주사위를 굴리면 36가지의 결과가 나온다.
# 이것을 6X6 크기의 2차원 리스트로 출력해보자.

rows = 6
cols = 6
table = []

# 2차원 리스트를 생성
for row in range(rows):
    table += [[0]*cols]

# 2차원 리스트의 각 요소에 rosw와 cols 값을 더하여 저장
for row in range(rows):
    for col in range(cols):
        table[row][col] = (row+1 + col+1) # 값이 0부터 시작이므로 1을 더함

print(table)

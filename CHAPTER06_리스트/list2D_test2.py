# 2차원 리스트 요소 접근 방법
# 2개의 인덱스 번호 사용하기

s = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
    ]

rows = len(s)       # 행의 개수
cols = len(s[0])    # 행에 들어있는 열의 개수

for r in range(rows):
    for c in range(cols):
        print(s[r][c], end=",")
    print()

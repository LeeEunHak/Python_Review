# 2차원 리스트 연산
# 특정한 행의 합을 계산해보자.

s = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
cols = len(s[0])

sum = 0;
for c in range(cols):
    sum = sum + s[1][c]

print(sum)

# 실행 결과
# 40

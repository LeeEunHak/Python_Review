# 지뢰찾기 게임
# 지뢰가 아닌 곳은 .으로 표시하고 지뢰인 곳은 #으로 표시한다.
# 어떤 칸이 지뢰일 확률은 난수를 발생시켜서 결정한다.
# 지뢰일 확률을 30%로 프로그램을 작성해보자.

import random

board = [[False for x in range(10)] for y in range(10)]

for r in range(10):
    for c in range(10):
        if (random.random() < 0.3):
            board[r][c] = True

for r in range(10):
    for c in range(10):
        if board[r][c]:
            print("# ", end=" ")
        else:
            print(". ", end=" ")
    print()

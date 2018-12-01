# 2차원 리스트와 함수
# 1과 0이 반복되는 체커보드 형태의 10X10 크기의 2차원
# 리스트를 초기와하는 함수 init()을 작성하고 실행하자.

table = []

# 2차원 리스트를 화면에 출력한다.
def printList(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[0])):
            print(mylist[row][col], end=" ")
        print()

# 2차원 리스트를 체커보드 형태로 초기화한다.
def init(mylist):
    for row in range(len(mylist)):
        for col in range(len(mylist[0])):
            if (row + col)%2 == 0:
                table[row][col] = 1

# 2차원 리스트를 생성한다.
for row in range(10):
    table += [[0]*10]

init(table)
printList(table)

# 출력결과

# 1 0 1 0 1 0 1 0 1 0 
# 0 1 0 1 0 1 0 1 0 1 
# 1 0 1 0 1 0 1 0 1 0 
# 0 1 0 1 0 1 0 1 0 1 
# 1 0 1 0 1 0 1 0 1 0 
# 0 1 0 1 0 1 0 1 0 1 
# 1 0 1 0 1 0 1 0 1 0 
# 0 1 0 1 0 1 0 1 0 1 
# 1 0 1 0 1 0 1 0 1 0 
# 0 1 0 1 0 1 0 1 0 1

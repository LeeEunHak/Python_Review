# 순차 탐색 알고리즘을 구현해보자.

def linearSearch(aList, key):
    for i in range(len(aList)):
        if key == aList[i]:
            return i
    return -1

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# 예시
position = linearSearch(numbers, 80)

if position != -1:
    print("탐색 성공 위치 = ", position)
else:
    print("탐색 실패")

# 출력 결과
# 탐색 성공 위치 = 7

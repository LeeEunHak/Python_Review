# 함수의 튜플 반환 예제

# 파이썬에서 함수가 튜플을 반환하게 하면 함수가 여러개의 값을 동시에 반환할 수 있다.
# 원의 넓이와 둘레를 동시에 반환하는 함수를 작성하고 출력해보자.

import math

def calCircle(r):
    area = math.pi * r * r
    circum = 2 * math.pi * r
    return (area, circum)

radius = float(input("원의 반지름을 입력하시오: "))
(a, c) = calCircle(radius)
print("원의 넓이는 " + str(a) + "이고 원의 둘레는 " + str(c) + "이다.")

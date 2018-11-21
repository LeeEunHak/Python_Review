# 사용자로부터 두 개의 점(x,y)를 입력받고 각 점을 지나는
# 직선의 기울기와 y절편을 반환하는 함수를 작성해보자.

# 파이썬은 여러개의 값을 반환할 수 있다.

def get_line(x1, y1, x2, y2):
    if (x1 == x2):
        return 0,0
    else:
        slope = (float)(y2 - y1) / (float)(x2- x1)
        yintercept = y1 - slope*x1
        return slope, yintercept  # 2개의 값을 반환

x1 = int(input("x1="))
y1 = int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))

slope, yintercept = get_line(x1, y1, x2, y2)  # 반환된 값을 풀어서 변수에 저장
print("기울기=", slope, "y절편=", yintercept)

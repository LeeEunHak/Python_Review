# 전역변수 사용해보기
# 상수를 정의할 때는 전역변수를 사용하는 것이 좋다.

PI = 3.141592

def main():
    radius = float(input("원의 반지름을 입력하세요: "))
    print("원의 면적:", circleArea(radius))
    print("원의 둘레:", circleCircumference(radius))

def circleArea(radius):
    return PI*radius*radius

def circleCircumference(radius):
    return 2*PI*radius

main()

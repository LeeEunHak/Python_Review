#사용자로부터 사각형의 가로와 세로를 입력받아 면적을 계산해주는 프로그램을 작성해보자.
#만약 길이값으로 양이 아닌 수를 적었을 때 '양수만 입력하시오: '라고 되묻고 다시 값을 입력 받는다.

def area(w,h):
    return w*h

def input_pos(msg):
    value = int(input(msg))
    while value <= 0:
        value = int(input("양수만 입력하시오: "))
    return value

width = input_pos("사각형의 가로: ")
height = input_pos("사각형의 세로: ")

print("면적=", area(width,height))

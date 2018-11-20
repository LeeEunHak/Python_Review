#섭씨 온도를 화씨 온도로, 또 그 반대로 변환하는 프로그램을 작성해보자.
#메뉴에서 종료(q)를 선택할 때까지 프로그램은 계속 반복된다.

def printOptions():
    print( " 'c' 섭씨온도에서 화씨온도로 변환")
    print( " 'f' 화씨온도에서 섭씨온도로 변환")
    print( " 'q' 종료")

def C2F(c_temp):
    return 9.0 / 5.0 * c_temp + 32

def F2C(f_temp):
    return (f_temp - 32) * 5.0 / 9.0

printOptions()
choice = input("메뉴에서 선택하세요.")
while choice != 'q':
    if (choice == 'c'):
        temp = float(input("섭씨온도: "))
        print("화씨온도:", C2F(temp)) 
    elif (choice == 'f'):
        temp = float(input("화씨온도: "))
        print("섭씨온도:", F2C(temp)) 
    printOptions()
    choice = input("메뉴에서 선택하세요.")

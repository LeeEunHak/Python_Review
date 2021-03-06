# 매개변수의 값을 함수 안에서 변경해보기
# 함수가 외부로부터 값을 전달받는데 사용하는 매개변수도 일졸의 지역 변수이다.

def sub(mylist):
    mylist = [1, 2, 3, 4]  # 새로운 리스트가 매개변수로 할당
    print("함수 내부에서의 mylist: ", mylist)
    return

mylist = [10, 20, 30, 40]
sub(mylist)
print("함수 외부에서의 mylist: ", mylist)

# 실행결과

# 함수 내부에서의 mylist: [1, 2, 3, 4]
# 함수 외부에서의 mylist: [10, 20, 30, 40]

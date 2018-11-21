# 매개변수의 값을 함수 안에서 변경해보기

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

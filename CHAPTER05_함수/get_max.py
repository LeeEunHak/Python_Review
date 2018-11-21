#두 개의 정수가 주어지면 두 수 중에서 더 큰 수를 찾아서 이것을 반환하는 함수

def get_max(x,y):
    if (x > y ):
        return x
    else:
        return y

#예시 
print(get_max(10,20))

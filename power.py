#정수의 거듭제곱값(x의 y승)을 계산하여 반환하는 함수

def power(x,y):
    result = 1
    for i in range(y):
        result = result * x
    return result

#예시
print(power(10,2))

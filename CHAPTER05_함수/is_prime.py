#사용자가 입력한 정수가 소수인지 아닌지 판별해주는 함수

def is_prime(n):
    for i in range(2,n):
        if (n%i == 0):
            return False
    return True

n = int(input("정수를 입력하세요: "))
print(is_prime(n))

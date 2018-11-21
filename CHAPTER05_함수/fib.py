# 피보나치 수열 모듈 만들어보기

def fib(n):
    a,b = 0,1
    while (b < n):
        print(b, end=" ")
        a,b = b,a+b

# 예시
fib(500)

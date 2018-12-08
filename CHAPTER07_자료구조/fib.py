# 피보나치 수열

# 앞의 두 개의 숫자를 더해서 뒤의 숫자를 만드는 개념이다.

table = {0:0, 1:1}

def fib(n):
    if n not in table:
        value = fib(n-1) + fib(n-2)
        table[n] = value
    return table[n]

# 예시
print(fib(100))

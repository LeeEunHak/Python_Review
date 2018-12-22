# n팩토리얼을 재귀함수로 표현

# 팩토리얼은 1부터 n까지 숫자를 차례대로 곱한 값이다.

def myfact(n):
    if ( n == 0 ):              # n이 0일 때
        return 1                # 1을 반환하고 재귀호출을 끝냄
    else:
        return n * myfact(n-1)  # n과 myfact함수에 (n-1)을 넣어서 반환된 값을 곱함


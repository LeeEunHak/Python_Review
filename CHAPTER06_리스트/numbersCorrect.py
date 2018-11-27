# 조건에 맞는 항목 찾기
# 공백 리스트를 만들고 요소가 발견될 때마다 추가하는 방식

# 리스트에서 50이 넘는 숫자들을 모두 찾는 코드를 작성해보자.

numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
result = []

for value in numbers:
    if value > 50:
        result.append(value)

print(result)

# 출력 결과
# [60, 70, 80, 90]

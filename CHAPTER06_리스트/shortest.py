# 문자열이 저장된 리스트를 가정하자.
# 길이가 가장 짧은 문자열을 찾는 코드를 작성해보자.

words = ["cat", "mouse", "tiger", "lion"]
shortest = words[0]

for i in range(1, len(shortest)):
    if len(words[i]) < len(shortest):
        shortest = words[i]

print("가장 짧은 단어는", shortest, "이다")

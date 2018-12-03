# 파일에서 중복되지 않은 단어의 개수 세기

# 텍스트 파일을 읽어서 단어를 얼마다 다양하게 사용하여 문서를 작성하였는지
# 계산하는 프로그램을 작성해보자. 중복된 단어는 하나만 인정한다.

# proverbs.txt
# All's well that ends well.
# Bad news travles fast.
# Well begun is half done.
# Birds of a feather flock together.

# 단어에서 구두점을 제거하고 소문자로 만든다.
def process(w):
    output = ""
    for ch in w:
        if(ch.isalpha()):
            output += ch
    return output.lower()

words = set()

# 파일을 연다.
fname = input("입력 파일 이름: ")
file = open(fname, "r")

# 파일의 모든 줄에 대하여 반복한다.
for line in file:
    linewords = line.split()
    for word in linewords:
        words.add(process(word)) # 단어를 세트에 추가한다.

print("사용된 단어의 개수=", len(words))
print(words)

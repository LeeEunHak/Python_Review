# 간단한 영한 사전 만들기

# 공백 딕셔너리를 생성하고 여기에 영어 단어를 키로하고 설명을 값으로 저장

english_dict = dict()

english_dict['one'] = "하나"
english_dict['two'] = "둘"
english_dict['three'] = "셋"

word = input("영어단어를 입력하세요: ")
print(english_dict.get(word, "없음"))

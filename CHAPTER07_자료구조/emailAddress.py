# 이메일 주소 분석

# 이메일의 아이디와 도메인을 구분하는 프로그램을 작성해보자.

address = input("이메일 주소를 입력하세요: ")

(id, domain) = address.split("@")

print(address)
print('아이디: ' + id)
print('도메인: ' + domain)

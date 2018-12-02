# 파티 동시 참석자 알아내기

# 파티에 참석한 사람들의 명단이 세트 A와 B에 각각 저장되어 있다.
# 2개의 파티에 모두 참석한 사람들의 명단을 출력하는 프로그램을 작성해보자.

partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("2개의 파티에 모두 참석한 사람은 다음과 같습니다. ")
print(partyA.intersection(partyB))

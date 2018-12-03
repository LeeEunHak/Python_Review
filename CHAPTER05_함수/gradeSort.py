# 성적을 사용자로부터 읽어서 크기순으로 정렬하여서 화면에 출력하는
# 프로그램을 작성해보자. 사용자가 음수를 입력하면 입력을 종료한다.

def readList():
    nlist = []
    flag = True;
    while flag:
        number = int(input("숫자를 입력하시오: "))
        if number < 0:
            flag = False
        else:
            nlist.append(number)
    return nlist

def processList(nlist):
    nlist.sort()
    return nlist

def printList(nlist):
    for i in nlist:
        print("성적=", i)

def main():
    nlist = readList()
    processList(nlist)
    printList(nlist)

if __name__ == "__main__":
    main()

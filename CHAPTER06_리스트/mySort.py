# 선택 정렬을 구현하는 함수

def selectionSort(alist):
    for i in range(len(alist)):
        least=i                           # i를 최솟값으로 간주
        leastValue=alist[i]               
        for k in range(i+1, len(alist)):  # (i+1)번부터 비교하기
            if alist[k] < leastValue:     # k번째 요소가 현재의 최솟값보다 작으면
                least=k                   # k번째 요소를 최솟값으로 한다.
                leastValue=alist[k]

        alist[i],alist[least]=alist[least],alist[i]  # i번째 요소와 최솟값을 교환

if __name__=="__main__":
    list1=[7, 9, 5, 1, 8]
    selectionSort(list1)
    print(list1)


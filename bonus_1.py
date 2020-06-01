# 보너스 문제
# 1. 자연수로 구성된 수열 ex) 1,2,3,2,5
# 2. 합이 5인 부분 연속 수열의 개수 구하기

def solution(arr1):
    count = 0
    for i in range(len(arr1)):
        if arr1[i] == 5:
            count+=1
        elif arr1[i]+arr1[i+1] == 5:
            count+=1
    print(count)
    return count
solution([1,2,3,2,5])
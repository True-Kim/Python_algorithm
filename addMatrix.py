def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        answer.append([x+y for x,y in zip(arr1[i],arr2[i])])
    print(answer)
    return answer

solution([[1,2],[2,3]],[[3,4],[5,6]])
solution([[1],[2]],[[3],[4]])
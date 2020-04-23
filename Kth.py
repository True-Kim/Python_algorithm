# 문제풀이
# 1. 배열 array를 자르고 k번째 값 구하려면 i,j,k값 필요
# 2. commands에서 i값, j값, k값을 찾음
# 3. array[i:j]를 자른값을 정렬
# 4. 자른array의 k번째 값을 answer에 넣기
# 5. answer return
#
# 관건
# 1. 인덱스는 0부터 시작
# 2. array는 바뀌면 안되니까 새로운 배열에 넣기.

def solution(array, commands):
    answer = []
    newArray=[]
    for x in range(len(commands)):
        i=commands[x][0]
        j=commands[x][1]
        k=commands[x][2]
        newArray=array[i-1:j]
        newArray.sort()
        answer.append(newArray[k-1])
    print(answer)
    return answer

solution([1,5,2,6,3,7,4],[[2,5,3],[4,4,1],[1,7,3]])
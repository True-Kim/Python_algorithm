# 풀이
# 1. strings 안의 문자열의 n번째 인덱스를 찾아 index에 저장
# 2. index의 값과 strings안의 문자열 n번째 값이 같으면 answer배열에 넣기
#
# 관건
# 1. for문에서 j와 i를 비교하냐 vs i와 j를 비교하냐?
# 2. 사전순으로 정렬이 안됨..ㅠ > 초반에 strings를 sort()로 정렬하고 시작하면 됨.

def solution(strings, n):
    answer = []
    index = []
    strings.sort()
    for i in range(len(strings)):
        index.append(strings[i][n])
    set_index=set(index)
    list_index=list(set_index)
    list_index.sort()
    print(list_index)

    for j in range(len(list_index)):
        for i in range(len(strings)):
            if list_index[j] is strings[i][n]:
                answer.append(strings[i])
    print(answer)
    return answer

solution(["sun", "bed", "car"],1)
solution(["abce", "abcd", "cdx"],2)
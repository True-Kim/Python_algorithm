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
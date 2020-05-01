def solution(strings, n):
    answer = []
    index = []
    index2 = []
    for i in range(len(strings)):
        index.append(strings[i][n])
        index2=sorted(set(index))
        print(index2)
        for j in range(len(index2)):
            if index2[j]==strings[i][n]:
                answer.append(strings[i])
    print(answer)
    return answer

solution(["sun", "bed", "car"], 1)
solution(["abce", "abcd", "cdx"], 2)


# ["hello", "hi", "python"]
print(sorted(['hello','hi', 'python'],key=lambda x:x[1]))
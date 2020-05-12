# 풀이
# 1. arr1과 arr2를 2진수로 변환
# 2. arr1과 arr2의 값을 각각 더하기
# 3. 더한 값이 1 or 2일 때, '#'넣고, 0일때 '공백'넣기
# 4. 배열로 출력

def solution(n, arr1, arr2):
    answer = []
    arr_1 = []
    arr_2 = []
    b_arr = []

    # 각 배열을 2진수로 바꿔주기
    for i in range(len(arr1)):
        arr_1.append(format(arr1[i],'b'))
        arr_2.append(format(arr2[i],'b'))

    arr_1 = [int(x) for x in arr_1] # int형으로 바꾸기
    arr_2 = [int(x) for x in arr_2]

    b_arr=list(zip(arr_1,arr_2))

    # 더하기
    for j in range(len(b_arr)):
        answer.append(sum(b_arr[j]))

    # '#, 공백'으로 바꾸기
    answer = [str(x) for x in answer]
    print(answer)
    for a in range(len(answer)):
        answer[a] = answer[a].zfill(n) # answer[a]의 앞쪽에 answer[a]가 n의 길이만큼 채워지도록 0을 넣어주겠다는 뜻
        answer[a] = answer[a].replace('0', ' ')
        answer[a] = answer[a].replace('1', '#')
        answer[a] = answer[a].replace('2', '#')
    print(answer)
    return answer

#!오류! 2진수의 길이가 n의 길이보다 짧을 때!
# ex) 11220 => 011220
# ex) 12221 => 012221
# answer[a] = answer[a].zfill(n) 넣었더니 됨...

# solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
# ['12111', '10101', '21201', '20011', '12111']
# ['#####', '# # #', '### #', '#  ##', '#####']

# solution(6,[46, 33, 33 ,22, 31, 50],[27 ,56, 19, 14, 14, 10])
# ['112121', '211001', '110012', '11220', '12221', '111020']
# ['######', '###  #', '##  ##', ' #### ', ' #####', '### # ']
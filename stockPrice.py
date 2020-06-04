# 문제설명
# 1. return 값 : 가격이 떨어지지 않은 총 기간
# 2. prices는 초단위로 기록
# 3. prices가 [1,2,3,2,3] 이라는 것은 0초:1, 1초:2, 2초:3, 3초:2, 4초:3 기록
# 4. 1초의 1은 2, 3, 2, 3 보다 작으므로, 4초 뒤에도 가격이 1보다는 떨어지지 않음.
# 5. 2초의 2는 3, 2, 3 보다 작거나 같으므로, 3초 뒤에도 가격이 떨어지지 않음.
# 6. !! 주의 !! 3초의 3은 2보다 크므로, 1초뒤에 가격이 떨어지므로, 1초간 가격이 떨어지지 않음.
# 7. !! 주의 !! 마지막은 0초

# 풀이 1
# 1. 뒤의 수가 앞의 수보다 크거나 같거나 작은경우 +1
# 2. answer에 append

# def solution(prices):
#     answer = []
#     second = {}
#     # 1. 딕셔너리 만들기
#     for sec, pri in enumerate(prices):
#         second[sec]=pri #{0: 1, 1: 2, 2: 3, 3: 2, 4: 3}
#     print(second)
#
#     for sec in second:
#         if second[sec]-second[0] >= 0:
#             print(second[sec]-second[0])

    # while prices:
    #     for j in range(1, len(prices)):
    #         if prices[j]-prices[0] > 0 :
    #             print(second[j]-second[0])
    #         # elif prices[j]-prices[0] < 0 :
    #
    #         elif len(prices)==1:
    #             answer.append(0)
    #     prices.pop(0)
    #     answer.append(count)
    #     count = 0
    # return answer
# solution([1, 2, 3, 2, 3]) #[4, 3, 1, 1, 0]
# solution([1, 2, 3, 2, 3, 1]) #[5, 4, 1, 2, 1, 0]
# solution([3,1]) #[1,0]

# 풀이 2
def solution(prices):
    answer = [0] * len(prices)

    for i in range(len(prices)):
        for j in range(i, len(prices) - 1):
            if prices[i] > prices[j]:
                break
            else:
                answer[i] += 1
    print(answer)
    return answer
solution([1,2,3,2,3]) #[4, 3, 1, 1, 0]
solution([1, 2, 3, 2, 3, 1]) #[5, 4, 1, 2, 1, 0]
solution([3,1]) #[1,0]


def solution(d, budget):
    answer = 0
    sd = sorted(d)
    for i in range(len(sd)):
        if budget-sd[i]>=0:
            answer+=1
            budget=budget-sd[i]
    return answer
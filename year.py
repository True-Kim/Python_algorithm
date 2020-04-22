def solution(a, b):
    answer = 'FRI,SAT,SUN,MON,TUE,WED,THU'
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if a<=12:
        n = a
        sum_day = sum(days[0:n-1])+b
        numb = sum_day%7
    print(answer.split(",")[numb-1])
    return answer.split(",")[numb-1]

solution(5,24)
solution(1,1)

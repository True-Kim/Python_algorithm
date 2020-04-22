def solution(n):
    answer = '수박'
    if n<=10000:
        if n%2==0:
            answer = answer*(n//2)
        elif n%2!=0:
            answer = answer*(n//2)+answer[0]
    print(answer)
    return(answer)
solution(3)
solution(15)


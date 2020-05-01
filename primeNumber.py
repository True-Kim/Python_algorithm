def solution(n):
    primes=[]
    numbers=[]
    for prime in range(1,n+1,2): # 1, 3, 5, 7, 9 / 1, 3, 5
        primes.append(prime)
    for number in primes: # 1 ~ 9 / 1~5
        numbers.append(number)
    if prime>number and prime%number==0:
            primes.pop(prime) # primes에서 나누어 떨어지는 수 제거
    if n%2==0:
        return len(primes)-1
    if n%2!=0:
        return len(primes)
solution(5)


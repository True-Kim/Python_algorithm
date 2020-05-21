# 풀이
# 1. 알파벳을 n거리만큼 밀기 -> 알파벳+n
# 2. ASKII code로 변환 : ord(), chr()
# 3. 대문자(65~90), 소문자(97~122)
# 4. 주의! 알파벳+n이 90보다 클 때는 ords[i]+n-26, 122보다 클 때는 ords[i]+n-26가 됨.
# 5. 주의! 입력값에 공백있음 -> 공백 = 32번

def solution(s, n):
    answer = ''
    ords = []
    for i in range(len(s)):
        ords.append(ord(s[i]))
        # ords[i]가 대문자일 때,
        if ords[i]>=65 and ords[i]<=90 and ords[i]!=32:
            if ords[i]+n>90:
                answer=answer+chr(ords[i]+n-26)
            else :
                answer=answer+chr(ords[i]+n)
        # ords[i]가 소문자일 때,
        elif ords[i]>=97 and ords[i]<=122 and ords[i]!=32:
            if ords[i]+n>122:
                answer=answer+chr(ords[i]+n-26)
            else :
                answer=answer+chr(ords[i]+n)
        # ords[i]가 32일 때,
        elif ords[i]==32:
            answer=answer+' '
    print(answer)
    return answer

solution("AB", 1) #BC
solution("z", 1) #a
solution("a B z", 4) #e F d
solution("y",3) #b


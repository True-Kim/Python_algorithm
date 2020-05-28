# 풀이
# 1. 별 문자를 이용해 가로길이가 n, 세로 길이가 m인 직사각형 형태 출력하기
# 2. = a개씩 b번 출력

a, b = map(int, input().strip().split(' '))
rec_star=('*'*a+'\n')*b
print(rec_star)

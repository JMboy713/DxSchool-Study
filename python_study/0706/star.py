# 공백의 갯수.
# 공백의 사이사이에 별을 넣자
# 4*4
# 3*1*3
# 2*3*2
# 1*5*1
# 0 0 0
n = int(input())


for i in range(n//2, -1, -1):
    if i == n//2:
        print(' '*(n//2), end='')
        print('*', end='')
        print(' '*(n//2))
    elif i == 0:
        print('*'*n)
    else:
        print(' '*i, end='')
        print('*', end='')
        print(' '*(9-2*(i+1)), end='')
        print('*', end='')
        print(' '*i)

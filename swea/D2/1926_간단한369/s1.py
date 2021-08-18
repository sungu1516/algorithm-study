import sys
sys.stdin = open("input.txt", "r")

clap = ['3', '6', '9']
N = int(input())
for num in range(1, N+1):
    cnt = 0
    for unit in str(num):
        if unit in clap:
            cnt += 1
    if cnt:
        print('-' * cnt, end=' ')
    else:
        print(num, end=' ')
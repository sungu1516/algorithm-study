import sys
sys.stdin = open("input.txt", "r")

def perm(v):
    if v == N:
        print(arr)
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                arr[i] = numbers[i]
                perm(i+1)
                visited[i] = 0

T = int(input())
for tc in range(1, T + 1):
    numbers, repet = input().split() # 숫자판, 교환횟수
    numbers, repet = list(map(int, numbers)), int(repet) # 목적에 맞게 형변환
    N = len(numbers) # 이후 몇번 사용되므로 변수로
    visited = [0] * N
    arr = [0] * N

    perm(0)
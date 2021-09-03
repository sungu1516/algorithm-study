import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())    # 문제의 개수
    scores = list(map(int, input().split()))
    total = [0]
    visited = [0] * (sum(scores) + 1)

    for i in range(len(scores)):
        for j in range(len(total)):
            temp = scores[i] + total[j]     # 임시 변수 - 부분합
            if not visited[temp]:
                visited[temp] = 1
                total.append(temp) 

    print(f'#{tc} {len(total)}')
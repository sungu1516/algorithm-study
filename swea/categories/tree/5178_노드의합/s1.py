import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    bin_tree = [0] * (N+1) # tree 초기화

    for _ in range(M):  # 리프노드 입력받기
        idx, val = map(int, input().split())
        bin_tree[idx] = val

    # 나머지 노드값 채워주기 - 뒤에서부터 출발
    for i in range(N, 2, -2):
        if i % 2 == 0:  # 마지막 인덱스가 짝수라면
            if i + 1 >= N + 1:   # 짝수인 경우, 형제 노드가 없는 경우라면
                bin_tree[i//2] = bin_tree[i]
            else:
                bin_tree[i // 2] = bin_tree[i] + bin_tree[i+1]
        else:   # 홀수인 경우 - 무조건 형제 노드가 존재
            bin_tree[i//2] = bin_tree[i] + bin_tree[i-1]

    print(f'#{tc} {bin_tree[L]}')
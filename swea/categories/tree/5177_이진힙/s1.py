import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    bin_tree = [0] * (N+1)  # 이진트리 초기화

    for i in range(1, N+1):
        bin_tree[i] = arr[i-1]  # arr의 숫자들을 순서대로 삽입

        while i > 0:   # 부모노드와 크기를 비교하여 자리를 바꿔준다.
            if bin_tree[i] < bin_tree[i//2]:
                bin_tree[i], bin_tree[i//2] = bin_tree[i//2], bin_tree[i]
                i = i // 2
                continue
            break

    total = 0
    idx = N // 2
    while idx > 0:
        total += bin_tree[idx]
        idx //= 2
    print(f'#{tc} {total}')



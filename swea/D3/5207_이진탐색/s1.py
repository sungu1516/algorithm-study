import sys
sys.stdin = open('input.txt')

def is_bidirect(arr, target):
    left = 0
    right = 0

    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2

        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            start = mid + 1
            left += 1
            curr = 'R'
        else:
            end = mid - 1
            right += 1
            curr = "L"

        if abs(left-right) > 2:
            return False

    return False

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    cnt = 0
    for target in B:
        if is_bidirect(A, target):
            cnt += 1

    print('#{} {}'.format(tc, cnt))



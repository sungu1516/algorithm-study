import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 함수 정의
def cal_bore(arr):
    global total

    if len(arr) == 2:
        total += abs(arr[0] - arr[1])
        return arr[0] if arr[0] > arr[1] else arr[1]
    else:
        group1 = arr[:len(arr)//2]
        group2 = arr[len(arr)//2:]
        return cal_bore([cal_bore(group1), cal_bore(group2)])

T = int(input())
for tc in range(1, T + 1):
    K = int(input())
    arr = list(map(int, input().split()))    # 각 사람의 코딩 실력
    total = 0
    cal_bore(arr)
    print('#{} {}'.format(tc, total))
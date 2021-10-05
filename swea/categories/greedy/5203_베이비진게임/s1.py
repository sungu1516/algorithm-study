import sys
sys.stdin = open('input.txt', 'r')

# run or triplet 을 확인하는 함수
def is_rort(arr):
    for i in range(10):
        # run
        if arr[i-2] and arr[i-1] and arr[i]:
            return True
        # triplet
        if arr[i] >= 3:
            return True
    return False

T = int(input())
for tc in range(1, T+1):
    # 전체 카드
    cards = list(map(int, input().split()))
    # counting arr
    p1 = [0] * 10
    p2 = [0] * 10
    # 결과 (무승부로 초기화)
    ans = 0

    # 카드를 번갈아가며 counting sort
    for i in range(12):
        card = cards[i]
        if i % 2 == 0:
            p1[card] += 1
        else:
            p2[card] += 1

        # run or triplet 확인
        if i < 4: continue    # 갖고있는 카드가 3장 이하인 경우 skip
        r1 = is_rort(p1)     # counting 배열을 넣어준다.
        r2 = is_rort(p2)

        # 승부 확인
        if r1 and not r2:
            ans = 1
            break
        elif r2 and not r1:
            ans = 2
            break
        elif r1 and r2: # 무승부
            break

    print('#{} {}'.format(tc, ans))
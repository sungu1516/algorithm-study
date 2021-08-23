import sys
sys.stdin = open('input.txt')

# 필요 함수 정의
def count_search(total_page, key):
    cnt = 1
    start = 1
    end = total_page
    while start <= end:
        middle = (start+end) // 2
        if middle == key:
            break
        elif middle > key:
            end = middle
        else:
            start = middle
        cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    P, A, B = map(int, input().split())
    result = 'A' if count_search(P, A) < count_search(P, B) else 'B' if count_search(P, A) > count_search(P, B) else 0
    print('#{} {}'.format(tc, result))
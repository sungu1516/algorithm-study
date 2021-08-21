import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    height = list(map(int, input().split()))
    # 높이 변화량이 담긴 리스트 생성 - 양수: 점프 / 음수: 뛰어내리기
    changes = []
    for i in range(1, len(height)):
        changes.append(height[i] - height[i-1])
    # 최댓값, 최소값을 출력 - 난이도 의미
    max_val = 0
    min_val = 0 # 만약 올라가는 부분이나 내려가는 부분이 없을 경우 0을 출력하기 위해 0으로 초기화해준다.
    for change in changes:
        if max_val < change:
            max_val = change
        if min_val > change:
            min_val = change
    print('#{} {} {}'.format(tc, max_val, abs(min_val)))
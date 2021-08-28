import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 함수 정의
def get_dominant(area):
    colors = ['white', 'blue', 'red']
    cnt = [0] * 3

    for i in range(len(area)):
        for j in range(M):
            if area[i][j] == 'W':
                cnt[0] += 1
            elif area[i][j] == 'B':
                cnt[1] += 1
            else:
                cnt[1] += 1

    # 최댓값?
    max_idx = 0
    for i in range(1, 3):
        if cnt[max_idx] < cnt[i]:
            max_idx = i

    return colors[i]

T = int(input())
for _ in range(1, T + 1):
    N, M = map(int, input().split())    # N = 줄(칸) 수, M = 문자열의 길이
    arr = [input() for _ in range(N)]

    # 첫째 줄과 마지막줄을 제외한 부분에서, 가장 많이 칠해진 색을 구한다.
    dom_color = get_dominant(arr[1:-1])     # 첫 줄, 마지막 줄을 제외한 영역을 인자값으로 넣는다.

    # 위의 결과를 바탕으로, 각 영역을 칠할 색을 결정한다.
    print(dom_color)


    # 반복문, 조건문을 이용해 새로칠해야 하는 칸의 최소 개수를 구한다.
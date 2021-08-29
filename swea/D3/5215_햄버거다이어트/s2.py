import sys
sys.stdin = open('input.txt')

# 함수정의 - 재료정보가 담긴 배열을 인자로 넣었을 때, 총 칼로리를 리턴
def get_cal(arr):
    total = 0
    for elem in arr:
        total += elem[1]
    return total

# 함수정의 - 재료정보가 담긴 배열을 인자로 넣었을 때, 총 만족도를 리턴
def get_sat(arr):
    total = 0
    for elem in arr:
        total += elem[0]
    return total

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())    # 재료의 수, 제한 칼로리
    # 재료별 만족도와 칼로리 받아 배열로 저장
    ingres = []
    for _ in range(N):
        ingres.append(tuple(map(int, input().split())))

    # 모든 재료조합 중 칼로리가 1000인 조합만 출력해보기
    max_val = 0
    for i in range(1<<N):
        temp = []
        for j in range(N+1):
            if i & (1<<j):
                if (get_cal(temp) + ingres[j][1]) >= L:
                    break
                temp.append(ingres[j])

        if get_sat(temp) > max_val:
            max_val = get_sat(temp)

    print('#{} {}'.format(tc, max_val))

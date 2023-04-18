# 입력값 받기

n = int(input())
work_arr = [list(map(int, input().split())) for _ in range(n)]
# visited = [0] * (n + 1)

def dfs(idx, price_sum):
    global max_val

    time = work_arr[idx][0]     # 상담 소요일
    price = work_arr[idx][1]    # 상담 이득

    # 이득 합계
    if idx + time <= n + 1:
        price_sum += price

    # 1-2. 마지막 날일 경우
    if idx + time >= n + 1:
        if price_sum > max_val:
            max_val = price_sum
        return

    # 재귀 방문
    for i in range(idx + time, len(work_arr)):
        dfs(i, price_sum)

# index 처리를 간편하게
work_arr.insert(0, [])
max_val = 0

# 모든 일자를 시작일자로 탐색
for i in range(1, len(work_arr)):
    dfs(i, 0)

# 얻을 수 있는 최대 이익 출력
print(max_val)
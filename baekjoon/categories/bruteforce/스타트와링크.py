# func
def dfs(cnt, idx):
    global min_val
    # 종료조건
    if cnt == n//2:
        # 차이를 구한다.
        power1, power2 = 0, 0
        for i in range(n):
            for j in range(n):
                if selected[i] and selected[j]:
                    power1 += graph[i][j]
                elif not selected[i] and not selected[j]:
                    power2 += graph[i][j]

        # 팀 능력치 차이의 최소값을 구한다.
        min_val = min(min_val, abs(power1 - power2))
        return

    # 재귀 호출 경우 - team 구분
    for i in range(idx, n):
        if not selected[i]:
            selected[i] = 1
            dfs(cnt + 1, i + 1)
            selected[i] = 0

# input
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# main
min_val = 999999999 # 최소값 초기화
selected = [0 for _ in range(n)]    # 팀 구분을 위한 배열

dfs(0, 0)   # 재귀 함수 실행  dfs(선택한 사람, 사람의 idx)
print(min_val)
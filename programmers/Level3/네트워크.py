def solution(n, computers):
    answer = 0

    # dfs 함수 정의
    def dfs(graph, v, visited):
        # 방문처리
        visited[v] = 1
        # 근접 노드 방문
        for i in range(n):
            # 근접노드이면서 방문하지 않은 경우
            if graph[v][i] == 1 and not visited[i]:
                # 재귀적 방문
                dfs(graph, i, visited)

    visited = [0] * n
    for i in range(n):
        if visited[i] == 0:환
            # dfs 실행하여 방문처리
            dfs(computers, i, visited)
            answer += 1

    return answer
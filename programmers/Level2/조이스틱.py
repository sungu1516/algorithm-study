def solution(name):
    name_list = list(name)
    min_cnt = len(name) - 1  # 최소 이동 횟수 초기화

    def dfs(name_list, idx, cnt):
        nonlocal min_cnt

        if idx >= len(name_list): return

        # 방문처리
        new_name_list = name_list[:]
        new_name_list[idx] = 'A'

        # 종료 조건
        if name_list.count('A') == len(name):
            if cnt < min_cnt:
                min_cnt = cnt
            return

        # 분기처리
        dfs(new_name_list, idx + 1, cnt + 1)

        dfs(new_name_list, idx - 1, cnt + 1)
        # 방문처리 원상복구

    dfs(name_list, 0, 0)

    return min_cnt

print(solution("JEROEN"))
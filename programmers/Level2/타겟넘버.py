def solution(numbers, target):
    answer = 0

    # DFS 정의
    def dfs(total, idx):

        # 만약 배열 내 모든 수를 사용한 경우
        if idx == len(numbers):
            nonlocal answer
            # target 넘버와 비교
            if total == target:
                answer += 1
            return

        # 현재 인덱스의 수를 -
        dfs(total - numbers[idx], idx + 1)

        # +
        dfs(total + numbers[idx], idx + 1)

    dfs(0, 0)

    return answer

print(solution([1, 1, 1, 1, 1], 3))
# input
n = int(input())
symbols = input().split()


# func
def check(num1, num2, symbol):
    if symbol == '<':
        if num1 > num2:
            return False
    else:
        if num1 < num2:
            return False
    return True


def dfs(depth, num):
    # 종료조건
    if depth == n + 1:
        ans.append(num)
        return

    # 재귀 호출
    for i in range(10):
        if not visited[i] and (depth == 0 or check(num[depth - 1], str(i), symbols[depth - 1])):
            visited[i] = 1
            dfs(depth + 1, num + str(i))
            visited[i] = 0


# main
visited = [0 for _ in range(10)]  # 선택한 숫자를 기록
ans = []  # 조건을 만족하는 숫자를 담을 배열

dfs(0, '')
ans.sort()
print(ans[-1])
print(ans[0])

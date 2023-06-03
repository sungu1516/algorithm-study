# input
cases = []
t = int(input())
for _ in range(t):
    cases.append(int(input()))

# func
def go(sum, n):
    # 종료조건1 - 답을 더이상 구할 수 없는 경우
    if sum > n:
        return 0
    # 종료조건2 - 답을 찾은 경우
    if sum == n:
        return 1

    cnt = 0
    for i in range(1, 4):
        cnt += go(sum + i, n)

    return cnt

# main
for case in cases:
    print(go(0, case))
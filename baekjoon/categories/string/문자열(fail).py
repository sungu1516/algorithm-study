# 입력값
a, b = input().split()

# 두 문자열의 차이를 구하는 함수
def get_diff(str1, str2):
    cnt = 0
    for i in range(len(str2)):
        if str1[i] != str2[i]:
            cnt += 1

    return cnt

# dfs 함수 정의
def dfs(str1, str2):
    global min_val
    # 종료조견
    if len(str1) == len(str2):
        # 최소값 갱신
        val = get_diff(str1, str2)
        if val < min_val:
            min_val = val

        return

    # 기준 집합 내 모든 알파벳이 추가되는 경우의 수를 탐색
    for alpha in std_alpha:
        # left or right 재귀 탐색
        dfs(str1 + alpha, str2)
        dfs(alpha + str1, str2)


# main
a_len = len(a)
b_len = len(b)
min_val = b_len # 최소값 초기화
std_alpha = set(b)  # 탐색의 기준이 되는 알파벳 집합

dfs(a, b)

print(min_val)
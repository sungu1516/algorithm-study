import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 함수 정의
def count_palindrome(word):
    cnt = 0
    for i in range(8-N+1):
        if word[i:i+N] == word[i:i+N][::-1]:
            cnt += 1
    return cnt

T = 10
for tc in range(1, T + 1):
    N = int(input())
    arr = [input() for _ in range(8)]
    ans = 0

    for i in range(8):
        # 가로
        ans += count_palindrome(arr[i])

        # 세로
        temp = ''
        for j in range(8):
            temp += arr[j][i]
        ans += count_palindrome(temp)

    print('#{} {}'.format(tc, ans))
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

# 고지식한 패턴 검색
def search(pattern, text):
    i = 0
    j = 0
    while j < len(pattern) and i < len(text):
        if text[i] != pattern[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == len(pattern):
        return 1
    else:
        return 0

for _ in range(1, T + 1):
    pattern = input()
    text = input()

    result = search(pattern, text)

    print('#{} {}'.format(_, result))




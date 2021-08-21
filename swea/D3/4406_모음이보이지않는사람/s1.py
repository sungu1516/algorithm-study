import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 모음
vowel = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc), end=' ')
    word = input()
    for chr in word:
        if chr not in vowel:
            print(chr, end='')
    print()
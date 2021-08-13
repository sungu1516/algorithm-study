import sys
sys.stdin = open('input.txt')

T = int(input())

for _ in range(1, T + 1):
    # 입력받은 다섯개의 단어들을 리스트에 담아주기 + list 로 변환
    words = [list(input()) for _ in range(5)]

    # 단어들 중 최대길이 구하기
    max_len = 0
    for word in words:
        if max_len < len(word):
            max_len = len(word)

    # 모든 단어 리스트를 순회하며, 최대길이를 가진 단어보다 짧은 단어들에 공백 추가해주기 for zip
    for word in words:
        if len(word) < max_len:
            word.extend(['']*(max_len - len(word)))

    # zip으로 처리해준 후 문자열로 이어붙이기
    result = list(map(lambda x: ''.join(x), list(zip(*words))))
    print('#{} {}'.format(_, ''.join(result)))


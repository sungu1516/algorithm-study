import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 특정 문자열에 대해 정해진 패턴의 크기만큼 탐색하여 회문이 존재한다면 회문의 길이 반환
def search(M, word):
    for i in range(0, 100 - M + 1):  # 문자열의 모든 부분을 패턴의 길이만큼 탐색
        if word[i:i + M] == word[i:i + M][::-1]:  # 회문 확인
            return M # 회문이라면 해당 회문의 길이 리턴
    return 1

T = 10

for _ in range(1, T + 1):
    tn = input() # 테스트 케이스 번호
    words = [input() for _ in range(100)] # 입력값으로 받은 문자열들을 리스트에 저장
    max_len = 1 # 최대 회문 길이 초기화

    # 가로탐색
    for word in words:
        i = max_len + 1  # 탐색 패턴길이 초기화
        while i <= 100:
            search_len = search(i, word)
            if max_len < search_len:
                max_len = search_len
                i = max_len + 1
            else:
                i += 1

    # 세로 탐색
    for my_tuple in zip(*words):
        new_word = ''.join(my_tuple)
        i = max_len + 1  # 탐색 패턴길이 초기화
        while i <= 100:
            search_len = search(i, new_word)
            if max_len < search_len:
                max_len = search_len
                i = max_len + 1
            else:
                i += 1

    print('#{} {}'.format(_, max_len))
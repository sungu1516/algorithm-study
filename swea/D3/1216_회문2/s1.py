import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 회문여부 확인 함수 - 입력받은 문자열이 회문이면 True, 아니면 False 반환
def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

# 특정 문자열에 대해 정해진 패턴의 크기만큼 탐색하여 회문이 존재한다면 회문을 반환하는 함수 정의
def search(M, word):
    for i in range(0, 100 - M + 1):  # 문자열의 모든 부분을 패턴의 길이만큼 탐색
        if is_palindrome(word[i:i + M]):  # 위에서 정의한 함수 호출
            return M # 회문이라면 해당 회문의 길이 리턴
    return 0

T = 10

for _ in range(1, T + 1):
    tn = input() # 테스트 케이스 번호
    words = [input() for _ in range(100)] # 입력값으로 받은 문자열들을 리스트에 저장
    max_len = 1 # 최대 회문 길이 초기화

    i = 2
    # 가로탐색
    for word in words:
        # 하나의 단어를 탐색 시작
         for i in range(2, 101): # 찾을 패턴의 길이를 2, 100 까지 설정한 후 탐색
            if max_len < search(i, word):
                max_len = search(i, word)

    # 세로 탐색
    for my_tuple in zip(*words):
        new_word = ''.join(my_tuple)
        for i in range(2, 101):
            if max_len < search(i, new_word):
                max_len = search(i, new_word)

    print('#{} {}'.format(_, max_len))
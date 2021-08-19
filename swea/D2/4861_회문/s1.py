import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

# 회문여부 확인 함수 - 입력받은 문자열이 회문이면 True, 아니면 False 반환
def palindrome(word):
    if len(word) < 2: # 종료조건: 문자열 길이가 1 or 0 일 때 회문이므로, True 리턴
        return True
    if word[0] != word[-1]:
        return False # 만약 양 끝의 글자가 같지 않다면 False 리턴
    return palindrome(word[1:-1]) # 양끝의 글자가 같다면 재귀함수 호출 (탐색범위 좁히기)

# 특정 문자열에 대해 정해진 패턴의 크기만큼 탐색하여 회문이 존재한다면 회문을 반환하는 함수 정의
def search(N, M, word):
    for i in range(0, N - M + 1):  # 문자열의 모든 부분을 패턴의 길이만큼 탐색
        if palindrome(word[i:i + M]):  # 위에서 정의한 함수 호출
            print('#{} {}'.format(_, word[i:i + M]))  # 만약 해당 부분이 회문이라면 출력

for _ in range(1, T + 1):
    N, M = map(int, input().split())
    words = [input() for _ in range(N)] # 입력값으로 받은 문자열들을 리스트에 저장

    # 가로탐색
    for word in words:
        search(N, M, word) # 모든 문자열을 순회하며, search 함수를 호출한다.

    # 세로 탐색
    for j in range(N):
        new_word = '' # 새로운 단어를 초기화
        for i in range(N):
            new_word += words[i][j] # 세로로 이동하며, 새로운 단어를 만들어준다.
        search(N, M, new_word)
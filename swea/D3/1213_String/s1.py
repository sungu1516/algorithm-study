import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = 10

def pattern_search(pattern, text):
    i = 0 # 전체 텍스트의 인덱스
    j = 0 # 찾고자 하는 pattern 의 인덱스
    cnt = 0 # text 내의 pattern 의 갯수

    while i < len(text):  # text 를 모두 탐색할 때까지 반복
        while j < len(pattern) and i < len(text):  # 일치하는 문자열이 있거나, text를 모두 탐색하는 경우 종료
            if text[i] != pattern[j]:  # 특정 위치의 글자가 다른 경우
                i -= j  # j와 비교했던 만큼 빼준다 (=처음 비교했던 위치로 이동)
                j = -1
            i += 1  # 처음 비교했던 위치에서 한칸 더 이동
            j += 1  # index = 0 에서부터 다시 시작

        if j == len(pattern):  # pattern 이 일치하여 반복문을 빠져나온 경우
            cnt += 1  # cnt ++
        j = 0  # pattern 의 인덱스를 0으로 초기화 = 1칸 이동하여 검색 재개

    return cnt

for _ in range(1, T + 1):
    N = input()

    pattern = input()
    text = input()

    print('#{} {}'.format(N, pattern_search(pattern, text)))




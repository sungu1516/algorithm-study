import sys
sys.stdin = open('input.txt', encoding='UTF-8')

# 필요함수 정의 - 고지식한 패턴 검색 활용
def min_typing(text, pattern):
    i = 0
    j = 0
    cnt = 0 # text 내의 pattern 의 갯수

    while i < len(text):  # text 를 모두 탐색할 때까지 반복
        while j < len(pattern) and i < len(text):  # 일치하는 문자열이 있거나, text를 모두 탐색하는 경우 종료
            if text[i] != pattern[j]:  # 특정 위치의 글자가 다른 경우
                i -= j
                j = -1
            i += 1
            j += 1

        if j == len(pattern):  # pattern 이 일치하여 반복문을 빠져나온 경우
            cnt += 1  # cnt 증가
        j = 0  # pattern 의 인덱스를 0으로 초기화 = 1칸 이동하여 검색 재개

    return len(text) - cnt*len(pattern) + cnt # 결과값 반환 - 최소 타이핑 횟수

T = int(input())

for _ in range(1, T + 1):
    A, B = input().split()
    result = min_typing(A, B) # result 에 함수의 리턴값 저장
    print('#{} {}'.format(_, result))


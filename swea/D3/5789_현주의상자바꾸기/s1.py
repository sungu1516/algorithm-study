import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

# test case
T = int(input())

for _ in range(1, T+1):
    N, Q = map(int, input().split())

    # 0 list 생성
    zeros = [0] * N

    for i in range(1, Q+1):
        # i 별 L, R 입력받기
        L, R = map(lambda x: int(x) - 1, input().split()) # 람다함수 이용해서 인덱싱 편하게 값 변경
        zeros[L:R+1] = [i] * (R - L + 1) # 해당 부분의 길이만큼 넣어주기

    print('#{}'.format(_), end=' ')
    print(*zeros)
import sys
sys.stdin = open("input.txt", "r")

T = 10
for tc in range(1, T + 1):
    N = int(input()) # 원본 암호문의 길이
    password = list(input().split()) # 암호가 담긴 배열
    M = int(input()) # 명령어의 개수
    command = list(input().split()) # 명령어가 담긴 배열

    # 반복문 돌며 모든 명령어 실행
    i = 1 # 인덱스 초기화 - 모두 Insert 명령어이므로, 두 번째 값부터 확인하면 됨
    while i < len(command):
        # 필요한 값 받아두기
        x = int(command[i])   # 삽입 위치 - 실제 인덱스 + 1
        y = int(command[i + 1])  # 삽입할 숫자의 개수
        for j in range(i + y + 1, i + 1, -1): # 끝 숫자부터 암호에 삽입
            password.insert(x, command[j])

        i = i + y + 3   # i값 최신화
    # 첫 10개 숫자 출력
    print('#{}'.format(tc), *password[:10])


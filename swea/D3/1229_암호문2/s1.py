import sys
sys.stdin = open("input.txt", "r")
# 필요함수 정의
def process(idx): # 명령어 안의 기능(I, D) 의 인덱스를 인자로 넣으면, password를 조작하는 함수
    # 필요한 값 받아두기
    func = command[idx]  # 실행할 기능을 받아둔다.
    x = int(command[idx+1])  # 삽입 위치 - 실제 인덱스 + 1
    y = int(command[idx + 2])  # 삽입할 숫자의 개수

    if func == 'I': # insert 기능
        for j in range(idx + y + 2, idx + 2, -1):  # 끝 숫자부터 암호에 삽입
            password.insert(x, command[j])
    else: # delete 기능
        for j in range(y):
            password.pop(x)

T = 10
for tc in range(1, T + 1):
    N = int(input()) # 원본 암호문의 길이
    password = list(input().split()) # 암호가 담긴 배열
    M = int(input()) # 명령어의 개수
    command = list(input().split()) # 명령어가 담긴 배열

    # 반복문 돌며 모든 명령어 실행
    i = 0 # 인덱스 초기화
    while i < len(command):
        process(i)
        # i값 최신화
        if command[i] == 'I': # 만약 현재 기능이 insert 라면
            i = i + int(command[i+2]) + 3
        else: # delete 라면
            i += 3
    # 첫 10개 숫자 출력
    print('#{}'.format(tc), *password[:10])


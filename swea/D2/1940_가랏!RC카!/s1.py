import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(1, T + 1):
    N = int(input())
    # 필요한 변수 선언
    speed = 0
    distance = 0
    for __ in range(N):
        command = list(map(int, input().split()))
        if command[0] == 0: # 0 인 경우 현재 속도만큼 거리 이동
            distance += speed
        elif command[0] == 1: # 1인경우
            speed += command[1] # command 내용만큼 속도를 더해주고
            distance += speed # 거리 이동
        else: # 2인 경우 - 감속
            if speed < command[1]: # 만약 현재 속도보다 감속정도가 더 클 경우
                speed = 0 # 속도 = 0 으로 초기화
            else:
                speed -= command[1]
            distance += speed

    print('#{} {}'.format(_, distance))
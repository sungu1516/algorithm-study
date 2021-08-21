import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    print('#{}'.format(tc))
    N = int(input())
    cnt = 0 # 한 줄에 들어간 알파벳의 개수를 count

    for _ in range(N):
        alpha, M = input().split()
        for i in range(int(M)): # 입력받은 개수만큼 출력
            print(alpha, end='')
            cnt += 1
            if cnt % 10 == 0: # 만약 한 줄에 10개의 알파벳이 출력되었을 때
                cnt = 0
                print() # 한 줄 넘기
    print()
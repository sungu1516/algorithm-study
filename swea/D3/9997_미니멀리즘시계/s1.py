import sys
sys.stdin = open('input.txt', encoding='UTF-8')

T = int(input())

for tc in range(1, T + 1):
    angle = int(input()) # 입력받은 각도
    k = int(12 * 60 / 360) # k = 각도당 분
    h, m = angle*k // 60, angle*k % 60 # 시, 분을 각각 저장해준다.
    print('#{} {} {}'.format(tc, h, m))
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 각 지폐별 사용 횟수를 저장할 배열을 만들기 - idx 0: 5000원 ~ idx 7: 10원
    cnts = [0]*8
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

    # 반복문을 통해 가장 큰 금액부터 계산(greedy)
    for i in range(8):
            cnts[i] = N//money[i] # 몫을 cnts 에 저장
            N %= money[i] # 거스름돈은 계속해서 계산

    print('#{}'.format(tc))
    print(*cnts)
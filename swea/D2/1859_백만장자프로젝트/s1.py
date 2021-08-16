T = int(input())

for _ in range(1, T + 1):
    N = int(input()) # 총 일수
    prices = list(map(int, input().split())) # 일별 매매가들이 담긴 리스트
    max_idx = len(prices) - 1 # 최대 매매가의 idx 를 초기화
    profit = 0 # 전체 이익을 저장해둘 변수

    for i in range(N-2, -1, -1): # 리스트의 끝에서 첫 원소까지 반복
        if prices[max_idx] < prices[i]: # 만약 값이 더 큰 원소가 등장한다면
            max_idx = i # max_idx 만 변경하고 반복문 진행
        else:
            profit += prices[max_idx] - prices[i] # 크지 않다면 profit 에 값의 차이 더해주기
    print('#{} {}'.format(_, profit))
T = int(input())

# 필요한 함수 정의
def max_profit(start, end): # 시작 인덱스와 끝 인덱스를 인자로 넣으면, 시작 인덱스의 가격부터 구매하다가 마지막 가격으로 판매한 이익을 반환하는 함수 정의
    cost = 0  # 비용 초기화

    for j in range(start, end):  # max_idx 이전의 값들을 모두 더해준다. 즉, 비용을 계산해줌
        cost += prices[j]
    return prices[end] * (end - i) - cost  # 리스트의 끝에서부터 탐색했을 때, 최댓값으로 판매한 이익을 반환

for _ in range(1, T + 1):
    N = int(input()) # 총 일수
    prices = list(map(int, input().split())) # 일별 매매가들이 담긴 리스트
    max_idx = len(prices) - 1 # 최대 매매가의 idx 를 초기화
    profit = 0 # 전체 이익을 저장해둘 변수

    for i in range(N-2, -1, -1): # 리스트의 끝에서 첫 원소까지 반복
        if prices[max_idx] < prices[i]: # 만약 값이 더 큰 원소가 등장한다면
        #     cost = 0 # 비용 초기화
        #
        #     for j in range(i + 1, max_idx): # max_idx 이전의 값들을 모두 더해준다. 즉, 비용을 계산해줌
        #         cost += prices[j]
        #     profit += prices[max_idx] * (max_idx - (i + 1)) - cost # 리스트의 끝에서부터 탐색했을 때, 최댓값으로 판매한 이익을 저장함
        #     # max_idx 를 변경
        #     max_idx = i
            profit += max_profit(i + 1, max_idx)
            max_idx = i

        elif i == 0: # 리스트의 첫 원소까지 탐색한 경우 - 위에서 이미 크기를 확인했으므로, 더해주기만 하면 됨
            profit += max_profit(i, max_idx)

    print('#{} {}'.format(_, profit))
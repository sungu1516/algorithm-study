import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cost = list(map(int, input().split()))
#
#     ans = 0
#
#     for i in range(N-1): # 어차피 마지막 날은 사도 그만 안사도 그만
#         max_cost = cost[i]
#         for j in range(i+1, N):
#             if max_cost < cost[j]:
#                 max_cost = cost[j]
#
#         if max_cost > cost[i]:
#             ans += max_cost - cost[i] # 이익을 구하자!
#
#     print('#{} {}'.format(tc, ans))

###############################################################
# 2. 팔 수 있는지 없는지 체크
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     cost = list(map(int, input().split()))
#
#     ans = 0
#
#     is_sell = [False] * N
#
#     # 사는 게 이득인지 아는지를 체크
#     for i in range(N-1):
#         for j in range(i+1, N):
#             if cost[i] < cost[j]:
#                 is_sell[i] = True
#                 break
#
#     buy_cost = 0
#     buy_cnt = 0
#
#     for i in range(N):
#         if is_sell[i]:
#             buy_cost += cost[i]
#             buy_cnt += 1
#         else:
#             ans += (cost[i]*buy_cnt) - buy_cost
#             buy_cost = 0
#             buy_cnt = 0
#
#     print('#{} {}'.format(tc, ans))

###############################################################
# 3. 반대로 생각
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cost = list(map(int, input().split())) # 가격들을 입력받기

    ans = 0

    max_cost = cost[-1]

    for i in range(N-2, -1, -1):
        # 내가 가진 값보다 보고 있는 값이 작을 때
        if max_cost > cost[i]:
            ans += max_cost - cost[i]
        else:
            max_cost = cost[i]

    print('#{} {}'.format(tc, ans))
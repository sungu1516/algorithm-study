# N = int(input())    # 배달해야 하는 설탕의 kg
# cnt = 0     # 배달해야 하는 최소 봉지 수 초기화
#
# def is_multiple(n):     # 함수 - n이 3 or 5의 배수이면 True를 리턴
#     if n % 3 and n % 5:
#         return False
#     return True
#
# if is_multiple(N):      # 3 or 5의 배수인 경우, 즉 배달 가능한 무게인 경우
#     cnt += N // 5
#     N %= 5
#     cnt += N // 3
#     print(cnt)
# else:
#     print(-1)
N = int(input())
cnt = -1
for n in range(N//3+1):
    for m in range(N//3+1):
        if N == (3*n + 5*m):
            cnt = n + m + 1
            break

print(cnt)
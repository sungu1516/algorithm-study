# input
n = int(input())

# main
ans = 0
start = 1  # 시작 수
length = 1 # 시작 자릿수

while start <= n:
    end = start * 10 - 1    # 끝 수

    if end > n:
        end = n

    # 자릿수 누적
    ans += (end - start + 1) * length

    length += 1
    start *= 10

print(ans)
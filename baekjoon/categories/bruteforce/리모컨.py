# input
import sys
input = sys.stdin.readline
targetNum = int(input())
m = int(input())
broken = list(map(int, input().split()))

# function
def isPossible(num):
    if num == 0:
        if 0 in broken:
            return 0
        else:
            return 1

    length = 0
    while num > 0:
        remain = num % 10
        if remain in broken:
            return 0

        num //= 10
        length += 1

    return length

# main
minVal = abs(targetNum - 100)   # 초기값
for num in range(1000001):
    res = isPossible(num)

    # 해당 번호로 이동 가능한 경우
    if res > 0:
        if minVal > res + abs(targetNum - num):
            minVal = res + abs(targetNum - num)

print(minVal)
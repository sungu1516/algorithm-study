# input
n = int(input())
tArr = []
pArr = []
for _ in range(n):
    t, p = map(int, input().split())
    tArr.append(t)
    pArr.append(p)

# func
def go(day, price):
    # 종료조건 - 정답
    if day == n:
        global maxVal
        maxVal = max(maxVal, price)
        return

    # 종료조건 - 불가능
    if day > n:
        return

    # 재귀 호출
    go(day + tArr[day], price + pArr[day])  # 현재 날짜를 선택하는 경우
    go(day + 1, price)  # 선택하지 않는 경우


# main
maxVal = 0  # 최대 이익 초기화
go(0, 0);
print(maxVal)
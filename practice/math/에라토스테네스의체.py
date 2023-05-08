# N이하의 모든 소수를 구할 때 유용
# 시간복잡도 - O(N*log(logN))
MAX = 1000000
check = [0] * (MAX + 1)
check[0] = check[1] = True

for i in range(2, MAX + 1):
    if not check[i]:
        j = i + i

        # MAX 이하 i의 모든 배수 True 처리
        while j <= MAX:
            check[j] = True
            j += i

# n ~ m 사이의 모든 소수를 출력
n, m = map(int, input().split())
for i in range(n, m + 1):
    if not check[i]:
        print(i)
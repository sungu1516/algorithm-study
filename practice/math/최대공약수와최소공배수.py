# 유클리드 호제법
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

a, b = map(int, input().split())
g = gcd(a, b)
# 최대 공약수 출력
print(g)
# 최소 공배수 출력
print(a * b // g)
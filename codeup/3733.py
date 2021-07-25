# 3733 : 우박수 길이 (3n+1)
num1, num2 = map(int, input().split())
count = 0

# global 사용
def collas(n):
    global count
    count += 1
    if n == 1:
        temp = count
        count = 0
        return temp
    elif n % 2:
        return collas(3*n + 1)
    else:
        return collas(n/2)

max_num = 0
max_len = 0

for i in range(num1, num2 + 1):
    if max_len < collas(i):
        max_len = collas(i)
        max_num = i

print(max_num, max_len)
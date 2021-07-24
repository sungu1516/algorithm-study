# 6091 : [기초-종합] 함께 문제 푸는 날

n1, n2, n3 = map(int, input().split())
min_num = min(n1, n2, n3)*2

while True:
    if not (min_num % n1 or min_num % n2 or min_num % n3):
        break
    min_num += 1

print(min_num)
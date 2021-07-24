# 6087 : [기초-종합] 3의 배수는 통과

number = int(input())

# for문
# for i in range(1, number + 1):
#     if i % 3:
#         print(i, end = ' ')

# while 문
i = 0

while i < number:
    i += 1
    if i % 3 == 0:
        continue
    print(i, end=' ')
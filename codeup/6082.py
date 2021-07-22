# 6082 : [기초-종합] 3 6 9 게임의 왕이 되자

end_number = int(input())

for num in range(1, end_number + 1):
    count = 0
    temp_num = num
    while num:
        if (num % 10) in [3, 6, 9]:
            count += 1
        num = num // 10
    result = 'X' * count if count else temp_num
    print(result, end=' ')

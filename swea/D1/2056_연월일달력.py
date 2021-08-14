T = int(input())

for _ in range(1, T+1):
    date = input()
    year = date[:4]
    month = date[4:6]
    day = date[6:]

    # 필요한 딕셔너리 만들기 - 월별 일수
    cal = {
        '01': range(1, 32),
        '02': range(1, 29),
        '03': range(1, 32),
        '04': range(1, 31),
        '05': range(1, 32),
        '06': range(1, 31),
        '07': range(1, 32),
        '08': range(1, 32),
        '09': range(1, 31),
        '10': range(1, 32),
        '11': range(1, 32),
        '12': range(1, 32)
    }

    result = -1 # 결과값 초기화

    if 1<= int(month) <= 12:
        if int(day) in cal[month]:
            result = '{}/{}/{}'.format(year,month,day)

    print('#{} {}'.format(_, result))
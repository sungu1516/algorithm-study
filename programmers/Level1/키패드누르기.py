def solution(numbers, hand):
    coordinates = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1),
    }

    left_numbers = (1, 4, 7)
    right_numbers = (3, 6, 9)
    mid_numbers = (2, 5, 8, 0)
    left_location = (3, 0)
    right_location = (3, 2)

    answer = ''

    for number in numbers:
        if number in left_numbers:
            answer += 'L'
            left_location = coordinates[number]
        elif number in right_numbers:
            answer += 'R'
            right_location = coordinates[number]
        else:
            # 왼손, 오른손과 대상 숫자의 거리 측정
            # 맨해튼 거리
            left_dist = abs(left_location[0] - coordinates[number][0]) + abs(left_location[1] - coordinates[number][1])
            right_dist = abs(right_location[0] - coordinates[number][0]) + abs \
                (right_location[1] - coordinates[number][1])

            # 1. 왼쪽 손이 가까운 경우
            if left_dist < right_dist:
                answer += 'L'
                left_location = coordinates[number]
            # 2. 오른쪽 손이 가까운 경우
            elif left_dist > right_dist:
                answer += 'R'
                right_location = coordinates[number]
            # 3. 거리가 동일한 경우
            else:
                if hand == "left":
                    answer += 'L'
                    left_location = coordinates[number]
                else:
                    answer += 'R'
                    right_location = coordinates[number]

    return answer
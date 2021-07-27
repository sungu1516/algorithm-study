# 3. 숫자의 의미 - 연속되는 숫자들을 제거하라

def lonely(numbers):
    # 원소의 값이 하나라면 리스트 그대로 반환
    if len(numbers) == 1:
        return numbers
    # 비교할 원소의 인덱스 초기와
    idx = 0
    # while 문의 종료조건 : 비교할 원소의 인덱스가 리스트의 마지막일 때
    while idx < len(numbers) - 1:
        if numbers[idx] == numbers[idx + 1]:
            # 만약 연속되는 두 원소가 동일할 때, 선행하는 원소를 제거
            numbers.pop(idx)
        else:
            # 연속되는 두 원소가 동일하지 않다면 인덱스값에 1을 더해주고, 다시 반복
            idx += 1

    return numbers

print(lonely([1, 1, 2, 2, 1, 3, 3, 4, 2, 1]))
def solution(numbers):
    # 첫 자리를 기준으로 내림차순
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)

    # test log
    return str(int(''.join(numbers)))
def solution(arr, divisor):
    answer = []

    for number in arr:
        if (number % divisor == 0):
            answer.append(number)

    return sorted(answer) if len(answer) > 0 else [-1]
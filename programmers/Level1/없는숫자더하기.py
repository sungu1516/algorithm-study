def solution(numbers):
    numbers = set(numbers)
    std = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    diff_set = std - numbers

    return sum(diff_set)
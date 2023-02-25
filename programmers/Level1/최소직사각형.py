def solution(sizes):
    left = []
    right = []

    for size in sizes:
        left.append(max(size))
        right.append(min(size))

    answer = max(left) * max(right)

    return answer
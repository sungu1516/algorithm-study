def solution(d, budget):
    answer = 0
    spend = 0
    idx = 0

    # 정렬
    d.sort()

    for i in range(len(d)):
        spend += d[i]
        if (spend > budget):
            break
        answer += 1

    return answer
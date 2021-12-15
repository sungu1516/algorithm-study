def solution(citations):
    # 내림차순으로 정렬
    citations.sort(reverse=True)

    # 만약 모든 논문의 인용횟수가 논문의 수보다 높은 경우
    if min(citations) > len(citations):
        return len(citations)

    # citations을 순회하며 조건 만족 시 H-Index 리턴
    for idx, cnt in enumerate(citations, start=1):
        if cnt <= idx:
            pre_idx = idx - 1
            return max(pre_idx, cnt)
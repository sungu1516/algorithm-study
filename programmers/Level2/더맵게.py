from collections import deque

def solution(scoville, K):
    cnt = 0     # 섞는 횟수 초기화
    
    # 1. queue 에 모든 scoville 지수 넣어주기 (정렬) 
    scoville = sorted(scoville)
    
    # que안에 든 음식이 2개 이상일 때까지만 반복
    while len(scoville) > 2:
        # 2. 작은 2개의 값 leftpop() 후 새로운 음식의 스코빌지수 계산 
        min1 = scoville.pop(0)
        min2 = scoville.pop(0)
        unit = min1 + (min2 * 2)
        cnt += 1

        # que에 다시 삽입 후 정렬
        scoville.append(unit)
        scoville = sorted(scoville)

        # 3. 스코빌지수 확인
        if scoville[0] >= K:
            return cnt
    
    # 음식이 1개가 될 때까지 섞었지만 스코빌지수를 넘지 못한 경우
    return 0

print(solution([1, 2, 3, 9, 10, 12], 7))
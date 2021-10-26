from heapq import heappush, heappop, heapify

def solution(scoville, K):
    cnt = 0  # 섞는 횟수 초기화

    # 1. scoville arr -> min heap 자료형으로 변환
    heapify(scoville)
    # 가지치기 - 이미 배열의 모든 스코빌 지수가 K 이상일 때
    if scoville[0] >= K:
        return cnt

    # 반복문 - heap 내의 스코빌지수가 1개보다 크거나
    while len(scoville) > 1:
        # 2. 작은 값 두 개를 빼서 섞고, 새로운 스코빌지수 구하기
        min_val1 = heappop(scoville)
        min_val2 = heappop(scoville)
        new_val = min_val1 + (min_val2 * 2)
        cnt += 1  # 맛을 섞었으니 cnt ++

        # 3. 새로구한 스코빌지수를 최소힙에 삽입
        heappush(scoville, new_val)

        # 4. 크기확인
        # 만약 힙의 루트(최소값)가 K보다 같거나 크다면
        if scoville[0] >= K:
            return cnt

    # 반복문이 cnt를 리턴하지 않고 종료되었을 경우
    return -1

print(solution([1, 2, 3, 9, 10, 12], 7))
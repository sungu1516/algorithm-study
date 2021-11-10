from collections import deque

def solution(priorities, location):
    # priorities 배열 변환 -> location(index) 값이 포함되도록
    arr = deque()
    for i in range(len(priorities)):
        arr.append((priorities[i], i))
        
    # location 위치의 원소가 몇 번째로 출력되는지 확인
    rear = 0  # 현재 출력할 원소의 위치 
    
    # arr이 빌 때까지 꺼내면서 확인
    while arr:
        curr = arr.popleft()
        # 만약 해당 원소가 마지막 원소인 경우
        if not arr:
            return rear + 1
            continue
        
        temp_arr = [x[0] for x in arr]  # priorities 만 포함된 배열 재생성
        
        # 만약 우선순위가 가장 높을 때
        if curr[0] >= max(temp_arr):
            rear += 1
            if location == curr[1]:
                return rear
        # 남은 목록 중 우선순위가 더 높은 것이 있을 경우
        else:
            arr.append(curr)
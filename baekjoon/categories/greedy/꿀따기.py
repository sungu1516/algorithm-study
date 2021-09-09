N = int(input())    # 장소의 수
honey = list(map(int, input().split()))     # 각 장소의 꿀의 양

max_val = 2*sum(honey[2:]) if 2*sum(honey[2:]) > 2*sum(honey[0:N-2]) else 2*sum(honey[0:N-2])      # 도착지점이 양쪽 끝인 경우를 먼저 고려해준다.

for i in range(N-2, 0, -1):    # 도착지점 = i (양 끝 지점 배제)
    temp = 0
    left, right = sum(honey[1:i+1]), sum(honey[i:N-1])
    if left > right:    # 첫 번째 출발 위치가 왼쪽 끝인 경우
        temp += left    # 첫 번째 출발 위치로부터 도착지까지의 꿀을 모두 더해준다.

        # 두 번째 위치 결정
        if left-honey[1] > right:   # 두 번째 출발 위치가 왼쪽 끝인경우
            temp += left-honey[0]

        else:   # 두 번째 출발 위치가 오른쪽 끝인경우
            temp += right
    else:     # 첫 번째 출발 위치가 오른쪽 끝인 경우
        # 두 번째 위치 결정
        if left > right - honey[N-2]:  # 두 번째 출발 위치가 왼쪽 끝인경우
            temp += left

        else:  # 두 번째 출발 위치가 오른쪽 끝인경우
            temp += right - honey[N-2]

    if max_val < temp:
        max_val = temp


print(max_val)
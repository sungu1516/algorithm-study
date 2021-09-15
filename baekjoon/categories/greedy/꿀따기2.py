N = int(input())    # 장소의 수
arr = list(map(int, input().split()))     # 각 장소의 꿀의 양
max_val = 0     # 최대 꿀의 양 초기화

# 꿀통이 오른쪽 끝에 있는 경우
for i in range(1, N-1):     # i : 움직이는 출발점의 위치
    fixed = sum(arr) - arr[0] - arr[i]
    move = sum(arr[i+1:])
    total = fixed + move
    if total > max_val:
        max_val = total

# 꿀통이 왼쪽 끝에 있는 경우
for i in range(N-2, 0, -1):
    fixed = sum(arr) - arr[-1] - arr[i]
    move = sum(arr[:i])
    total = fixed + move
    if total > max_val:
        max_val = total

# 벌-통-벌
for i in range(1, len(arr)-1):
    cnt = sum(arr[1:len(arr)-1])+arr[i]
    if cnt > max_val:
        max_val = cnt

print(max_val)
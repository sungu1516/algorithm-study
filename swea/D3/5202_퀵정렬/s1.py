import sys
sys.stdin = open('input.txt')

def partition(arr, left, right):
    p = arr[left]   # 피벗을 배열의 왼쪽 원소로 지정
    i, j = left, right  # 양 끝 인덱스를 가리킴
    while i <= j:   # 두 변수가 가리키는 지점이 교차하기 전까지
        while i <= j and arr[i] <= p:   # 피벗보다 큰 값을 찾을 때까지 ++
            i += 1
        while i <= j and arr[j] >= p:   # 피벗보다 작은 값을 찾을 때까지 --
            j -= 1
        if i < j:   # 만약 두 지점이 만나지 않은 경우
            arr[i], arr[j] = arr[j], arr[i] # 위치를 변경한다. (작은 값을 왼쪽, 큰 값을 오른쪽으로 이동시키기 위함)
    arr[left], arr[j] = arr[j], arr[left]   # i와 j가 교차하면 j가 가리키는 원소들은 모두 피벗보다 작은 값이므로, 피벗을 가운데로 이동
    return j    # 피벗의 idx 를 리턴

def quick_sort(arr, left, right):
    if left < right:
        idx = partition(arr, left, right)
        quick_sort(arr, left, idx-1)    # 인덱스 기준 왼쪽 배열
        quick_sort(arr, idx+1, right)   # 인덱스 기준 오른쪽 배열

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)
    ans = arr[N//2]

    print('#{} {}'.format(tc, ans))
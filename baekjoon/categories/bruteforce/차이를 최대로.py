# func
def calc(nums):
    res = 0
    for i in range(n - 1):
        res += abs(nums[i] - nums[i + 1])

    return res

def next_permutation(a):
    # 교체할 숫자의 인덱스 찾기 - i
    i = len(a) - 1
    while i > 0 and a[i - 1] >= a[i]:
        i -= 1
    if i <= 0:
        # a가 순열 중 마지막임을 의미
        return False
    # 교체할 숫자와 swap 할 숫자의 인덱스 찾기
    j = len(a) - 1
    while a[j] <= a[i - 1]:
        j -= 1

    a[i - 1], a[j] = a[j], a[i - 1]

    # reverse 를 통해서 뒷 부분을 정렬
    j = len(a) - 1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # a 다음 순열이 있음을 의미
    return True

# main
n = int(input())
nums = sorted(list(map(int, input().split())))
ans = 0 # 최댓값 초기화
while True:
    val = calc(nums)
    ans = max(val, ans)
    if not next_permutation(nums):
        break

print(ans)
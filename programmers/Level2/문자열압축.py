def solution(s):
    # 1개 단위로 잘라보기
    cnt = 1
    arr = []
    for i in range(1, len(s)):
        if i == len(s) - 1:
            arr.append(cnt)
        if s[i-1] == s[i]:
            cnt += 1
        else:
            arr.append(cnt)
            cnt = 1

    # 개수 세기
    ans = 0
    for i in range(len(arr)):
        if arr[i] > 2:
            arr[i] = 2
        ans += arr[i]

    return ans

string =  "aabbaccc"
print(solution(string))
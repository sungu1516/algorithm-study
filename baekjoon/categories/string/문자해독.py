def permutation(cnt):
    if cnt == len(W):
        global ans

        string = ''.join(p)  # 문자열로 다시 변환
        # 해당 문자열이 포함된 개수 탐색
        for i in range(len(S) - len(W)):
            if string == S[i:i+len(W)]:
                ans += 1

    for i in range(len(W)):
        if not visited[i]:
            visited[i] = 1
            p[cnt] = W[i]
            permutation(cnt+1)
            visited[i] = 0


g, s = map(int, input().split())
W = input()
S = input()

visited = [0] * len(W)
p = [0] * len(W)

ans = 0

permutation(0)

print(ans)
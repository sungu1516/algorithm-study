# input
n, m = map(int, input().split())
paper = [list(map(int, input().split()))for _ in range(n)]

# main
## 1. blocks
blocks = (
 ((0,1), (0,2), (0,3)),
 ((1,0), (2,0), (3,0)),
 ((1,0), (1,1), (1,2)),
 ((0,1), (1,0), (2,0)),
 ((0,1), (0,2), (1,2)),
 ((1,0), (2,0), (2,-1)),
 ((0,1), (0,2), (-1,2)),
 ((1,0), (2,0), (2,1)),
 ((0,1), (0,2), (1,0)),
 ((0,1), (1,1), (2,1)),
 ((0,1), (1,0), (1,1)),
 ((0,1), (-1,1), (-1,2)),
 ((1,0), (1,1), (2,1)),
 ((0,1), (1,1), (1,2)),
 ((1,0), (1,-1), (2,-1)),
 ((0,1), (0,2), (-1,1)),
 ((0,1), (0,2), (1,1)),
 ((1,0), (2,0), (1,1)),
 ((1,0), (2,0), (1,-1))
)

maxVal = 4

for i in range(n):
    for j in range(m):
        # 각각의 모양에 대해 확인
        for block in blocks:
            isValid = True  # 해당 지점에 모양을 넣을 수 있는지 여부
            temp = paper[i][j]  # sum of numbers 초기화

            for k in block:
                ti, tj = i + k[0], j + k[1]   # 해당 칸의 인덱스
                # 각 모양의 특정 칸이 범위 밖에 있다면
                if ti < 0 or ti >= n or tj < 0 or tj >= m:
                    isValid = False
                    break
                # 범위 안에 있는 경우
                temp += paper[ti][tj]

            # 최대값 갱신
            if isValid:
                if maxVal < temp:
                    maxVal = temp

print(maxVal)
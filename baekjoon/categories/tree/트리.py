# leaf node 의 개수를 세는 함수 정의
def count_leaf(n):
    global cnt

    if n == M:  # 삭제된 노드일 경우 - 접근 X
        return

    if not tree[n]: # 자식노드가 없는 경우
        cnt += 1    # leaf node count
        return

    for ve in tree[n]:
        count_leaf(ve)

N = int(input())
arr = list(map(int, input().split()))
M = int(input())    # 지울 노드의 번호

tree = [[] for _ in range(N)] # 그래프 초기화
cnt = 0 # 리프노드의 개수 초기화

# 트리 만들기 - 배열엔 해당 트리의 번호가, 값엔 자식 노드의 번호가 담겨있다.
for i in range(N):
    if arr[i] == -1: continue

    tree[arr[i]].append(i)

# 삭제 처리  (M번 노드를 자식으로 갖고있는 경우, 배열에서 삭제)
for row in tree:
    if M in row:
        row.remove(M)   # 리프노드의 개수를 정확히 세기 위해, 삭제한다.
        break

count_leaf(arr.index(-1))   # 루트 노드부터 시작한다.
print(cnt)
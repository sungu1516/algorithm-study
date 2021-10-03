import sys
sys.setrecursionlimit(10*9)     # 재귀의 최대깊이 제한 해제 (입력값을 받기 위해)

# 후의 순회 함수 정의
def postorder(n):
    if n < len(tree) and tree[n]:
        postorder(2 * n)
        postorder(2 * n + 1)
        print(tree[n])


# 함수 정의 - 전위순회 결과를 바탕으로 기존의 이진 검색 트리를 완성
def make_tree(idx, subtree):
    if subtree:
        root = subtree[0]
        tree[idx] = root
        print(tree)
        # base condition
        if len(subtree) < 2:
            return

        # tree 완성을 위한 dfs
        k = 0   # 오른쪽 subtree의 인덱스 초기화
        for i in range(1, len(subtree)):
            if root< subtree[i]:
                k = i
                break

        if k:   # 오른쪽 subtree 가 존재하는 경우
            make_tree(2 * idx, subtree[1:k])      # 왼쪽 subtree 탐색
            make_tree(2 * idx + 1, subtree[k:])    # 오른쪽 subtree 탐색
        else:
            make_tree(2 * idx, subtree[1:])  # 왼쪽 subtree 탐색

# 입력값 받기 - 입력의 크기가 주어지지 않았다는 점에 주의
input = sys.stdin.readline
que=[]  # 전위순회한 결과 - 노드의 key 가 담긴다.

while True:
    try:
        que.append(int(input()))
    except:
        break

tree = [0] * len(que) * 100000

make_tree(1, que)

postorder(1)

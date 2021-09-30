# tree 를 생성하는 함수
def make_tree(arr, level):
    if level > K:   # 주어진 레벨보다 커진 경우
        return
    # 방문처리 - tree 에 층별로 저장
    mid = len(arr) // 2
    tree[level].append(arr[mid])    # 방문한 노드는 해당 층에 삽입해주기
    make_tree(arr[:mid], level + 1)     # 왼쪽 subtree 방문
    make_tree(arr[mid+1:], level + 1)   # 오른쪽 subtree 방문

K = int(input())    # tree의 레벨 K
arr = list(map(int, input().split()))   # 중위순회로 출력한 순서대로 저장

tree = [[] for _ in range(K+1)]     # 각 층(레벨) 별 노드를 저장
make_tree(arr, 1)

for i in range(1, K+1):     # 1번 층부터 출력
    print(*tree[i])
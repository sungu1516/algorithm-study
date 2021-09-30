# 트리 순회함수
# 전위
def preorder(n):
    if n != '.':
        print(n, end='')    # 방문 후 처리
        preorder(tree[n][0])  # 왼쪽자식
        preorder(tree[n][1])  # 오른쪽

# 중위
def inorder(n):
    if n != '.':
        inorder(tree[n][0])  # 왼쪽자식
        print(n, end='')    # 방문 후 처리
        inorder(tree[n][1])  # 오른쪽

# 후위
def postorder(n):
    if n != '.':
        postorder(tree[n][0])  # 왼쪽자식
        postorder(tree[n][1])  # 오른쪽
        print(n, end='')  # 방문 후 처리

N = int(input())    # 노드의 개수
tree = dict()

# 트리 완성
for _ in range(N):
    p, c1, c2 = input().split()
    tree[p] = [c1, c2]

preorder('A')
print()
inorder('A')
print()
postorder('A')


import sys
sys.setrecursionlimit(10**9)     # 재귀의 최대깊이 제한 해제 (입력값을 받기 위해)

# 함수 정의 - 전위 순회의 결과를 후위 순회로 출력하는 함수
def pre_to_post(subtree):
    if not subtree: return  # 만약 노드가 존재하지 않는다면

    root = subtree[0]   # 방문 노드 (가운데)

    k = len(subtree)  # 오른쪽 subtree의 인덱스 초기화
    for i in range(1, len(subtree)):
        if root < subtree[i]:   # 만약 오른쪽 sub tree 가 있다면 해당 인덱스를 저장하고, 없다면 마지막 인덱스가 k에 저장됨
            k = i
            break

    # 후위순회
    pre_to_post(subtree[1:k])  # 왼쪽 subtree 탐색
    pre_to_post(subtree[k:])  # 오른쪽 subtree 탐색
    print(root) # 방문처리 - 출력

# 입력값 받기 - 입력의 크기가 주어지지 않았다는 점에 주의
input = sys.stdin.readline
que=[]  # 전위순회한 결과 - 노드의 key 가 담긴다.

while True:
    try:
        que.append(int(input()))
    except:
        break

pre_to_post(que)

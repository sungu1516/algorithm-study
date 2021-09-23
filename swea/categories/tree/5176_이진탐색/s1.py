import sys
sys.stdin = open('input.txt', 'r')
# 중위 순회 함수 정의
def inorder(n):
    if 0 < n <= N:
        inorder(2*n)    # 왼쪽 자식 노드로 이동
        arr2.append(n)
        inorder(2*n + 1)    # 오른쪽 자식 노드로 이동

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr2 = [0] # 각 숫자(값) 이 인덱스로, 노드 번호가 값인 배열 초기화
    result = [0] * (N+1)    # 결과 배열

    inorder(1)

    for idx, value in enumerate(arr2):  # arr2 를 바탕으로, 노드 번호를 인덱스로 번호에 해당하는 숫자를 값으로 갖는 배열을 만들기
        result[value] = idx

    print(f'#{tc} {result[1]} {result[N//2]}')



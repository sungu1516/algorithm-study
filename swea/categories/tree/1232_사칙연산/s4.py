import sys
sys.stdin = open('input.txt', 'r')

def calc(v):
    if len(tree[v]) == 2:
        return int(tree[v][1])
    else:
        L = calc(int(tree[v][2]))
        R = calc(int(tree[v][3]))

        if tree[v][1] == '+': return L+R
        elif tree[v][1] == '-': return L-R
        elif tree[v][1] == '*': return L*R
        elif tree[v][1] == '/': return L/R

for tc in range(1, 11):
    N = int(input())    # 정점의 개수
    tree = [0] * (N+1)

    for i in range(1, N+1):
        tmp = input().split()

        tree[int(tmp[0])] = tmp

    print("#{} {}".format(tc, int(calc(1))))
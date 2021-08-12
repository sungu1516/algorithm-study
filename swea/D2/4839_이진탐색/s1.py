import sys
# input을 파일로 받아오는 설정
sys.stdin = open('input.txt')

# 필요 함수 정의 - 전체 페이지와 찾을 페이지를 인자로 받는 함수. 호출 시 필요한 탐색 횟수 리턴
def search_cnt(total_page, key):
    start = 1
    end = total_page

    # key 값을 찾는 데 필요한 반복 횟수
    cnt = 1

    # 이진탐색
    while  start <= end:
        middle = (start + end) // 2
        if middle == key:
            # 중간 값과 찾고자 하는 페이지가 같으면 cnt 를 리턴
            return cnt
        # 키값을 찾는데 실패하면 탐색 범위가 수정되고 cnt++
        elif middle > key:
            end = middle
            cnt += 1
        else:
            start = middle
            cnt += 1

T = int(input())

for _ in range(1, T + 1):
    p, pa, pb = map(int, input().split())
    a_cnt = search_cnt(p, pa) # A가 해당 페이지를 찾는데 필요한 반복횟수가 저장됨
    b_cnt = search_cnt(p, pb) # B가 해당 페이지를 찾는데 필요한 반복횟수가 저장됨
    result = 'A' if a_cnt < b_cnt else 'B' if a_cnt > b_cnt else 0

    print('#{} {}'.format(_, result))
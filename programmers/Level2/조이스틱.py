def solution(name):
    '''
    상하, 좌우 조작 횟수를 각각 구한다.
    '''
    
    '''
    상하의 경우 ord() 를 이용하여 두 가지 경우 중 작은 값을 구한다.
    좌우의 경우, 그리디로 접근한다.
    처음 변경하는 문자를 시작점으로, 가까운 알파벳으로 이동하며 바꿔나간다.
    '''
    
    # 최소 조작횟수 초기화
    min_cnt = 0
    
    # 각 알파벳의 상하 최소 조작횟수를 배열에 담는다.
    min_updown = []
    for chr in name:
        min_updown.append(min(ord(chr)-ord('A'), ord('Z')-ord(chr) + 1))
    
    # 최소 좌우 조작횟수 구하기
    idx = 0
    while True:
        min_cnt += min_updown[idx]
        min_updown[idx] = 0     # 변경시킨 부분은 0으로 변경해준다. (더 이상의 횟수가 필요없음을 의미)
        
        # 더이상 바꿀 알파벳이 없는 경우, 반복문 종료
        if sum(min_updown) == 0:
            break
            
        left, right = 1, 1  # 왼쪽, 오른쪽으로 이동했을 때 A가 아닌 다른 알파벳을 만나기 위한 최소이동거리 초기화
        while min_updown[idx - left] == 0:
            left += 1
        while min_updown[idx + right] == 0:
            right += 1
        
        # 더 적게 이동할 수 있는 방향을 선택하여 결과값, idx에 더해주기
        min_cnt += right if right < left else left
        idx += right if right <= left else -left
        
    return min_cnt
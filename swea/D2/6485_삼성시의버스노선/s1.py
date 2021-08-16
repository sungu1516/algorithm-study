T = int(input())

for _ in range(1, T + 1):
    N = int(input()) # 노선의 개수
    routes = [list(map(int, input().split())) for _ in range(N)] # 버스 노선 정보를 2차원 배열 형태로 저장

    P = int(input()) # 버스 정류장의 개수
    stops = [int(input()) for _ in range(P)] # 버스 정류장 번호를 배열 형태로 저장

    result = [] # 결과값을 저장할 배열 초기화
    for stop in stops: # 주어진 모든 버스정류장을 순회
        cnt = 0 # 정류장이 버스 노선에 속하는 횟수 초기화
        for route in routes: # 모든 노선을 순회하며, 정류장이 노선에 포함되는지 확인
            if route[0] <= stop <= route[1]:
                cnt += 1
        result.append(cnt)

    print('#{}'.format(_), *result)
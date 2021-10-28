def solution(s):
    # 문자열 parsing
    arr = s.strip('{}').split('},{')
    # 배열로 변환 & 부분 집합의 길이를 기준으로 오름차순 정렬
    arr = sorted(map(lambda x: x.split(','), arr), key=lambda x: len(x))
    
    # 모든 부분 집합을 순회하며 원래의 튜플을 만들기
    result = []
    for subset in arr:
        for num in subset:
            if num not in result:
                result.append(num)
                flag = False
                break
    
    # 정수로 변환
    result = list(map(int, result))
    
    return result
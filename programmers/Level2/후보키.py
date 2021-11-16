from itertools import combinations
def solution(relation):
    # relation colums 의 모든 조합 경우의 수
    
    cols = len(relation[0])
    
    combs = []  # 리스트에 담아두기
    for i in range(1, cols + 1):
        combs.extend(combinations(range(cols), i))
    
    '''
    combs 에는 모든 잠재 후보키가(column의 조합) 존재
    '''
    
    
    # 조건을 만족하는 후보키를 넣어둘 배열
    candidates = []
    # 검사
    for comb in combs:
        # 모든 잠재 후보키를 고려한다.
        hash = set()    # 유일성을 확인하기 위한 hash
        for row in relation:
            tmp = []
            for i in comb:
                tmp.append(row[i])
            hash.add(tuple(tmp))
        
        # 유일성 검사
        if len(hash) == len(relation):
            able = True
            
            # 최소성 검사
            for candidate in candidates:
                if set(candidate).issubset(set(comb)):
                    able = False
                    break
            
            # 두 조건을 모두 만족하는 경우 candidates 배열에 추가
            if able:
                candidates.append(comb)
    
    return len(candidates)
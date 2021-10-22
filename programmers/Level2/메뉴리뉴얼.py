from itertools import combinations

def solution(orders, course):
    result = []
    # course 순회하며, 특정 길이의 문자열의 빈도 hash에 저장
    for cnt in course:
        # hash 초기화
        hash = dict()
        
        # orders를 순회
        for order in orders:
            if len(order) < cnt: continue
            
            for comb in combinations(order, cnt):
                string = ''.join(sorted(comb))

                hash[string] = hash.get(string, 0) + 1
                  
        # hash 완성
        # 만약 hash가 비어있다면 - continue
        if not hash: continue
        
        # hash의 value 중 max_value를 찾고, 이에 대응하는 key(s) 을 result에 담기
        max_value = max(hash.values())
        
        # 최소 2명 이상의 손님으로부터 주문되어야 
        if max_value < 2: continue
        
        for key, value in hash.items():
            if value == max_value:
                result.append(''.join(key))      # 정렬해서 넣어준다.
        
    # 알파벳순으로 정렬
    result.sort()
    return result
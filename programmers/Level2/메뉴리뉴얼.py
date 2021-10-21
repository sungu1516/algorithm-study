from itertools import combinations

def solution(orders, course):
    result = []
    # course 순회하며, 특정 길이의 문자열의 빈도 hash에 저장
    hash = dict()
    for cnt in course:
        # orders를 순회
        for order in orders:
            if len(order) < cnt: continue
            
            for comb in combinations(order, cnt):
                string = ''.join(comb)
                hash[string] = hash.get(string, 0) + 1
                
            
        # hash 완성    
        # cnt와 동일한 길이를 가진 order에 대해서만 결과에 누적
        for key, value in hash.items():
            if value == cnt:
                print(value)
                result.append(''.join(sorted(key)))
        print(hash)
    return result
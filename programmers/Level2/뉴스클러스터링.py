# 인자로 들어온 문자열이 모두 알파벳이라면 True 반환
def is_alpha(string):
    for chr in string:
        num = ord(chr)
        if num < 97 or num > 122:
            return False
    return True

def solution(str1, str2):
    # 모두 소문자화    
    str1, str2 = str1.lower(), str2.lower()

    # 1. 각 문자열의 다중집합 만들기
    set1, set2 = [], []
   
    # 1) set1
    for i in range(len(str1)-1):
        tmp = str1[i:i+2]
        print(tmp)
        if is_alpha(tmp):
            set1.append(tmp)
    # 2) set2
    for i in range(len(str2)-1):
        tmp = str2[i:i+2]
        if is_alpha(tmp):
            set2.append(tmp)
    
    # 두 다중집합 모두 공집합인 경우 - 합집합이 0이므로 나눗셈 불가
    if not set1 and not set2:
        return 65536
    
    # 2. 자카드 유사도 구하기
    
    # 1) 교집합의 개수 구하기
    intersection = 0
    
    # hash 구하기
    hash1, hash2 = {}, {}
    for s in set1:
        hash1[s] = hash1.get(s, 0) + 1
    for s in set2:
        hash2[s] = hash2.get(s, 0) + 1

    for key1 in hash1:
        if key1 in hash2:
            intersection += min(hash1[key1], hash2[key1])
    
    # 2) 합집합의 개수 구하기
    # n(AUB) = n(A) + n(B) - n(AnB)
    union = len(set1) + len(set2) - intersection
    
    
    # 3) 유사도 계산
    answer = int(intersection / union * 65536)
    return answer
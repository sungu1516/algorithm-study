from itertools import combinations, permutations

# 해당 숫자가 소수인지를 판별하는 함수
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number//2 + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    # 소수를 담을 set
    prime_numbers = set()
    # 가지치기를 위한 set
    records = set()
    
    for i in range(1, len(numbers) + 1):
        for comb in combinations(numbers, i):
            print(comb)
            if comb in records: continue    # 가지치기
            records.add(comb)
            # 숫자의 순서가 뒤바뀔 수 있음을 고려
            for perm in permutations(comb):
                # int 형으로 변환
                number = int(''.join(perm))
                print(number)
                # 만약 소수라면
                if is_prime(number):
                    prime_numbers.add(number)
                    
    return len(prime_numbers)
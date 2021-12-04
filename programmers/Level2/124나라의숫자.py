def solution(n):
    # 3진수
    result = ''
    
    while n:
        remainder = n % 3
        
        # 3으로 나누어 떨어지지 않는 경우 - 3진수로 표현한 것과 동일!
        if remainder:
            result = str(remainder) + result
            n = n // 3
        # 3으로 나누어 떨어지는 경우 - 나머지로 0대신 4를 넣어주고, 몫은 -1 처리
        else:
            result = '4' + result
            n = n // 3 - 1
            
    return result
def solution(phone_book):
    N = len(phone_book)     # 전화번호부 안의 전화번호의 개수
    for i in range(N-1):
        pre_len = len(phone_book[i])      # 현재 가리키고 있는 전화번호의 길이
        
        for j in range(i+1, N):     # 중복 비교하지 않게, 현재 전화번호의 뒤의 것들과만 비교   
            post_len = len(phone_book[j])
            
            # 만약 비교대상이 되는 전화번호의 길이가 더 짧다면
            if pre_len > post_len:
                i, j = j, i
                pre_len, post_len = post_len, pre_len
            
            for k in range(post_len - pre_len + 1):
                print(phone_book[i])
                print(phone_book[j][k:k+pre_len])
                if phone_book[i] == phone_book[j][k:k+pre_len]:
                    return False
                
    return True
            
# 2. 소대소대

def low_and_up(word):
    result = ''
    # 들어온 문자의 글자 하나하나를 소문자로 바꾸로 리스트로 형변환
    chrs = [x.lower() for x in word]

    for i in range(1, len(chrs), 2):
        # 홀수 인덱스를 가지는 리스트 원소만 대문자로 값 변경
        chrs[i] = chrs[i].upper()

    # join 메서드를 활용하여 리스트를 이어붙인 후 출력
    return ''.join(chrs)

print(low_and_up('banana'))
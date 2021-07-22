# 3. 강한 이름

def get_strong_word(str1, str2):
    total1 = 0
    total2 = 0

    for alp in str1:
        total1 += ord(alp)
    for alp in str2:
        total2 += ord(alp)

    return str1 if total1 > total2 else str2

print(get_strong_word('tom', 'john'))

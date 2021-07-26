# 1. 모음은 몇 개나 있을까?

def count_vowels(word):
    # 횟수
    cnt = 0
    # 모든 모음을 변수에 저장
    vowels = 'aeiouwy'
    # 반복문을 통해 모음 개수 저장
    for chr in vowels:
        # vowels의 모음을 하나하나 순회하며, count 메서드를 활용해 각각의 모음의 개수를 합
        cnt += word.count(chr)
    return cnt
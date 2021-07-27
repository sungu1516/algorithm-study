# 1. 무엇이 중복일까

def duplicated_letters(word):
    # count() 메서드를 이용하여 개수가 2개 이상인 문자열만 set 에 담고 (중복제거를 위해)
    # 이를 다시 리스트로 형변환하여 반환
    return list({chr for chr in word if word.count(chr) > 1})


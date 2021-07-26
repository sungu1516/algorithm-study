# 2. 내 이름은 몇일까?
def get_secret_number(word):
    total = 0
    for alp in word:
        total += ord(alp)
    return total

print(get_secret_number('tom'))
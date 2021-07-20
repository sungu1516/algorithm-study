# 함수 정의
word_input = input()

def return_reversed_word(word):
    str = ""
    for i in range(len(word) - 1, -1, -1):
        str += word[i]
    return str

reversed_word = return_reversed_word(word_input)
print(reversed_word)
if word_input == reversed_word:
    print("입력하신 단어는 회문(Palindrome)입니다.")
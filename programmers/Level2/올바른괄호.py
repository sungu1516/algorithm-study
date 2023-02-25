def solution(s):
    # conner case
    if len(s) < 2 or s[0] == ')':
        return False

    # stack
    stack = []
    for item in s:
        if item == '(':
            stack.append(item)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()

    if len(stack) > 0:
        return False
    else:
        return True
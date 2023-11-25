def is_correct_brackets(brackets):
    correct_bracket = {'(':')', '{':'}', '[':']'}
    data = []
    for bracket in brackets:
        if bracket in '({[':
            data.append(bracket)
        else:
            if not data or correct_bracket[data[-1]] != bracket:
                return False
            data.pop()
    if data:
        return False
    return True

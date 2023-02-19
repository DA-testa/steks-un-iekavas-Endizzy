def find_mismatch(text):
    stack = []
    for i, char in enumerate(text):
        if char in "([{":
            stack.append((char, i))
        elif char in ")]}":
            if not stack:
                return i + 1
            last_bracket, _ = stack.pop()
            if not ((last_bracket == "(" and char == ")") or 
                    (last_bracket == "[" and char == "]") or 
                    (last_bracket == "{" and char == "}")):
                return i + 1
    if stack:
        _, position = stack.pop()
        return position + 1
    return "Success"

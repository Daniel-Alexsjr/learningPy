
def isvalid(s):
    stack = []

    for bracket in s:
        if bracket in {"(", "{", "["}:
            stack.append(bracket)
        else:
            if len(stack) == 0:
                return False
            popped = stack.pop()
            if (bracket == ")" and popped != "(") or (bracket == "}" and popped != "{") or (bracket == "]" and popped != "["):
                return False
            print(popped)
    return len(stack) == 0

print(isvalid("({})"))
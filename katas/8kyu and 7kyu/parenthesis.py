def eval_parentheses(s):
    contador = 0
    for char in range(len(s)-1):
        if s[char] == s[char + 1]:
            contador = 2
        elif s[char] == "(":
            contador += 1
        
    
    return contador
    
print(eval_parentheses("(())()"))
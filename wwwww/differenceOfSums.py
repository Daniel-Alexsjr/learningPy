def differenceofsums(n,m):
    num1 = [] 
    num2 = []
    for i in range(1,n+1):
        if i % m:
            num1.append(i)
        else:
            num2.append(i)
    return sum(num1) - sum(num2)

print(differenceofsums(5,6))
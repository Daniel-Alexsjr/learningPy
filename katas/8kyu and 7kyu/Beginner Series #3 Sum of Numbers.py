def get_sum(a,b):
    lista = []
    
    if a > b:
        lista.append(a)
        while a != b:
            a -= 1
            lista.append(a)

    elif a < b:
        lista.append(a)
        while a != b:
            a += 1
            lista.append(a)

    elif a == b:
        return a


    return sum(lista)

print(get_sum(0, 2))


def get_sum2(a,b):
    return sum(range(min(a, b), max(a, b) + 1))

print(get_sum2(0, 2))
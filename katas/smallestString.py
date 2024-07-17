def find_short(s):
    array = s.split(' ')
    numberArray =[]
    for x in array:
        numberArray.append(len(x))

    smallest = numberArray[0]
    for i in numberArray:
        if i < smallest:
            smallest = i
    return smallest

print(find_short('hello world macaco bau nice w'))




def find_short1(s):
    return min(len(x) for x in s.split())

print(find_short1('hello world macaco bau nice w'))
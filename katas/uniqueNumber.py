def find_uniq(arr):
  arr.sort()
  return arr[-1] if arr[0]==arr[1] else arr[0]


def find_uniq2(arr):
  arr.sort()
  if arr[0]==arr[1]:
    return arr[-1]
  else:
    return arr[0]

print(find_uniq([3,2,2,2,2]))

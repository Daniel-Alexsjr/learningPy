import string
def pangram(s):
  s = s.lower()
  s = ''.join(char for char in s if char.isalpha())
  return set(s) == set(string.ascii_lowercase)

print(pangram("The quick, brown fox jumps over the lazy dog!"))



#import string

def is_pangram(s):
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True

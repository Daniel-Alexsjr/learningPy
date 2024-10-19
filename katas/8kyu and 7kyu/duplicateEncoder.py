def duplicate_encode(word):
    return "".join(["(" if word.lower().count(l)==1 else ")" for l in word.lower()])

print(duplicate_encode("din"))
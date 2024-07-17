import re
def to_underscore(name):
    name_with_underscore = re.sub(r'(?<=[a-z0-9])([A-Z0-9])', r'_\1', name)
    return re.sub(r'__', r'_', name_with_underscore)

print(to_underscore("camelCase"))
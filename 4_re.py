import re

# . (ca.e): .은 문자를 의미> care,cafe
# ^ (^de): ^은 시작을 의미> desk, dessert
# $ (se$): $는 끝을 의미> case, base

p = re.compile('ca.e')      
m = p.match('care')

print(p.search('good care cafe'))
print(p.findall('good care cafe'))
print()

def print_match(m):
    if m :
        print(m.group())
        print(m.string)
        print(m.start())
        print(m.end())
    else:
        return '매칭되지 않음'
print_match(m)

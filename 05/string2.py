s11= '<><abc><><><defg>'
print(s11.strip('<>'))
# strip 하나 제거
s13 = 'King and Queen'
print('-----', s13.center(30), '-----')
print('-----', s13.ljust(30), '-----')
print('-----', s13.rjust(30), '-----')
s14=str.split('chicken and hen', 'and')
print(s14)

lines = '''
asdf
qwer
zxcz
'''

print(lines.splitlines())

# 판별
print("1234".isnumeric())
print("abcd".isalpha())
print("ABCD".isupper())
print("Abcd".isdigit())
print("abcd \n   csdcsd".isspace())

# format_map
name2 = 'sdsdsd'
print('name:{n}'.format_map({'n':name2}))

# 0 채우기





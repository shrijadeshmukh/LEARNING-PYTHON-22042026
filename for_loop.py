name = 'World'
character='+'
print(character+name+character)
for char in name:
    char = char + '     '
    print(char+char)
print(character+name+character)

###another test case
name = 'World'
space = ''
for char in name:
    space += ' '
    print(space + char)
####
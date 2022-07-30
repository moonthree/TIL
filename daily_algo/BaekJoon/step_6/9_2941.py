letter = input()
if letter.count('c=') > 0:
    letter = letter.replace('c=', 'c', letter.count('c='))
if letter.count('c-') > 0:
    letter = letter.replace('c-', 'c', letter.count('c-'))
if letter.count('dz=') > 0:
    letter = letter.replace('dz=', 'c', letter.count('dz='))
if letter.count('d-') > 0:
    letter = letter.replace('d-', 'c', letter.count('d-'))
if letter.count('lj') > 0:
    letter = letter.replace('lj', 'c', letter.count('lj'))
if letter.count('nj') > 0:
    letter = letter.replace('nj', 'c', letter.count('nj'))
if letter.count('s=') > 0:
    letter = letter.replace('s=', 'c', letter.count('s='))
if letter.count('z=') > 0:
    letter = letter.replace('z=', 'c', letter.count('z='))


print(len(letter))
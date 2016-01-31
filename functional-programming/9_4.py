def pig_latin(word):
    if word[0] in 'aeiou':
        print(word + 'way')
    else:
        print(word[1:] + word[0] + 'ay')

f = open('C:/PMP/functional-programming/translate.txt')

lines = f.readlines()

"""
for line in lines:
    for word in line.split():
    	pig_latin(word)
"""

[pig_latin(word) for line in lines for word in line.split()]
##def reverse(x):
##    if len(x) % 2 == 0:
##        y = int(len(x)/2)
##    else:
##        y = int((len(x) - 1)/2)
##    letters = []
##    for j in range(len(x)):
##        letters.append(x[j])
##    for i in range(y):
##        letters[i], letters[-1-i] = letters[-1-i], letters[i]
##    return ''.join(letters)
##
##def anti_vowel(x):
##    letters = []
##    for i in range(len(x)):
##        if x[i] != 'a' and x[i] != 'e' and x[i] != 'i' and x[i] != 'o' and x[i] != 'u' and x[i] != 'A' and x[i] != 'E' and x[i] != 'I' and x[i] != 'O' and x[i] != 'U':
##            letters.append(x[i])
##    return ''.join(letters)
##
##score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
##         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
##         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
##         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
##         "x": 8, "z": 10}
##def scrabble_score(x):
##    x = x.lower()
##    points =[]
##    for i in range(len(x)):
##        points.append(int(score[x[i]]))
##    return sum(points)
##
##def censor(x, y):
##    z = len(y)*'*'
##    return x.replace(y, z)
##
##def count(s, i):
##    x=0
##    for m in range(len(s)):
##        if s[m] == i:
##            x += 1
##    return x
##
##def purify(x):
##    evens = []
##    for i in range(len(x)):
##        if x[i] % 2 == 0:
##            evens.append(x[i])
##    return evens
##
##def product(x):
##    y = 1
##    for i in range(len(x)):
##        y *= x[i]
##    return int(y)
##
##def remove_duplicates(x):
##    singles = []
##    for i in range(len(x)):
##        if x[i] not in singles:
##            singles.append(x[i])
##    return singles
##
##def median(x):
##    if len(x) % 2 != 0:
##        x.sort()
##        y = int((len(x)-1)/2)
##        return x[y]
##    else:
##        x.sort()
##        y = int((len(x)/2)-1)
##        z = int((len(x)/2))
##        return (x[y] + x[z])/2
##

# takes input strings a, b and calculates number of deletions required
#   to make the two anagrams of each other

def number_needed(a, b):
    c = [0] * 26
    d = [0] * 26
    e = [0] * 26
    for i in range(0,26):
        c[i] += a.count(chr(97+i))
    for j in range(0,26):
        d[j] += b.count(chr(97+j))
    for k in range(0,26):
        e[k] = abs(d[k] - c[k])
    return sum(e)

a = input().strip()
b = input().strip()

print(number_needed(a, b))

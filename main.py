from string import punctuation
# read from file, remove caps and punctuation, and split into words
f = open('Machine learning.txt').read()
#size_to_read = 100
#f_contents = f.read(size_to_read)
#while len(f_contents) > 0:
    #print(f_contents, end='')
f = f.lower()
for p in punctuation:
    f = f.replace(p, '')
words = f.split()
#build the dictionary of frequencies
d = {}
for w in words:
    if w in d:
       d[w] = d[w] + 1
    else:
        d[w] = 1
# print in alphabetical order
items = list(d.items())
items.sort()
for i in items:
    print(i)
# print in order from least to most common
items = list(d.items())
items = [(i[1], i[0]) for i in items]
items.sort()
for i in items:
    print(i)

print(f.closed)

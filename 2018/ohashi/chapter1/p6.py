def n_gram(text, n):
    return [' '.join(text[i:i+n]) for i in range(len(text) - n + 1)]

a = [x for x in 'paraparaparadise']
b = [x for x in 'paragraph']

X = set(n_gram(a, 2))
Y = set(n_gram(b, 2))

print(X | Y)
print(X & Y)
print(X - Y)

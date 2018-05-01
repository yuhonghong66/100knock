with open('hightemp.txt', encoding='utf-8') as f:
    lines = [x for x in f]

count = {}
for line in lines:
    try: count[line.split()[0]] += 1
    except: count[line.split()[0]] = 1


def comp(x):
    return count[x.split()[0]] + 1e-6*sum(ord(x) for x in x.split()[0])

lines.sort(key=comp)

for l in lines:
    print(l.replace('\n', ''))
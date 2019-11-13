import itertools
import operator
l1sorted = sorted((tuple(line.strip().split(','))
                   for line in open("routers.txt")), key=lambda x: x[1])
print(l1sorted)
for item in l1sorted:
    print(item[0]+','+item[1])

it = itertools.groupby(l1sorted, operator.itemgetter(1))
print(list(it))

it = itertools.groupby(l1sorted, operator.itemgetter(1))
for key, group in it:
    print(f"key={key}, group:{list(group)}")

print("-"*80)
it = itertools.groupby(l1sorted, operator.itemgetter(1))
dict1 = {}
for k, v in it:
    print(k, v)
    dict1.update({k: [item[0] for item in v]})
    print(dict1)

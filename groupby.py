l1=[]

for line in open("routers.txt"):
    l1.append(tuple(line.strip().split(',')))

l1sorted = sorted(l1, key=lambda x: x[1])
print(l1sorted)

for item in l1sorted:
    print(item[0]+','+item[1])
from itertools import combinations as comb


count = int(0)
n, p = (int(_) for _ in input().split())
a = (int(i) for i in input().split())

for bag in range(1, n+1, 1):
    print(bag)
    c = 0
    print(c)
    list_bag = list(comb(a, bag))
    for c in range(0, len(list_bag)):
        print(list_bag[c])

print("what the fuck")

from itertools import combinations as comb


count = int(0)
n, p = [int(_) for _ in input().split()]
a = [int(i) for i in input().split()]

for bag in range(0, n+1, 1):
    list_bag = list(comb(a, bag))
    for c in range(0, len(list_bag)):
        s = sum(list_bag[c]) % 2
        if s == p:
            print(list_bag[c])
            count += 1

print("count: %s" % count)

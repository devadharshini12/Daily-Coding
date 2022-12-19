#First Positive Integer
p = [int(i) for i in input().split()]
for i in range(min(p), max(p)+1):
    if i not in p and i > 0:
       print(i)
       break
else:
    print(max(p)+1)
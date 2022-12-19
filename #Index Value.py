#Index Value
m=list(map(int, input().split()))
n=[] 
for i in m:
    x=1 
    for j in m:
        if j==i: 
           continue
        else:
           x*=j 
    n.append(x)
print(n)
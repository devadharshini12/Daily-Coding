#pentagon function
n=int(input())
count=1
if(n==1):
    print(n)
else:
    for i in range(1,n):
        count=count + 5*i
print(count)
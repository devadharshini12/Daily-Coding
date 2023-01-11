#Auto Complte sys
a=list(input().split())
b=input().strip()
c=len(b)
for i in a:
    if i[:c]==b:
        print(i,end=" ")
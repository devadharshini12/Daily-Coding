#Additive Equivalent
d=list(map(int, input(). split()))
k=int(input()) 
for i in d: 
    for j in d: 
        if i+j == k: 
           res = "True" 
           break 
        else:
           res = "False" 
print("True")
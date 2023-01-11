#Disarium No
def is_disarium(n):
    s=str(a)
    ln=len(s)
    c=0
    for i in range(0,ln):
        m=(int(s[i]))**(i+1)
        c+=m
    if(c==a):
        print("True")
    else:
        print("False")
a=int(input())
is_disarium(a)
#Longest Substring

k = int(input())
s = input()
x = ""
list = []
for i in s:
    x += i
    if len(set(x)) < k:
        continue
    if len(set(x)) > k:
        a=x[0]
        x=x.replace(a,'')
        continue
    if len(set(x)) == k:
        list.append(x)
print(max(list))
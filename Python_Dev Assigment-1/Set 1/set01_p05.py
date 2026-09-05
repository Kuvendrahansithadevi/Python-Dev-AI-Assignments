print("a = ",end=" ")
a = list(map(int,input().split()))
print("b = ",end=" ")
b = list(map(int,input().split()))
i=0
j=0
res=[]
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        res.append(a[i])
        i+=1
    else:
        res.append(b[j])
        j+=1
if i!=len(a):
    while i<len(a):
        res.append(a[i])
        i+=1
if j!=len(b):
    while j<len(b):
        res.append(b[j])
        j+=1
print(res)
print("Enter array elements :")
arr=list(map(int,input().split()))
print("Enter k :")
k=int(input())
for i in range(len(arr)):
    while k:
        val=arr.pop(0)
        arr.append(val)
        k-=1
print(arr)
import array
arr=array.array('i',[6,12,4,0,15,8,3,20])
print("Total runs :",sum(arr))
print("Highest over :",max(arr))
print("Lowest over :",min(arr))
print("Average per over :",sum(arr)/len(arr))
print("Maiden overs :",arr.count(0))
print("Bytes used :",arr.itemsize*len(arr))
arr=list(map(int,input().split()))
set_arr=set(arr)
new_arr=list(set_arr)
max_num=max(new_arr)
new_arr.remove(max_num)
if len(new_arr)==0:
    print("No second largest")
else:
    print("Second largest = ",max(new_arr))
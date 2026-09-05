count=0
def counter():
    global count
    count+=1
    print(count,end=" ")
print("Version A:",end=" ")
counter()
counter()
counter()
print()
def create_counter():
    count=0
    def counter():
        nonlocal count
        count+=1
        print(count,end=" ")
    return counter
print("Version B:",end=" ")
cnt=create_counter()
cnt()
cnt()
cnt()
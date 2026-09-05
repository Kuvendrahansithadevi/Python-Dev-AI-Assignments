x="I am global"
def outer():
    y="I am enclosing"
    def inner():
        x="I am local"
        print("Local :",x)
        print("Enclosing :",y)
    inner()
outer()
print("Global :",x)
print("Built-in : ",len([1,2,3,4,5]))
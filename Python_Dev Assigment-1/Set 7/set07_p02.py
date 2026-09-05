def compose(f,g):
    def operation(x):
     return f(g(x))
    return operation
add_one=lambda x:x + 1
double=lambda x:x*2
f=compose(add_one,double)
print(f(5))
g=compose(double,add_one)
print(g(5))
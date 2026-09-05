#------A------
"""
Predicted:
10
20
"""
x = 10
def f():
    print(x)
    x = 20
f()
"""
output: error
cannot access local variable without declaring since the variable declared after print we can't access.
"""
#------B------
"""
predicted: 10
"""
x = 5
def f(x):
    x = 10
f(x)
print(x)

"""
output: 5
The function is just called it modifies x value only in the function, the print statement was 
outside the function so it considers global value.
"""
#------C------
"""
Predicted:
enclosing
"""
x = "global"
def outer():
    x = "enclosing"
    def inner():
        print(x)
    inner()
outer()

"""
output: enclosing
The inner function is called inside the outer function
so it access the x as local variable.
"""
#------D------
"""
Predicted: 99
"""
if True:
    z = 99
print(z)
"""
output: 99
if true is always true statement, so the z was declared and printed.
"""
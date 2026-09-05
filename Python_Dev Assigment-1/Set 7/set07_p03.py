def add(a,b): a+b
def sub(a,b): a-b
def mul(a,b): a*b
def div(a,b): a/b if b!=0 else "Error: divide by zero is not defined"
operations={'+':add,'-':sub,'*':mul,'/':div}
def calculate(a,op,b):
    func=operations.get(op)
    if func is None:
        return f"Unknown operator: {op}"
    return func(a,b)
for op in ['+','-','*','/','%']:
    print(f"10 {op} 3=",calculate(10,op,3))
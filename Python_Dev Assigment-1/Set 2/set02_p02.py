def calculator(a,b,op="+"):
    if op=="+":
        print(a+b)
    elif op=="-":
        print(a-b)
    elif op=="*":
        print(a*b)
    elif op=="/":
        if b==0:
            print("Error: cannot divide by zero")
        else:
            print(a/b)
    else:
        print(f"Error: unknown operator '{op}'")
calculator(10,5)
calculator(10,5,"-")
calculator(10,5,"*")
calculator(10,0,"/")
calculator(10,5,"%")
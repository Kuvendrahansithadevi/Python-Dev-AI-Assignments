def report(name,*marks,**details):
    print(f"Student : {name}")
    for key,value in details.items():
        print(f"{key} : {value}")
    print("Marks : ",end="")
    last=marks[-1]
    for i in marks:
        if i==last:
            print(i)
        else:
            print(i,end=", ")
    print("Total : ",sum(marks))
    print("Average : ",sum(marks)/len(marks))
    avg=sum(marks)/len(marks)
    print("Result :","PASS" if avg>=40 else "FAIL")
report("Priya",85,92,78,90,section="A",year=2)
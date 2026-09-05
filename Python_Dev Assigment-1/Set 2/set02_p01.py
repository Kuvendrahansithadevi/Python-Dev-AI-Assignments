def place_order(customer,*items,**charges):
    print("Customer :",customer)
    print(f"Items ordered ({len(items)}) :")
    for i in range(len(items)):
        print(f"{i+1}. {items[i]}")
    print("Charges:")
    for key,value in charges.items():
        print(key,":",value)
place_order("Ravi","Biryani","Coke","Gulab Jamun",delivery=40,gst=25,discount=50)
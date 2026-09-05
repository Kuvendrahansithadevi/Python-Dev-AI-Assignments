total_seats=100
seats=total_seats
def book(val):
    global seats
    if val>seats:
        print(f"Only {seats} seats left. Booking failed")
    else:
        seats-=val
        print(f"Booked {val} seats. Remaining: {seats}")
def cancel(val):
    global seats
    seats+=val
    print(f"Cancelled {val} seats. Remaining: {seats}")
def status():
    print(f"{seats} seats available out of {total_seats}")
book(3)
book(10)
book(200)
cancel(5)
status()
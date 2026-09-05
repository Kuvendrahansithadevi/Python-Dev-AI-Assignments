def add_to_cart(item, cart=[]):
    cart.append(item)
    return cart

print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))
"""Everytime the cart is not getting empty instead storing all the items.
To fix this we need to take an empty cart inside the function."""
def add_to_cart(item):
    cart=[]
    cart.append(item)
    return cart
print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))
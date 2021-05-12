Q = int(input("Order quantity Q: "))
R = int(input("Reorder point R: "))
I = int(input("Initial inventory I: ")) 
print("Inventory: " + str(I))

while True: #因為每天都要跑，所以讓他無窮迴圈
    sales = int(input("Sales in a day: ")) 
    I=I-sales if I-sales>=0 else 0 
if I<R:
    I=I+Q
print("Inventory: " + str(I))
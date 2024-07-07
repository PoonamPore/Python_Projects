size=input("what size of pizza you want S/M/L? ")
bill =0

if size=='s'or size=='S':
    bill+=100
    print("small pizza price is 100")
elif size=='M'or size=='m':
    bill+=200
    print("medium pizza price is 200")
else:
    bill+=300
    print("large pizza price is 300")

add_pepricon=input("Do you want pepricon Y/N? ")
if add_pepricon=='Y' or add_pepricon=='y':
    if size=='s' or size=='S':
       bill+=30
    else:
        bill+=50
extra_cheese=input("Do you want extra_cheeseY/N? ")
if extra_cheese=='y' or extra_cheese=='Y':
    bill+=20
print(f"your total bill is {bill}")


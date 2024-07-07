import random

User_choice=int(input("Enter Your Choice: Type 0 for Rock,1 for Paper,2 for Scissor"))
if User_choice >=3 or User_choice<0:
    print("Invalid choice,you lose")
else:
    Computer_choice=random.randint(0,1)
    print("computer_choice: ")
    print(Computer_choice)
    if User_choice==Computer_choice:
        print("It's Draw")
    elif User_choice==0 and Computer_choice==2:
        print("you win")
    elif User_choice==2 and Computer_choice==0:
        print("you lose")
    elif User_choice > Computer_choice:
        print("you win")
    elif Computer_choice >User_choice:
        print("you lose")



import random
def roll_dice():
    print("The number is:")
    x=random.randint(1,6)
    print(x)
    choice=input("Enter choice:")
    if(choice.lower()=='yes'):
        roll_dice()
roll_dice()
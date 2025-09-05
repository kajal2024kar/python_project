import random
import os
while True:
    ops = ["Rook","Paper","Scisser"]
    buttom = [1,2,3]
    print("\n\n\tWelcome To\n Rock🪨, Paper🗞️, Scissors✂️ ")
    comp = random.randint(1,3)
    print("\n1.Rock🪨\n2.paper🗞️\n3.Scissors✂️")
    cho = int(input("enter your choice : "))
    if cho in buttom:
        if((cho == 1 and comp ==3)or(cho == 2 and comp == 1)or(cho == 3 and comp == 2)):
            print(f"\nYOU WIN 😥  compute choose {ops[comp-1]}")
        elif((cho == 2 and comp == 3)or(cho ==1 and comp == 2)or(cho == 3 and comp == 1)):
            print(f"You Lose 😎  compute choose {ops[comp-1]}")
        else:
            print("You Drow😐") 
    else:
        print("Invlide option !.......")
    agein = input("\n\nDo you wanna play agein ?\nPress👆 'Space' for yes\nPress👆 any key for no\n : " )  
    if(agein == " "):
        break       
    os.system("cls")       
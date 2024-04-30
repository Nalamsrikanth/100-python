import random
list = ["rock", "paper", "scissor"]
num = int(input("enter your number 0 for rock,1 for paper, 2 for scissor"))
my_selection = list[num]
print(f"{list[num]}")
computer = random.randint(0, 1)
com_selection = list[computer]
print(f"{list[computer]}")
if list[num] != list[computer]:
    if list[num] == "rock" and list[computer] == "scissor":
        print("you win")
    elif list[num] == "paper" and list[computer] == "rock":
        print("you win")
    elif list[num] == "scissor" and list[computer] == "paper":
        print("you win")
    elif list[num] == "scissor" and list[computer] == "rock":
        print("you loss")
    elif list[num] == "rock" and list[computer] == "paper":
        print("you loss")
    elif list[num] == "paper" and list[computer] == "scissor":
        print("you loss")
    else:
        print("you loss")
else:
    print("its draw")









print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this lin
if size == "s":
  bill = int(15)
  if add_pepperoni =="y":
    bill += int(2)
if size == "m":
  bill = int(20)
  if add_pepperoni =="y":
    bill += int(3)
if size == "l":
  bill = int(25)
  if add_pepperoni =="y":
    bill += int(3)

if extra_cheese =="y":
  bill += int(1)
print(f"Your final bill is: {bill}.")
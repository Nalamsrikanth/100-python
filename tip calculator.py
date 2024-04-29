print("Welcome to the tip calculator!")
b = (input("What is the total bill?"))
bill = float(b)
tip = int(input("How much tip would you like to give ? 10,12, or 15?"))
total_bill = (bill * (tip / 100))
t_bill = bill + total_bill
t_person = int(input("How many people to split the bill?"))
final_bill = t_bill / t_person
f_b = round(final_bill,2)
print(f"Each person should pay: {f_b}")

name1 = input()
name2 = input()

st = name1 + name2
lower_names = st.lower()
t = lower_names.count("t")
r = lower_names.count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t+r+u+e
l = lower_names.count("l") #.count() is used to count the number of words mention in the brackets.
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
sec_digit = l+o+v+e

love = int(str(first_digit)+str(sec_digit))

print(f" your love percentage is {love}")
if love<= 10 or love>= 90:
    print(f"Your score is {love}, you go together like coke and mentos.")
elif love >= 40 and love <= 50:
    print(f"Your score is {love}, you are alright together.")
else:
    print(f"your score is {love}")
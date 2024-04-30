line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

w1 = position[0].lower()
abc = ["a", "b", "c"]
w1_index = abc.index(w1)
num_index = int(position[1])-1
map[num_index][w1_index] = "X"
print(f"{line1}\n{line2}\n{line3}")
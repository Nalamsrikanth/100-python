def paint_cal(height, width, cover):
    num_cans = (height * width)/cover
    cans = round(num_cans)
    print(f"you will need {cans} cans of paint")

test_h = int(input("enter the height"))
test_w = int(input("enter the width"))
coverage = 5
paint_cal(height=test_h, width=test_w, cover=coverage)
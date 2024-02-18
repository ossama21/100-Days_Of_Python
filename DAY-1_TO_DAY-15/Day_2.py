print("Welcome to my second day task, SER:)\nThis is a TIP Calculator.\n")
total=input("What was the total bill? ")
like=input("How much tip would you like to give? 10, 12, or 15? \n")
people=input("How many people to split the bill? ")
print("Each person should pay: ")

after_tip = (float(total) * (float(like) / 100) + float(total))
formatted_after_tip = f"{after_tip:.2f}"
print("yourfinal bill after tip is : \n", formatted_after_tip)

split= after_tip / int(people)
formatted_split = f"{split:.2f}"
print(f"each person should pay: {formatted_split}\n")
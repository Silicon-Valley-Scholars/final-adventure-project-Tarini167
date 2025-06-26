import random

def run_pace(opt):
    if opt == 1:
        print("You have chosen to jog!")
    else:
        print("You have chosen to sprint!")

print ("Welcome to Silicon Valley's Fun Run where you run up to 10 miles!")
name = input("Please enter your name contestant")
opt =int (input("Please enter 1 if you want to jog and 2 if you want to sprint"))
print("Hello" ,name, "Good luck on your run!")
run_pace(opt)

print("Before you start, look at your running belt to see what you have for your run.")
items = ["snacks", "water", "fitness gear"  ]
for each in items:
    if each == "snacks":
        print("You have some snacks!")
    else:
        print("You have" ,each +"!")
        
miles = random.randint (1,10)
print("Today you will be running" ,miles, "miles")

total_miles = 0
while total_miles < miles:
    total_miles = total_miles +1
    print("You have ran" ,total_miles,"miles")
print("Congrtulations, you have completed your run!!!!")
age=int(input("enter your age: ")) #enter the age from the user
calc=18-age #check the age gap
if age<0:
    print("inavlid input") #invalid in negative number
elif age<18:
    Pyear=int(input("enter the present year: ")) #ask only if the age is less than 18 and to check the voting year
    print(f"your are not eligible for vote after {calc} years in {Pyear+calc} you'r eligible for vote")
else:
    print("you are eligible for vote")

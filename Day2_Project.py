#Tip Calculator
print("Welcome to the tip calculator.")
bill = float(input("What is the total bill? $"))
tip = float(input("What percentage would you like to give as a tip?"))
people= int(input("How many people to split the bill?"))
tip_amount = bill * (tip / 100)
total = bill + tip_amount
each_person= (total/people)
print("Each person should pay: $",each_person)



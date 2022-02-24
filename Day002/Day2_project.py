#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

bill_amount = int(input("Enter the Bill amount: "))
tip_percent = int(input("enter the Tip Percent: "))
total = bill_amount + (bill_amount*tip_percent)/100
person = int(input("Enter number of person bill to be splited into: "))
share = round((total/person),2)
print(f"Each individual share = {share}")
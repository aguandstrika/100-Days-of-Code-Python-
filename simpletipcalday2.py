#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: You might need to do some research in Google to figure out how to do this.

#Welcome splash
print("Weclome bloke to the tip calculator")
# total bill $$$
sub_total_bill = input("what was the total bill: ")
# the percentage amount 10, 12, 15
tip_percentage = input("what percentage tip would you like to give? 10,12, or 15: ")
# how many people to split the bill with
people = input("how many people in the party to split the bill: ")


percentage = float(tip_percentage)/100
pertimbill = float(sub_total_bill) * percentage
tipplubill = pertimbill + float(sub_total_bill)
totalbillsplit = tipplubill / float(people) 

print(round(totalbillsplit, 2))

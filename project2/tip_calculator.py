#Welcome to the tip calculator
print("Welvome to the tip calculator!")
#What was the total bill? $124.56
total_bill = float(input("What was the total bill? "))
#What percentage tip would you like to give? 10, 12 or 15? 12
percentage = int(input("What is the percentage?"))
percentage_bill = percentage / 100 + 1
#if percentage == 10:
 #   percentage = 1.10
#if percentage == 12:
 #   percentage = 1.12
#if percentage == 15:
 #   percentage = 1.15 
#How many people to split the bill? 7
people =  int(input("How many people?"))
#Each person should pay: $19,93
for_each = round((total_bill / int(people) * percentage_bill) , 2)
for_each = "{:.2f}".format(total_bill / int(people) * percentage_bill)

print(for_each)
# print(percentage_bill)
# print(f'{num_1_float}/{num_2_float}=', num_1_float / num_2_float)
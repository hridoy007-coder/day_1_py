rent = int(input("enter your rent: "))
food = int(input("enter your amount of your food order: "))
electricity_spend = int(input("enter the total of electricity spend: "))
charge_per_unit = int(input("enter the charge per unit: "))
persons = int(input("enter the number of persons: "))

total_bill = electricity_spend * charge_per_unit

output = (food + rent + total_bill) / persons

print("each person will pay = ", output)
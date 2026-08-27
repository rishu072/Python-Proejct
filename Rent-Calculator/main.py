#---> Input user
# total rent
# total food order for snacking
#Electricity unit spend
#charge per unit
#Persons living in room.

## Output
# Total amout u have to pay.

rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amout of food ourder = "))
ele_speed = int(input("Enter the charge pr unit = "))
charge_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the number of persons living in room/flat = "))

total_bill = ele_speed * charge_per_unit

output = (food + rent + total_bill)// person

print("Each person will pay = ", output)


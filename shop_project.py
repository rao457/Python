SUGAR = 80
RICE = 150
FLOUR = 50

result1 = 0
result2 = 0
result3 = 0
def how_much():
    how = int(input("How much, Sir/Ma'am? "))
    return how
def cost_calculate(unit_price, quantity):
    return unit_price*quantity
while True:

    ask_costumer = input("What can I serve you (Sugar, Rice, Flour)? ").lower()
    if ask_costumer == 'q':
        break
    elif ask_costumer in ['sugar','rice', 'flour']:
        quantity = how_much()
        if ask_costumer == 'sugar':
        
            result1 += cost_calculate(quantity,SUGAR)
        elif ask_costumer == 'rice':
        
            result2 += cost_calculate(quantity,RICE)
        elif ask_costumer == 'flour':
        
            result3 += cost_calculate(quantity, FLOUR)
    else:
        print("Invalid Item Please select from available ones.")

    
# BILL
total_bill = result1+result2+result3
if total_bill > 0:
    print(f"Your Total Bill is {total_bill}")
else:
    print("You haven't purchased anything.")
print("****Thank You For Shopping Here****")

"""
Week 2 Assignment: Smart Shopping Cart Calculator
Variant: 2
Student Name: Oktyabrov Umrbek https://yangibaev.com/courses/itp/week2/assignment/123
Date: 08.10.2025
Description: This is a shopping cart program that calculates the final price based on multiple discount rules and membership status
"""

n1 = input("Please, enter the name of the first dish: ")
p1 = float(input("Please, enter the price of the first dish: "))
q1 = int(input("Please, enter the quantity of the first dish: "))
n2 = input("Please, enter the name of the second dish: ")
p2 = float(input("Please, enter the price of the second dish: "))
q2 = int(input("Please, enter the quantity of the second dish: "))
n3 = input("Please, enter the name of the third dish: ")
p3 = float(input("Please, enter the price of the third dish: "))
q3 = int(input("Please, enter the quantity of the third dish: "))

subtotal_before_discounts = p1*q1 + p2*q2 + p3*q3

n = input("Please, enter your name: ")
ID = input("Do you have a student ID(yes/no): ")
o_t = int(input("Enter the order time in 24-hour format(e.g: 11; 12; 13...): "))

is_s = 'yes' in ID
is_h_d_t = o_t >= 14 and o_t <= 17
l_o_d = subtotal_before_discounts >= 150000

student_discount = is_s * .15 * subtotal_before_discounts
happy_hour = is_h_d_t * .2 * subtotal_before_discounts
is_main_dis = is_s * is_h_d_t
main_discount = (student_discount * (student_discount >= happy_hour) + happy_hour * (happy_hour > student_discount)) * is_main_dis
large_order_dis = l_o_d * .05 * subtotal_before_discounts

after_disses = subtotal_before_discounts - large_order_dis - main_discount - (happy_hour + student_discount) * (not is_main_dis)

after_service_charge = after_disses + after_disses * .1
delivery = (after_service_charge >= 100000) * 15000
final = after_service_charge - delivery
print('\n\n'+'='*50)
print(' '*15+'CHEQUE INFORMATION')
print('='*50)
print(f'Customer name: {n}    Student status: {ID}')
print(f'Order Time: {o_t}')
print('='*50)
print("YOUR ORDERS:")
print(f"1. {n1}\nPrice of each: {p1:.2f}   Quantity: {q1}")
print(f"2. {n2}\nPrice of each: {p2:.2f}   Quantity: {q2}")
print(f"3. {n3}\nPrice of each: {p3:.2f}   Quantity: {q3}")
print(f"Total price: {subtotal_before_discounts:.2f}")
print('='*50)
print(f"DISCOUNTS\n1. Student discount eligibility: {is_s}   Amount: {student_discount:.2f}")
print(f"2. Happy hour eligibility: {is_h_d_t}   Amount: {happy_hour:.2f}")
print(f"Applied discount: {('The larger one'*is_main_dis) or ('First'*(not is_main_dis)*is_s) or ('Second'*(not is_main_dis)*is_h_d_t)}")
print(f'Large order discount eligibility: {l_o_d}   Amount: {large_order_dis:.2f}')
print(f'Total discounts: {(large_order_dis + main_discount + (happy_hour + student_discount) * (not is_main_dis)):.2f}')
print('='*50)
print(f"Subtotal after discounts: {after_disses:.2f}")
print(f"Service charge amount: {(after_disses * .1):.2f}")
print(f"Delivery status and fee: {after_service_charge >= 100000}; {delivery:.2f}")
print(f"FINAL PRICE: {final:.2f}")
print(f"Total amount saved: {(subtotal_before_discounts - final):.2f}")
print('='*50)
print('='*50)
"""
Week 2 Assignment: Smart Shopping Cart Calculator
Variant: 2
Student Name: Oktyabrov Umrbek https://yangibaev.com/courses/itp/week2/assignment/123
Date: 08.10.2025
Description: This is a shopping cart program that calculates the final price based on multiple discount rules and membership status
"""

d_n = input("Please, enter the dish name: ")
p = input("Please, enter the price: ")
q = input("Please, enter the quantity: ")
subtotal_before_discounts = p*q
n = input("Please, enter your name: ")
ID = input("Do you have a student ID(yes/no): ")
o_t = input("Enter the order time in in 24-hour format: ")
is_s = 'yes' in ID
h_d_t = o_t >= 14 and o_t <= 17
l_o_d = subtotal_before_discounts >= 150000
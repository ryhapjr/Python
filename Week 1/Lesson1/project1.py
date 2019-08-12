# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 19:10:36 2019

@author: Randy Jr
"""

restaurant_name="Tim Hortons"
address="\nStaten Island, NY, 10314"
phone= "\n(718) - 370 - 2555"

print(restaurant_name, address, phone)

item_1=input("Please enter the item 1: ")
item_1_price = float(input("Please enter the price for "))

item_2=input("Please enter the item 2: ")
item_2_price= float(input("Please enter the price for "))


item_3=input("Please enter the item 3: ")
item_3_price= float(input(" Please enter the price for"))

item_4=input("Please enter the item 4: ")
item_4_price= float(input("Please enter the price for "))

subtotal = item_1_price + item_2_price + item_3_price + item_4_price
tax_rate=8.75/100
tax=subtotal * tax_rate
subtotal= tax + subtotal


print("Subtotal: ", subtotal)

cash= float(input("Please enter cash amount"))
grand_total = cash - subtotal


print("grand total: ", grand_total)
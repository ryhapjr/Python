store = {
    'name': 'Tim Hortons',
    'address': '55 Bay Street,Staten Island,New York 10301',
    'phone': '111-111-1111'
}

print(store['name'])
print(store['address'])
print(store['phone'])

items = []
items_price = []

items.append(input('Please enter the item 1 : '))
items_price.append(float(input('Please enter the price for item 1 : ')))

items.append(input('Please enter the item 2 : '))
items_price.append(float(input('Please enter the price for item 2 : ')))

items.append(input('Please enter the item 3 : '))
items_price.append(float(input('Please enter the price for item 3 : ')))

sub_total = items_price[0] + items_price[1] + items_price[2]

sales_tax = 8.878 / 100
sales_tax = sub_total * sales_tax
grand_total = sales_tax + sub_total
change = float(input('Please insert your cash amount: '))
received_money = change - grand_total

print(items)
print(items_price)
print(sub_total)
print(grand_total)
print(round(received_money, 2))

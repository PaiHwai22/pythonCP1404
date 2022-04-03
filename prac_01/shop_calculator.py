"""Calculate total price of items from user's amount and price of items.
Apply 10% discount for total over $100"""

number_of_items = int(input("Number of items: "))
while number_of_items < 0:  # get valid number
    print("invalid number of items!")
    number_of_items = int(input("Number of items: "))

price_of_item = 0
total_price = price_of_item

for i in range(0, number_of_items):
    price_of_item = float(input("Price of item: "))
    total_price += price_of_item
if total_price > 100:
    total_price = (total_price / 100) * 90  # applies discount
print(f"total price for {number_of_items} items is ${total_price}")

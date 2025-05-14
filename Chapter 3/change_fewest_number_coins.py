purchase_price_of_item = float(input("enter purchase price: "))


if purchase_price_of_item > 1.00:
	print("enter lesser purchase price: ")
else:
	
	change = round((1.00 - purchase_price_of_item) * 100)
   
quarters = change // 25
change = change % 25

dimes = change // 10
change = change % 10

nickels = change // 5
change = change % 5

pennies = change

print("your change is:")
print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)


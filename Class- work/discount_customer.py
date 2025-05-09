total_spending = int(input("Enter your purchasing amount: "))

purchase_between_1000_10000 = float(5/100) * total_spending

new_discount_amount_1000_10000 = int( total_spending - purchase_between_1000_10000 )

purchase_between_10000_50000 = float(10 /100) * total_spending

new_discount_amount_10000_50000 = int(total_spending - purchase_between_10000_50000)

purchase_between_above_50000 = float(20 / 100) * total_spending

new_discount_amount_above_50000  = int(total_spending - purchase_between_above_50000 )


	#print("invalid purchaseing amount")	
if total_spending >= 1000 and total_spending < 10000:
	print(f" you recieved  %5 discount for this package : {purchase_between_1000_10000: .2f}$ ")
	print(f" your new discount amount is: {new_discount_amount_1000_10000:,.2f}$ ")
	

if total_spending >= 10000 and total_spending < 50000:
	print(f" you recieved %10 discount for this package : {purchase_between_10000_50000:,. 2f}$ ")
	print(f" your new discount amount is: {new_discount_amount_10000_50000:,. 2f}$")

if total_spending >= 50000:
	print(f" you recived %20 discount for this package : {purchase_between_above_50000:,. 2f}$ ") 
	print(f" your new discount amount is: {new_discount_amount_above_50000:, 2.f }$ ")

 
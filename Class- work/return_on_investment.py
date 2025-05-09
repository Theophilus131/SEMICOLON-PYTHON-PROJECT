"""
calculate the ROI for an investment for a given number of years and interest rate.
write a program that prompt for the investment amount, number of years and interest rate and present the return on investment from years one to the given number of years.
"""

investment_amount = int(input("Enter investment amount: "))
number_years = int(input("enter the number of years: "))
interest_rate =float(input("Enter the interest rate: ")) / 100
return_on_investment = 0

for i in range(0, number_years, 1):
	interest = investment_amount * interest_rate 	
	return_on_investment += investment_amount 
	print(f" Return on investment over the {i + 1} years is {return_on_investment}")


 
	


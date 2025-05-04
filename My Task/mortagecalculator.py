principal = float(input("Enter amount you wish to borrow"))

annual_interest_rate = float(input("enter yearly interest rate"))

duration = float(input("enter mortgage duration"))

percentage_monthly = float(annual_interest_rate / 100)

monthly_rate = float(percentage_monthly / 12)

year_duration = float(duration * 12)


monthly_payment = float(principal * monthly_rate * ((1 + monthly_rate) ** year_duration)) / ((1 + monthly_rate) **( year_duration) - 1)
    

print(f" your Monthly Mortgage payment: ${monthly_payment}")
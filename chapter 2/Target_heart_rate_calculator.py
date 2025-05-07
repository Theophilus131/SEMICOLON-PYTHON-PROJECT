age = int(input("Enter your age:"))

maximum_heart_rate = 220 - age
 	
first_target_heart_rate = maximum_heart_rate * 50 / 100

second_target_heart_rate = maximum_heart_rate * 85 / 100


print(f"The maximum heart rate is {maximum_heart_rate} and the target heart is {first_target_heart_rate} to {second_target_heart_rate}")
	
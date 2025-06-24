Tasks = [] 


def main_menu():
	while True:
		message = """
                 My To do list Menu options:
                 Enter your choice:
                1.  Add a task
		2.  view all tasks
		3.  Mark a task as complete
		4.  delete a task
		00. Exit from stores
		"""
		print(message)
		user = input("Enter the task: ")

		match user:
			case "1": add_a_task_menu()

			case "2": view_all_tasks_menu()

			case "3": mark_a_task_as_complete_menu()

			case "4": delete_a_task_menu()

			case "00": 
				print("Exiting store ")
				break
			case _: print("Invalid input. Try again.")
			
def add_a_task_menu():
	while True:
		message = """
		1. add a task
		
		0. Back
		
		"""
		print(message)
		user = input("Enter the task: ")

		match user:
			case "1": 
				add = input("add what you want to add: ")
				Tasks.append(add)
				print(" task added")
			
			case "0": 
				print("Exiting store ")
				break
			case _: print("Invalid input. Try again.")


def view_all_tasks_menu():
	while True:
		message = """
		1. view tasks

		0. Back
		
		"""
		print(message)
		user = input("Enter a number to select: ")

		match user:
			case "1":
				print("here are your tasks: ")
				for index, task in enumerate(Tasks):
					print(f"{index}.{task}")
			
			case "0": 
				print("Exiting store ")
				break
			case _: print("Invalid input. Try again.")



def mark_a_task_as_complete_menu():
	while True:
		message = """
		1. Mark tast as complete

		0. Back
		
		"""
		print(message)
		user = input("Enter a number to select: ")

		match user:
			case "1":
				 print("mark task as complete")
			
			case "0": 
				print("Exiting store ")
				break
			case _: print("Invalid input. Try again.")


def delete_a_task_menu():
	while True:
		message = """
		1. Delete a task
		0. Back
		
		"""
		print(message)
		user = input("Enter a number to select: ")

		match user:
			case "1":
				delete = input("enter index of task to delete: ")
				if delete.isdigit():
					delete = int(delete)
				if 0 <= delete < len(Tasks):
					Tasks.pop(delete)
					print("Deleted the task  ")
			
			
			case "0": 
				print("Exiting store ")
				break
			case _: print("Invalid input. Try again.")



		
main_menu()





def main_menu():
	while True:
		message = """
                 T-phils Nokia Menu Map:
                 Enter:
                 1 - Phone book
                 2 - Messages
                 3 - Chat
		 4 - Call register
		 5 - Tones
		 6 - Settings
		 7 - Call divert
		 8 - Games
		 9 - Calculator
		 10 - Reminders
		 11 - Clock
		 12 - Profiles
		 13 - Sim Service
                 00 - Exit
		"""
		print(message)
		choice = input("Enter a number to select: ")

		match choice:
			case "1":
				phonebook_menu()
			case "2":
				messages_menu()
			case "3":
				chart_menu()
			case "4":
				call_register_menu()
			case "5":
				tones_menu()
			case "6":
				settings_menu()
			case "7":
				call_divert_menu()
			case "8": games_menu()
			case "9": calculator_menu()
			case "10": reminders_menu()
			case "11": clock_menu()
			case "12": profiles_menu()
			case "13": sim_service_menu()
			case "00": 
				print("Exiting Nokia Menu. Goodbye!")
				break
			case _: print("Invalid input. Try again.")

def phonebook_menu():
	while True:
		menu = """
        PhoneBook Menu:
        1 - Search
        2 - service Nos.
	3 - Add name
    	4 - Erase
    	5 - Edit
    	6 - Assign tone
    	7 - Send b'card
    	8 - Option
    	9 - Speed dials
    	10- Voice tags
        0 - Back
        """
		print(menu)
		choice = input("Select option: ")

		match choice:
			case "1": print("Search selected")
			case "2":print("service Nos selected.")
            
			case "3": print("add name")
			case "4":print("erase")
			case "5": print("edit")
               
			case "6":  print("assign tone")
               
			case "7": print("snd b card")
                
			case "8":
				 while True:
						menu ="""
						option menu:
						1. type of view
						2.  memory status
						0. back	
						"""
						print(menu) 
						choice = input("select option")
			
						match choice:
							case "1": print("type of view")
                               
							case "2": print("memory status")
							
							case "0":
								break
							case _:
								print("Invalid input. Try again.")	                               
									
			case "9": print("speed dials")
								
			case "10": print("voice tags")
								

			case "0":
				break
			case _:
				print("Invalid input. Try again.")


def messages_menu():
	while True:
		menu = """
		Messages Menu:
	1 - Write message
        2 - Inbox
        3  - Outbox
        4  - Picture messages
        5  - Templates
	6  - Smileys
	7  - Message settings
	8  - Info service
	9  - Voice mailbox number
        10 - Service command editor
        0 - Back

        """
		print(menu)
		choice = input("Select option: ")

		match choice:
			case "1":  print("Write message selected.")
               
			case "2":  print("Inbox selected.")
               
			case "3": print("outbox")
                
			case "4": print("picture messages")
                
        
			case "5": print("templates")
			case "6": print("smileys")

			case "7": 
				while True:
					menu ="""
					message settings menu:
					1. Set
					2. common
					0. back	
					"""
					print(menu) 
					choice = input("select option")
			
					match choice:
						case "1": print("set")
                               
						case "2": print("common")
						
						
						case "0":
							break
						case _:
							print("Invalid input. Try again.")
			
			
			case "8": print("info service")

            
			case "9": print("voice mailbox number")
                
			case "10": print("service command editor")
                
			case "0":
				break
			case _:
				print("Invalid input. Try again.")

def chart_menu():
	while True:
		menu = """
		chart menu
		1 - chart
		0 - Back
		"""
		print(menu)
		choice = input("Select option: ")

		match choice:
			case "1": print("Chart.")
			case "0": 
				break
			case _:
				print("invalid input. ")



def call_register_menu():
	while True:
		menu = """
		Call Register Menu:

        1 - missed call
        2 - recieved call
        3  - dialled numbers
        4  - erase recent call
        5 - Show call duration
    	6 - Show call cost
    	7 - Call cost settings
    	8 - Prepaid credit
        0 - Back

        """
		print(menu)
		choice = input("Select option: ")

		match choice:

			case "1": print("missed call")

			case "2": print("recieved call")
            
			case "3": print("dialled numbers")
			case "4": print("erase recent call")
        
			case "5":
				while True:
					menu ="""
					Show call duration menu:
					1. Last call duration
					2 - All calls duration
					3 - Received calls duration
					4 - Dialled calls duration
					5 - Clear timers
					0 - Back

					"""
					print(menu) 
					choice = input("select option")
			
					match choice:
						case "1": print("Last call duration")
                               
						case "2": print("All calls duration")

						case "3": print("Received calls duration")
                               
						case "4": print("Dialled calls duration")

						case "5": print("Clear timers")
						
						case "0":
							break
						case _:
							print("Invalid input. Try again.")
 
				

			case "6": 
				while True:
					menu ="""
					Show call cost menu:
					1 - Last call cost
					2 - All calls cost
					3 - Clear counters
					0 - Back

					"""
					print(menu) 
					choice = input("select option")
			
					match choice:
						case "1": print("Last call cost")
                               
						case "2": print(" All calls cost")

						case "3": print("Clear counters")
						
						case "0":
							break
						case _:
							print("Invalid input. Try again.")


			case "7": 
				while True:
					menu ="""
					call cost setting menu:
					1 - call cost limit
					2 - show costs in
					0 - Back

					"""
					print(menu) 
					choice = input("select option")
			
					match choice:
						case "1": print("call cost limit")
                               
						case "2": print("show costs in")
						
						case "0":
							break
						case _:
							print("Invalid input. Try again.")



				
			case "8": print("Prepaid credit selected")
           
			case "0":
				break
			case _:
				print("Invalid input. Try again.")


def tones_menu():
	while True:
		menu = """
		Tones settings Menu:

       1 - Ringing tone
       2 - Ringing volume
       3 - Incoming call alert
       4 - Composer
       5 - Message alert tone
       6 - Keypad tones
       7 - Warning and game tones
       8 - Vibrating alert
       9 - Screen saver
       0 - Back

        """

		print(menu)
		choice = input("Select option: ")

		match choice: 
			case "1": print("Ringing tone selected.")
			case "2": print("Ringing volume selected.")
			case "3": print("Incoming call alert")
			case "4": print("Composer")
			case "5": print("Message alert tone")
			case "6": print("Keypad tones")
			case "7": print("Warning and game tones")
			case "8": print("Vibrating alert")
			case "9": print(" Screen saver")
			case "0":
				break
			case _:
				print("Invalid input. Try again.")

def settings_menu():
	while True:
		menu = """
		Settings Menu:
       1 - Call settings
       2 - Phone settings
       3 - Security settings
       4 - Restore factory settings
       0 - Back
        """
		print(menu)
		choice = input("Select option: ")

		match choice:
			case "1": 
				while True:
					menu ="""
					call settinggs menu:
					  
					1 - Automatic redial
					2 - Speed dialing
					3 - Call waiting options
					4 - Own number sending
					5 - Phone line in use
					6 - Automatic answer
					0 - Back

					"""
					print(menu) 
					choice = input("select option")
			
					match choice:
						case "1": print("Automatic redial")
                               
						case "2": print(" Speed dialing")

						case "3": print("Call waiting options")

						case "4": print("Own number sending")
					
						case "5": print("Phone line in use")
						
						case "6": print("Automatic answer")

						case "0":
							break
						case _:
							print("Invalid input. Try again.")

			
			case "2":
				while True:
					menu ="""
					phone settinggs menu:
					 1 - Language
					 2 - Cell info display
					 3 - Welcome note
					 4 - Network selection
					 5 - Lights
					 6 - Confirm SIM service action
					 0 - Back
 
					"""
					print(menu) 
					choice = input("select option")
			
					match choice:
						case "1": print(" Language")
                               
						case "2": print(" Cell info display")

						case "3": print("Welcome note")

						case "4": print("Network selection")
					
						case "5": print("Lights")
						
						case "6": print("Confirm SIM service action")

						case "0":
							break
						case _:
							print("Invalid input. Try again.")

 

				
			case "3": print("Security settings")
			case "4": print("Restore factory settings")
        
			case "0":
				break
			case _:
				print("Invalid input. Try again.")


def call_divert_menu():
     while True:
       menu = """
       call divert menu

       0 - Back
         """
       print(menu)
       choice = input("Select option: ")

       match choice:
            
            case "0": 
                break
            case _:
                 print("invalid input. ")


def games_menu():
     while True:
       menu = """
       Game menu

       0 - Back
         """
       print(menu)
       choice = input("Select option: ")

       match choice:
            
            case "0": 
                break
            case _:
                 print("invalid input. ")


def calculator_menu():
     while True:
       menu = """
       Calculator menu

       0 - Back
         """
       print(menu)
       choice = input("Select option: ")

       match choice:
            
            case "0": 
                break
            case _:
                 print("invalid input. ")


def reminders_menu():
     while True:
       menu = """
       reminders menu

       0 - Back
         """
       print(menu)
       choice = input("Select option: ")

       match choice:
            
            case "0": 
                break
            case _:
                 print("invalid input. ")



def clock_menu():
     while True:
       	menu = """
        clock  Menu:

       1 - Alarm clock
       2 - Clock settings
       3 - Date setting
       4 - Stopwatch
       5 - Countdown timer
       6 - Auto update of date and time
       0 - Back

        """

        print(menu)
        choice = input("Select option: ")


        print(menu)
        choice = input("Select option: ")
 
        match choice:
            case "1":
                print("Alarm clock selected.")
            case "2":
                print("Clock settings selected.")
            
            case "3":
                print("Date setting")
            case "4":
                print("Stopwatch")
        
            case "5":
                print(" Countdown timer")
            case "6":
                print(" Auto update of date and time")
          
            case "0":
                break
            case _:
                print("Invalid input. Try again.")

def  profiles_menu():
     while True:
       menu = """
      profiles menu

       0 - Back
         """
       print(menu)
       choice = input("Select option: ")

       match choice:
            
            case "0": 
                break
            case _:
                 print("invalid input. ")

def sim_service_menu():
     while True:
       menu = """
      sim service menu

       0 - Back
         """
       print(menu)
       choice = input("Select option: ")

       match choice:
            
            case "0": 
                break
            case _:
                 print("invalid input. ")




main_menu()

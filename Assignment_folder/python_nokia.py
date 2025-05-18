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
            case "8":
                games_menu()
            case "9":
                calculator_menu()
            case "10":
                reminders_menu()
            case "11":
                clock_menu()
            case "12":
                profiles_menu()
             
            case "13":
                sim_service_menu()

            case "00":
                print("Exiting Nokia Menu. Goodbye!")
                break
            case _:
                print("Invalid input. Try again.")

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
            case "1":
                print("Search selected.")
            case "2":
                print("Add name selected.")
            
            case "3":
                print("add name")
            case "4":
                print("erase")
        
            case "5":
                print("edit")
            case "6":
                print("assign tone")
            case "7":
                print("snd b card")
            case "8":
                print("option")
            
            case "9":
                print("speed dials")
            case "10":
                print("voice tags")

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
            case "1":
                print("Write message selected.")
            case "2":
                print("Inbox selected.")
            
            case "3":
                print("outbox")
            case "4":
                print("picture messages")
        
            case "5":
                print("templates")
            case "6":
                print("smileys")
            case "7":
                print("message settings")
            case "8":
                print("info service")
            
            case "9":
                print("voice mailbox number")
            case "10":
                print("service command editor")

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
            case "1":
                print("Write message selected.")
            case "0": 
                break
            case _:
                 print("invalid input. ")

main_menu()

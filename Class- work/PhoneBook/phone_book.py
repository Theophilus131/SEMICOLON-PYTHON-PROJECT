from PhoneBook import contacts


class PhoneBook:
    Contacts = []

    @property
    def addContact(self,first_name,last_name,phone_number)-> None:
       pass

    @property
    def removeContact(self,first_name,last_name)-> None:
        pass

    @property
    def find_contact_by_first_name(self,first_name)-> Contacts:
        if first_name is in contacts.Contacts:
            return first_name
        return None

    @property
    def find_contact_by_last_name(self,last_name)-> Contacts:
        if last_name is in contacts.Contacts:
            return last_name
        return None

    @property
    def find_contact_by_phone_number(self,phone_number)-> Contacts:
        if phone_number is in contacts.Contacts:
            return phone_number
        return None


    @property
    def edit_contact(self, first_name, last_name)-> None:
        pass



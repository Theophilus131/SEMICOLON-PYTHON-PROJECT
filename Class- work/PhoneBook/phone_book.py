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
        for contact in self.Contacts:
            if first_name == contact.first_name:
                return first_name
            else:
                raise Exception



    @property
    def find_contact_by_last_name(self,last_name)-> Contacts:
        for contact in self.Contacts:
            if last_name == contact.last_name:
                return contact
            else:
                raise Exception

    @property
    def find_contact_by_phone_number(self,phone_number)-> Contacts:
        for contact in self.Contacts:
            if phone_number == contact.phone_number:
                return contact
            else:
                raise Exception


    @property
    def edit_contact(self, first_name, last_name)-> None:
        for contact in self.Contacts:
            if first_name == contact.first_name and last_name == contact.last_name:
                contact.first_name = first_name
                contact.last_name = last_name





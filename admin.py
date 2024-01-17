import logging
from user import User

class Admin(User):
    def __init__(self, first_name):
        super().__init__(first_name)
        
    @staticmethod
    def add_contact_to_phone_book(contact, phone_book):
        phone_book.add_contact(contact)
        logging.info(f"Админ добавил контакт {contact.user.firstname} в телефонную книгу {phone_book.tag}")

    @staticmethod
    def remove_contact_from_phone_book(contact, phone_book):
        phone_book.delete_contact(contact)
        logging.info(f"Админ удалил контакт {contact.user.firstname} из телефонной книги {phone_book.tag}")

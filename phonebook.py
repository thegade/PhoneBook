import logging


class PhoneBook:
    def __init__(self, tag):
        self.tag = tag
        self.contacts = []
        self.logger = logging.getLogger(f"PhoneBook_{tag}")

    def add_contact(self, contact):
        if contact not in self.contacts:
            self.contacts.append(contact)
            self.logger.info(f"Контакт {contact.user.firstname} добавлен в телефонную книгу {self.tag}")
        else:
            self.logger.warning("Данный контакт уже существует")

    def delete_contact(self, contact):
        if contact in self.contacts:
            self.contacts.remove(contact)
            self.logger.info(f"Контакт {contact.user.firstname} удален из телефонной книги {self.tag}")
        else:
            self.logger.warning("Данный контакт не существует")

    def filter_user(self, user):
        filtered_contacts_user = [contact for contact in self.contacts if contact.user == user]
        for contact in filtered_contacts_user:
            self.logger.info(f"Контакт {contact.user.firstname} принадлежит книжке {contact.user.firstname}")
        return filtered_contacts_user

    def filter_country_code(self, country_code):
        filtered_contacts_code = [contact for contact in self.contacts if contact.country_code == country_code]
        for contact in filtered_contacts_code:
            self.logger.info(f"Контакт {contact.user.firstname} имеет код страны {contact.country_code}")
        return filtered_contacts_code





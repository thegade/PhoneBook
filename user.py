import logging
from phonebook import PhoneBook


class User:

    def __init__(self, firstname):
        self.firstname = firstname
        self.friends = []
        self.phone_books = {}
        self.logger = logging.getLogger(f"User_{firstname}")

    def add_contact(self, contact, tag):
        if tag not in self.phone_books:
            self.logger.error(f"Данный тег {tag} не найден")
            return
        self.phone_books[tag].add_contact(contact)

    def delete_friends(self, user):
        if user in self.friends:
            self.friends.remove(user)
            self.logger.info(f"Пользователь {user.firstname} удален из друзей")
        else:
            self.logger.warning(f"Пользователь {user.firstname} не является вашим другом")

    def add_friends(self, user):
        if user not in self.friends:
            self.friends.append(user)
            self.logger.info(f"Пользователь {user.firstname} добавлен в друзья")
        else:
            self.logger.warning("Вы уже дружите")

    def add_phone_book(self, tag):
        if tag not in self.phone_books:
            self.phone_books[tag] = PhoneBook(tag)
        else:
            self.logger.warning(f"Телефонная книга с тегом {tag} уже существует")

    def share_phone_books(self, user, tag):
        if user not in self.friends:
            self.logger.warning(f"{user.firstname} не является вашим другом")
            return
        if tag not in self.phone_books:
            self.logger.error(f"Телефонная книга с тегом {tag} не существует")
            return
        user.phone_books[tag] = self.phone_books[tag]
        self.logger.info(f"{self.firstname} поделился телефонной книгой с {user.firstname}, тег: {tag}")
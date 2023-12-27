import logging
from user import User
from admin import Admin
from contact import Contact
logging.basicConfig(level=logging.DEBUG)


# Create users
user1 = User("Adel")
user2 = User("Ilmir")
user3 = User("Guts")
admin = Admin()

# Add friends to user1
user1.add_friends(user2)

# Create phonebooks
user1.add_phone_book('family')
user2.add_phone_book('work')

# Add contact information to user
contact1 = Contact(user1, '7', '8005553535')
contact2 = Contact(user2, '8', '9116664646')

# Admins moves
Admin.add_contact_to_phone_book(contact2, user1.phone_books['family'])
Admin.remove_contact_from_phone_book(contact2, user1.phone_books['family'])

# Add users to contact with tags
user1.add_contact(contact1, 'family')
user2.add_contact(contact2, 'work')

# Sharing phonebook with other users
user1.share_phone_books(user2, 'family')
user1.share_phone_books(user3, 'family')

# Filter contacts by users
filtered_contacts_user = user1.phone_books['family'].filter_user(user='user1')

# Filter contacts by country_code
filtered_contacts_code = user1.phone_books['family'].filter_country_code(country_code='7')

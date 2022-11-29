# User account
class User:
    uName = 'No Name Provided'
    password = 'test!369'
    account_number = 0

# Character associated with User
class Character(User):
    char_name = 'default'
    level = 1
    region = 'NA'

# Inventory associated with User Character
class Inventory(Character):
    gold = 0
    food = 2

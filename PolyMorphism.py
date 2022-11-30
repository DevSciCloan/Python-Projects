import random # Importing module to generate random numbers

class User:
    r = False
    w = False
    name = 'Robert'
    password = 'jr1992'
    # Method to log in using hard coded name and password
    def login(self):
        uName = input('Enter Username: ')
        pWord = input('Enter Password: ')
        # Checking if entered uName and pWord match
        if (uName == self.name and pWord == self.password):
            self.r = True
            print("You now have permission to view this data {}. Your permissions are read: {}, write: {}".format(uName,self.r,self.w))
        else:
            print("The email or password you entered is incorrect.")

class Admin(User):
    name = 'Admin'
    password = 'Master'

    def login(self):
        uName = input('Enter Username: ')
        pWord = input('Enter Password: ')
        if (uName == self.name and pWord == self.password):
            # Giving Admin privilege
            self.r = True
            self.w = True
            print("Welcome back {} your permissions are read: {}, write: {}".format(uName,self.r,self.w))
        else:
            print("The email or password you entered is incorrect.")

class Guest(User):
    randNum = random.random()
    name = 'Guest'
    idNumber = random.randint(1,10)

    def login(self):
        # Removing privilege
        self.r = False
        self.w = False
        self.name = input("Enter your name: ")
        print("Welcome {}. Your guest ID is {} and your permissions are read: {} write: {}".format(self.name,self.idNumber,self.r,self.w))

if __name__ == "__main__":
    # Getting user input whether or not they want to login as Admin
    isAdmin = True if input("Login as admin? (Y/N)").upper() == 'Y' else False
    if isAdmin == True:
        admin = Admin()
        admin.login()
    else:
        # Getting user input whether or not they want to login as a Guest
        isGuest = True if input("Login as guest? (Y/N)").upper() == 'Y' else False
        if isGuest == True:
            guest = Guest()
            guest.login()
        # If not an Admin or a Guest login as regular User
        else:
            user = User()
            user.login()
    

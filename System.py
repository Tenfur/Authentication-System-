from User import User
from File import File

class System:
    def __init__(self):
        self.__users = []
        self.__file = File()
    def verificatePasswords(self, password, passwordCheck):
        if password == passwordCheck:
            return True
        else:
            return False
    def createUser(self):
        email = input("Email: ")
        password = input("Password: ")
        passwordCheck = input("Password again: ")
        if self.verificatePasswords(password, passwordCheck):
            user = User(email, password, passwordCheck)
            self.__file.saveUserInfoInFile(user)  # Save the user's info in a file
            print("User created correctly!")
        else:
            print("The passwords are not equal")
    def loginUser(self):
        email = input("Email: ")
        password = input("Password: ")
        # First we check if the email exists
        validate, index = self.__file.verificateEmail(email)
        if validate:
            # Check the password
            if self.__file.verificatePassword(email, password):
                print("Welcome to the system")
            else:
                print("Verificate your password")
        else:
            print("That email doesn't exist in the system")
    def showUsersInfo(self):
        size = len(self.__users)
        if size == 0:
            print("There are not users in the system")
        else:
            print("\t Users in the system")
            for i in self.__users:
                i.showInfo()
    def problemsUser(self):
        try:
            print("1) Change email")
            print("2) Change password")
            print("3) Delete account")
            option = int(input("Option: "))
            if option == 1:
                self.__file.changeEmailUser()
            elif option == 2:
                self.__file.changePasswordUser()
            elif option == 3:
                self.__file.deleteUser()
        except:
            print("Please, enter a validate option")
    def recoverDataUsers(self):
        self.__file.recoverUsersInfoFile()
        self.__users = self.getUsersFile()
    def getUsersFile(self):
        return self.__file.getUsers()
    

from User import User

class File:
    def __init__(self):
        self.__users = []

    def saveUserInfoInFile(self, user):
        file = open("users.txt", "a")
        file.write(user.getEmail() + "," + user.getPassword() + ','+ user.getPasswordCheck() + "\n")
        file.close()
    def recoverUsersInfoFile(self):
        file = open("users.txt", "r")
        data = file.read().split("\n")
        file.close()
        elements = []
        # Get the information
        for i in data:
            elements.append(i.split(","))
        # Delete last position
        elements.pop()

        # Check if there are repeat values
        size = len(self.__users)
        if size > 0:
            self.__users.clear()

        # Save the info in objects
        for i in elements:
            user = User(i[0], i[1], i[2])
            self.__users.append(user)
    def verificateEmail(self, email):
        authEmail = False
        index = 0
        for i in self.__users:
            if i.getEmail() == email:
                authEmail = True
                break
            index += 1
        return authEmail, index
    def verificatePassword(self, email, password):
        auth = False
        for i in self.__users:
            if i.getEmail() == email and i.getPassword() == password:
                auth = True
                break
        return auth
    def changeEmailUser(self):
        email = input("Enter your email to check in the system: ")
        validate, index = self.verificateEmail(email)
        if validate:
            newEmail = input("Enter your new email: ")
            self.__users[index].setEmail(newEmail)
            self.saveAllUserInfo()
            print("Email changed correctly!")
        else:
            print("That email doesn't exist in the system")
    def changePasswordUser(self):
        email = input("Enter your email to check in the system: ")
        validate, index = self.verificateEmail(email)
        if validate:
            newPassword = input("Enter your new password: ")
            self.__users[index].setPassword(newPassword)
            self.__users[index].setPasswordCheck(newPassword)
            self.saveAllUserInfo()
            print("Password changed correctly!")
        else:
            print("That email doesn't exist in the system")
    def saveAllUserInfo(self):
        # First we need to delete the previous data
        open("users.txt", "w").close()
        # Now save the new data with the changes
        file = open("users.txt", "a")
        for i in self.__users:
            file.write(i.getEmail() + "," + i.getPassword() + "," + i.getPasswordCheck() + "\n")
        file.close()
    def deleteUser(self):
        email = input("Enter your email to check in the system: ")
        validate, index = self.verificateEmail(email)
        if validate:
            password = input("Verificate password before to delete: ")
            if self.verificatePassword(email, password):
                condition = input("Are you that you want to delete your account? (yes or no): ")
                if condition.lower() == "yes":
                    del self.__users[index]
                    self.saveAllUserInfo()
                    print("User deleted correctly!")
                else:
                    print("See you later!")
            else:
                print("Verificate your password")
        else:
            print("The email doesn't exist in the system")
    def getUsers(self):
        return self.__users
class User:
    def __init__(self, email, password, passwordCheck):
        self.__email = email
        self.__password = password
        self.__passwordCheck = passwordCheck
    def setEmail(self, email):
        self.__email = email
    def setPassword(self, password):
        self.__password = password
    def setPasswordCheck(self, passwordCheck):
        self.__passwordCheck = passwordCheck
    def getEmail(self):
        return self.__email
    def getPassword(self):
        return self.__password
    def getPasswordCheck(self):
        return self.__passwordCheck
    def showInfo(self):
        print("Email:", self.__email)
        print("Password:", self.__password)
        print("Password check:", self.__passwordCheck)
        print("\n")
from System import System

def run():
    system = System()
    while True:
        try:
            system.recoverDataUsers()
            print("\t Authentication System")
            print("1) Register")
            print("2) Login")
            print("3) Problems with your account")
            print("4) Show users")
            print("5) Exit")
            option = int(input("Enter an option: "))
            if option == 1:
                system.createUser()
            elif option == 2:
                system.loginUser()
            elif option == 3:
                system.problemsUser()
            elif option == 4:
                system.showUsersInfo()
            elif option == 5:
                break
        except:
            print("Please, enter a validate option")
if __name__ == "__main__":
    run()
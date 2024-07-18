from os import system

class Database:
    def __init__(self) -> None:
        self.data = {}
    
    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
     User's class with attributes: login, password
    """
    def __init__(self, username, password, password_confirm) -> None:
        self.username = username
        self.password = None
        upregister = digexist = False
        if len(password) > 7:
            for i in range(len(password)):
                st = str(password[i])
                # print(st, type(st))
                if st.upper() in password:
                    upregister = True
                if ord(st) in range(ord('0'), ord('9')):
                    digexist = True

            if password != password_confirm:
                input("Error: password not confirmed. press <Enter>")
            elif not upregister:
                input("Error: password does not consist upregister symbols. press <Enter>")
            elif not digexist:
                input("Error: password does not consist digits. press <Enter>")
            else:
                self.password = password
        else:
            input("Error: password length less then 8 symbols. press <Enter>")            
        

if __name__ == '__main__':
    database = Database()
    login=""
    while True:
        system('cls')
        print(database.data)
        choise = int(input(f"Welcome {login}: Input move:\n1 - Enter\n2 - Registration\n3 - exit\n"))
        if choise == 1:
            login = input("Input login: ")
            password = input("Input password: ")
            if login in database.data:
                if password == database.data[login]:
                    input(f"Hellow {login}")
                else:
                    input("Wrong password")
            else:
                input("There is no such user")

        if choise == 2:
            user = User(input("Input login: "), pass1:=input("Input password: "), pass2:=input("Confirm password: "))
            if pass1 == pass2 and user.password != None:
                database.add_user(user.username, user.password)
            
        if choise == 3:
            exit(0)
   
    
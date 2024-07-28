from os import system
class User:
    '''
    > Class of UrTube's user <
    '''

    def __init__(self, nickname, password, age) -> None:
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
    
    def __str__(self) -> str:
        return f"User: {self.nickname}, psw: {self.password}, age: {self.age}\n"
    
    def name(self):
        return self.nickname
    
    def old(self):
        return self.age




if __name__ == '__main__':
    system('cls')
    print("start user module...")
    print(User.__doc__)
    user = User('Bot', 'user1', 23)
    print(user)
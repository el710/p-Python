users = []

class User():
    id: int
    username: str
    age: int
    def __init__(self, userlist):
        self.id = self.new_max(userlist)
        print(self.id)
        self.username = "f"
        userlist.append(self)
    
    def new_max(self, userlist):
        ids = [x.id for x in userlist]
        if len(ids) > 0:
            _max = max(ids)
        else:
            _max = 0
        
        if _max >=  len(userlist):
            for x in range(len(userlist)):
                if x not in ids:
                    return x
        return len(userlist)


u1 = User(users)
u1 = User(users)
u1 = User(users)


x = 0

y = lambda x: if x: len(users) else: 1

print(y)


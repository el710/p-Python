### 
# OOP: inheritance - class Human -> class Men(Human)
#      incapsulation - 
#      polimorphizm -  
# ###


class Human:
    Head = True ## attribute of class
    _legs = True ## this var not available in other modules(files) because of '_'
    __arms = True ## this var is uniq for this class and its decsendants because of '__'
                  ## __arms in descendant class will be different: Parent_class.__arms !=  Child_class.__arms

    ##def __new__(cls) -> Self: ## start first

    def __init__(self, name, age) -> None:  # here is initialization
        self.name = name  ## attribute of object
        self.age = age
        self.about()
        if type(self) != Human and type(self) != Teacher:
            self.tellabout() # method of child Student
    
    def __del__(self) -> None: # distructor
        print(f"{self.name} is left the world")
        
    def about(self):
        print(f" My name {self.name} I am {self.age}")
    
    def len(self):
        print(f"{self.name} is {self.age} years old")

    def birthday(self):
        self.age += 1
        print(f"{self.name} has birthday for {self.age}")

    ## overload operator '<' (lower then)
    def __lt__(self, other) -> None:
        return self.age < other.age
    
    ## overload (greater then) '>'
    def __gt__(self, other):
        return self.age > other.age
    
    ## overload '=='
    def __eq__(self, value: object) -> bool:
        return self.name == value.name and self.age == value.age
    
    ## magic methods
    def __bool__(self) -> bool:
        return bool(self.age)
    
    def __str__(self) -> str:
        return self.name
    
    def status(self):
        print(f"head - {self.Head}")
        print(f"legs - {self._legs}")
        print(f"arms - {self.__arms}")
    
## inheritance
class Student(Human):

    def tellabout(self):
        print("I am student")

class Teacher(Human):
    __arms = 'other arms' ## this is _Human__arms - Teacher doesn't have itsown __arms
    pass

human = Human('Homo', 45)
human.status()

student = Student("Lex", 23) ## it uses __init of Human
teacher = Teacher('Nick', 56)

#check out for __arms
print(dir(human), '\n')
print(dir(teacher))
## print(teacher.__arms) - make error
print(teacher._Human__arms)
teacher.status()
input('press <Enter> to continue...')


ben = Human("Bender", 17)
max = Human("Max", 24)

print(f"{ben} < {max}:", ben < max)
print(f"{ben} > {max}:", ben > max)
print(f"{ben} == {max}:", ben == max)

if ben:
    ben.about()

print(ben, ben.age)
print(max, max.age)

## online adding attributes
ben.surname = "Rodriges"
print(f"{ben.name}", ben.surname)

max.birthday()
max.len()

print(ben.__dict__, ben.Head) ## here we use class's attribute because object 'Ben' has not attribute 'Head' but class has
ben.Head = False ## now Ben has his own attribute 'Head'
print(ben.__dict__, ben.Head)


del ben
del max

###########################
# about class 'object' and __new__
print(int.__mro__) # inheritance chain
print(Human.__mro__) # inheritance chain
## class 'object' is base for all

class User:
    __instance = None
    var_a = None

    def __new__(cls, *args, **kwargs):
        ## here cls - is link to class User
        ## we can use class's attribute for make uniq object of class User
        if cls.__instance is None:
            cls.__instance = super().__new__(cls) ## we called method new() of class Object
        return cls.__instance  ## return link to our object
    
    def __init__(self, *args, **kwargs) -> None: ## args and kwargs are put here from __new__(*args, **kwargs)
        print(f"{id(self)}: Init work...")
        self.args = args

        for key, value in kwargs.items(): ## the same as
            setattr(self, key, value)     ## self.name = kwargs.get('name')
                                          ## self.age = kwargs.get('age') e.t.c ...

    def print_that(self, leb):
        User.var_a = leb
        print(User.__instance)

    def print_it(self):
        User.print_that(self, 'pro')
        print("Object method\n")
        

at_list = (1, 2, 3)
at_dict = {'name': 'Bender', 'age': 35, 'gender': 'male'}

user1 = User(*at_list, **at_dict)
# user2 = User() ## because of __instance it will be the same object user1
# print(user1 is user2)

user1.print_it()
user1.print_that('dfg')

print(user1.__dict__)

input("press <Enter>")

        
####################################
# About multiinheritance
class Arm():
    def __init__(self) -> None:
        self.arms = 2
        super().__init__() # this adds chain from Animal to Leg

    def get_arms(self):
        return self.arms
    

class Leg():
    def __init__(self) -> None:
        self.legs = 2

    def get_legs(self):
        return self.legs


class Animal(Arm, Leg):
    def make(self, arms, legs) -> None:
        self.arms = arms
        self.legs = legs
    
    def status(self):
        return f"{self.arms} - arms, {self.legs} - legs"
        


animal = Animal()
print(Animal.__mro__, "\n")

print(animal.status())

animal.make(3, 5)
print(animal.status())






'''

from ..Tasks import module_5_1, module_5_2, module_5_3, module_5_4, module_6_1, module_6_2, module_6_3

'''




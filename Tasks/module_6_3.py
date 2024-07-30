class Horse():
    def __init__(self) -> None:
        self.x_distance = 0
        self.sound = 'Frrr'
        super().__init__()

    def run(self, dx):
        self.x_distance += dx
       

class Eagle():
    def __init__(self) -> None:
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'
    
    def fly(self, dy):
        self.y_distance += dy
       
    
class Pegasus(Horse, Eagle):
    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)
    
    def get_pos(self):
        return self.x_distance, self.y_distance
    
    def voice(self):
        return self.sound


if __name__ == '__main__':
    from os import system
    system('cls')

    pegas = Pegasus()
    # print(Pegasus.mro(), "\n")
    # print(dir(Pegasus), "\n")

    print(pegas.get_pos())
    pegas.move(45, 45)
    print(pegas.get_pos())
    pegas.move(-5, 20)
    print(pegas.get_pos())

    print(pegas.voice())

from student import *

class Group:
    peoples: [Student] = []
    lives: int = 0
    def __init__(self) -> None:
        for i in range(0, 10000):
            self.peoples.append(J())
        self.lives = len(self.peoples)
        return
    def goOn(self) -> None:
        for i in range(len(self.peoples)):
            if not self.peoples[i].isDied:
                self.peoples[i].grow()
                if self.peoples[i].isDied:
                    self.lives -= 1
                    print(self.peoples[i].name, "is died!")
                else:
                    print(self.peoples[i].name, "is", self.peoples[i].age, "years old now!")
        return
    def checkBumped(self) -> None:
        for i in range(len(self.peoples)):
            if not self.peoples[i].isDied:
                from random import randint
                if randint(1, 50) == 1:
                    print("A car bumped int", self.peoples[i].name + '!')
                    self.peoples[i].getBumped()
                    if self.peoples[i].isDied:
                        self.lives -= 1
                        print(self.peoples[i].name, "is died because of that car!")
                    else:
                        print("Conguaduations!", self.peoples[i].name, "is still alive!");
        return
    def checkEvent(self) -> None:
        self.checkBumped()
        return
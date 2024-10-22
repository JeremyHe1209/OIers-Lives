from group import *

class Game:
    time: int = 0
    peoples: Group = Group()
    def __init__(self) -> None:
        self.time: int = 0
        self.peoples: Group = Group()
        return
    def run(self) -> None:
        import time as t
        while self.peoples.lives:
            self.time += 1
            print("Year", self.time)
            self.peoples.goOn()
            self.peoples.checkEvent()
            t.sleep(0.5)
        return
class Student:
    age: int = 0
    name: str = ""
    health: int = 100
    deathProbility: float = 5
    diff: {int: float} = {0: -0.5, 10: 0, 60: 0.5}
    isDied: bool = False
    defense: int = 10
    def __init__(self, age: int = 0) -> None:
        self.age = age
        return
    def getDif(self) -> float:
        for i in range(self.age):
            if self.age - i in self.diff:
                return self.diff[self.age - i]
        return self.diff[0]
    def grow(self) -> None:
        self.age += 1
        self.deathProbility += self.getDif()
        from random import randint
        self.isDied = randint(1, self.health * 10) <= self.deathProbility * 10
        return
    def getBumped(self) -> None:
        from random import randint
        r: int = randint(1, 100)
        if r > self.defense:
            self.isDied = 1
        elif r < 10:
            self.health *= 0.6
            print("The health of", self.name, "has been attacked!")
        return

class W(Student):
    health: int = 80
    name: str = "yyy"
    defense: int = 60

class J(Student):
    name: str = "zzz"
    diff: {int: float} = {0: -0.5, 10: 0, 60: 0.3}
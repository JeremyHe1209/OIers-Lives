from random import random
from deathProb import *

class Figure:
    age: int = 0
    name: str = ""
    health: int = 100
    reason: str = ""
    healthDelta: int = 5
    deathProb: DeathProb = DeathProb()
    luck: float = 1
    strength: float = 1
    def __init__(self, name: str):
        self.age = 0
        self.name = name
    def getStatus(self) -> str:
        if self.health > 80:
            return "healthy"
        elif self.health > 50:
            return "unhealthy"
        else:
            return "weak"
    def getAge(self) -> str:
        if self.age < 10:
            return "child"
        elif self.age < 20:
            return "teenager"
        elif self.age < 30:
            return "young adult"
        elif self.age < 40:
            return "adult"
        elif self.age < 50:
            return "middle-aged"
        elif self.age < 60:
            return "elderly"
        else:
            return "old"
    def die(self, reason: str) -> None:
        self.health = 0
        self.reason = reason
        print("[{name}] : died at the age of {age} {reason}".format(name = self.name, age = self.age, reason = reason))
    def show(self) -> None:
        print("[{name}] : {status1}, {status2}".format(name = self.name, age = self.age, status1 = self.getStatus(), status2 = self.getAge()))
    def grow(self) -> None:
        if self.health <= 0:
            return
        self.age += 1
        print("[{name}] : {age}-year-old now!!!".format(name = self.name, age = self.age))
    def passAMonth(self) -> None:
        if self.health <= 0:
            return
        self.health = min(self.health + self.strength * self.healthDelta, 100)
        self.show()
        if(random() < self.deathProb.getProb(self.age, self.health) * (2 - self.strength) * (2 - self.luck)):
            self.die("due to natural causes")

from figure import *

class Event:
    name: str
    description: str
    prob: float
    def __init__(self, name: str, description: str, prob: float) -> None:
        self.name = name
        self.description = description
        self.prob = prob

class HealthEffectedEvent(Event):
    healthDelta: int
    dueToDeath: bool
    def __init__(self, name: str, description: str, prob: float, healthDelta: int, dueToDeath: bool = False, reason: str = "") -> None:
        super().__init__(name, description, prob)
        self.healthDelta = healthDelta
        self.dueToDeath = dueToDeath
        if dueToDeath:
            self.reason = reason

class GlobalEvent(Event):
    year: int
    month: int
    def __init__(self, name: str, description: str, prob: float, year: int, month: int) -> None:
        super().__init__(name, description, prob)
        self.year = year
        self.month = month

class AwardEvent(Event):
    def __init__(self, name: str, description: str, prob: float) -> None:
        super().__init__(name, description, prob)

def HealthEffectedEventHappen(figure: Figure, event: HealthEffectedEvent) -> None:
    if random() < min(event.prob * (2 - figure.luck), 1):
        if event.name == "AIDS":
            if figure.healthDelta != 0:
                figure.healthDelta = 0
            else:
                return
        print("[{name}] : {description}".format(name = figure.name, description = event.description))
        if event.dueToDeath:
            figure.die(event.reason)
        else:
            figure.health += event.healthDelta * (2 - figure.strength)
            if(figure.health > 100):
                figure.health = 100
            if figure.health <= 0:
                figure.die("because he/she was too weak")

def GlobalEventHappen(event: GlobalEvent) -> None:
    if random() < event.prob:
        print("[All] : {description}".format(description = event.description))

def AwardEventHappen(event: AwardEvent) -> None:
    pass

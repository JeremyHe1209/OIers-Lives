class DeathProb:
    child: int = 0
    teen: int = 14
    midage: int = 25
    elderly: int = 55
    childProb: float = 0.00015
    teenProb: float = 0.00005
    midageProb: float = 0.0001
    elderlyProb: float = 0.00025
    childDelta: float
    teenDelta: float
    midageDelta: float
    elderlyDelta: float = 0.0004
    def __init__(self) -> None:
        self.childDelta = (self.teenProb - self.childProb) / (self.teen - self.child)
        self.teenDelta = (self.midageProb - self.teenProb) / (self.midage - self.teen)
        self.midageDelta = (self.elderlyProb - self.midageProb) / (self.elderly - self.midage)
    def update(self) -> None:
        self.childDelta = (self.teenProb - self.childProb) / (self.teen - self.child)
        self.teenDelta = (self.midageProb - self.teenProb) / (self.midage - self.teen)
        self.midageDelta = (self.elderlyProb - self.midageProb) / (self.elderly - self.midage)
    def getProb(self, age: int, health: int) -> float:
        if age < self.teen:
            return self.childProb + self.childDelta * (age - self.child) + (100 - health) * 0.0001
        elif age < self.midage:
            return self.teenProb + self.teenDelta * (age - self.teen) + (100 - health) * 0.0001
        elif age < self.elderly:
            return self.midageProb + self.midageDelta * (age - self.midage) + (100 - health) * 0.0001
        else:
            return self.elderlyProb + self.elderlyDelta * (age - self.elderly) + (100 - health) * 0.0001

from event import *
from figure import *
from random import randint
from os import system

class Game:
    figures: [Figure] = []
    healthEffectedEvents: [HealthEffectedEvent] = []
    globalEvents: [GlobalEvent] = []
    awardEvents: [AwardEvent] = []
    figuresCount: int = 0
    healthEffectedEventsCount: int = 0
    globalEventsCount: int = 0
    awardEventsCount: int = 0
    fast: bool = False
    stop: bool = False
    def __init__(self) -> None:
        pass
    def addFigure(self, figure: Figure) -> None:
        self.figures.append(figure)
        self.figuresCount += 1
    def addEvent(self, event: Event) -> None:
        if isinstance(event, GlobalEvent):
            self.globalEvents.append(event)
            self.globalEventsCount += 1
        elif isinstance(event, AwardEvent):
            self.awardEvents.append(event)
            self.awardEventsCount += 1
        elif isinstance(event, HealthEffectedEvent):
            self.healthEffectedEvents.append(event)
            self.healthEffectedEventsCount += 1
        else:
            raise Exception("Unknown event type")
    def passAMonth(self) -> None:
        for figure in self.figures:
            if figure.health <= 0:
                continue
            figure.passAMonth()
            if figure.health <= 0:
                self.figuresCount -= 1
                continue
            if self.healthEffectedEventsCount > 0:
                ind: int = randint(0, self.healthEffectedEventsCount - 1)
                HealthEffectedEventHappen(figure, self.healthEffectedEvents[ind])
            if figure.health <= 0:
                self.figuresCount -= 1
                continue;
    def passAYear(self, year) -> None:
        if year < 2019:
            self.addEvent(GlobalEvent("NOIP-J/S{year} The First Test".format(year = year), "NOIP-J/S{year} The First Test is coming!".format(year = year), 1, year, 9))
            self.addEvent(GlobalEvent("NOIP-J/S{year} The Second Test".format(year = year), "NOIP-J/S{year} The Second Test is coming!".format(year = year), 1, year, 10))
        else:
            self.addEvent(GlobalEvent("CSP-J/S{year} The First Test".format(year = year), "CSP-J/S{year} The First Test is coming!".format(year = year), 1, year, 9))
            self.addEvent(GlobalEvent("CSP-J/S{year} The Second Test".format(year = year), "CSP-J/S{year} The Second Test is coming!".format(year = year), 1, year, 10))
            self.addEvent(GlobalEvent("NOIP{year}".format(year = year), "NOIP{year} is coming!".format(year = year), 1, year, 11))
        self.addEvent(GlobalEvent("The Provinces' OI{year}".format(year = year), "The Provinces' OI{year} is coming!".format(year = year), 1, year, 3))
        self.addEvent(GlobalEvent("NOI{year}".format(year = year), "NOI{year} is coming!".format(year = year), 1, year, 7))
        self.addEvent(GlobalEvent("WC{year}".format(year = year), "WC{year} is coming!".format(year = year), 1, year, 1))
        self.addEvent(GlobalEvent("APIO{year}".format(year = year), "APIO{year} is coming!".format(year = year), 1, year, 5))
        self.addEvent(GlobalEvent("CTSC{year}".format(year = year), "CTSC{year} is coming!".format(year = year), 1, year, 5))
        self.addEvent(GlobalEvent("IOI{year}".format(year = year), "IOI{year} is coming!".format(year = year), 1, year, 0))
        month: int = 0
        print("Year {year}".format(year = year))
        if self.figuresCount <= 0:
            return
        for figure in self.figures:
            if figure.health > 0:
                figure.grow()
        if not self.fast:
            tmp: str = input()
            if tmp == "fast":
                self.fast = True
            elif tmp == "exit":
                self.stop = True
                return
            system("cls")
        for i in range(1):
            if self.figuresCount <= 0:
                return
            month += 1
            print("Year {year}, Month {month}".format(year = year, month = month))
            for globalEvent in self.globalEvents:
                if globalEvent.year == year and globalEvent.month == month:
                    GlobalEventHappen(globalEvent)
            self.passAMonth()
            if not self.fast:
                tmp: str = input()
                if tmp == "fast":
                    self.fast = True
                elif tmp == "exit":
                    self.stop = True
                    return
                system("cls")
    def run(self) -> None:
        system("cls")
        year: int = 2010
        while self.figuresCount > 0:
            year += 1
            self.passAYear(year)
            if self.stop:
                return
        print("Summary")
        for figure in self.figures:
            print("[{name}] died at the age of {age} {reason}".format(name = figure.name, age = figure.age, reason = figure.reason))

game = Game()
# j : 英年早逝
j: Figure = Figure("j")
j.deathProb.childProb = j.deathProb.teenProb = j.deathProb.midageProb = 0.0004
j.deathProb.elderlyProb = 0.005
j.deathProb.elderlyDelta = 0.003
j.deathProb.update()
j.deathProb.midageDelta = 0
game.addFigure(j)
# w : 无敌之身但厄运附体
w: Figure = Figure("w")
w.strength = 1.8
w.luck = 0.1
game.addFigure(w)
# r : 运气爆棚但身体薄弱
r: Figure = Figure("r")
r.strength = 0.3
r.luck = 1.8
r.deathProb.childProb = r.deathProb.teenProb = r.deathProb.midageProb = 0.0003
r.deathProb.elderlyProb = 0.0005
r.deathProb.elderlyDelta = 0.0005
game.addFigure(r)
# f : fw
f: Figure = Figure("f")
f.strength = 0.5
f.luck = 0.5
game.addFigure(f)
# h : god
h: Figure = Figure("h")
h.strength = 1.5
h.luck = 1.5
game.addFigure(h)
game.addEvent(HealthEffectedEvent("cold", "he/she got cold", 0.5, -10))
game.addEvent(HealthEffectedEvent("flu", "he/she got flu", 0.3, -20))
game.addEvent(HealthEffectedEvent("AIDS", "he/she got AIDS", 0.0005, 0))
game.addEvent(HealthEffectedEvent("depressed", "he/she was depressed and then killed himself/herself", 0.005, 0, True, "because he/she was depressed and then killed himself/herself"))
game.addEvent(HealthEffectedEvent("car accident", "a car accident happened to him/her", 0.01, 0, True, "because of the car accident"))
game.addEvent(HealthEffectedEvent("killer", "a man kill him/her", 0.007, 0, True, "because a man kill him/her"))
game.addEvent(HealthEffectedEvent("killer", "a woman kill him/her", 0.003, 0, True, "because a woman kill him/her"))
game.addEvent(HealthEffectedEvent("fall down", "he/she felt down from the 30th floor", 0.008, 0, True, "because he/she felt down from the 30th floor"))
game.addEvent(HealthEffectedEvent("idiot", "he/she became an idiot and killed himself/herself", 0.002, 0, True, "because he/she became an idiot and killed himself/herself"))
game.addEvent(HealthEffectedEvent("pool", "he/she felt into a pool but he/she couldn't swim", 0.005, 0, True, "because he/she felt into a pool but he/she couldn't swim"))
game.addEvent(HealthEffectedEvent("cancer", "he/she got cancer", 0.0005, 0, True, "because he/she got cancer"))
game.run()

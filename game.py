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

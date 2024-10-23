from game import *

if __name__ == '__main__':
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

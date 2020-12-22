# Ref https://realpython.com/python3-object-oriented-programming/#classes-vs-instances
class Player:
  walkSpeed = 10

  def __init__(self, name: str, heath: int):
    self.heath = heath
    self.name = name

    print("Player init")

  def attack(self):
    print("Attack!")  

  def walk(self):
    print("I'm walking speed = " + str(self.walkSpeed))

  def __str__(self):
    #return super.__str__(self)
    return "Player(name={} heath={} walkSpeed={})".format(self.name, self.heath, self.walkSpeed)

class WarriorPlayer(Player):
  def __init__(self, name: str, heath: int):
    Player.__init__(self, name, heath)
    print("WarriorPlayer init")

class WizardPlayer(Player):
  def __init__(self, name: str, heath: int, manaMax: int):
    Player.__init__(self, name, heath)
    self.manaMax = manaMax
    print("WizardPlayer init")

  def attack(self):
    if(self.manaMax >= 5):
      print("Attack with mana!")  
      self.manaMax -= 5
    else:
      print("Out of mana! Can't attack!")  

class FlyingCreature():
  def __init__(self, flySpeed: int):
    self.flySpeed = flySpeed
    print("FlyingCreature init")

  def __str__(self):
    #return super.__str__(self)
    return "FlyingCreature(flySpeed={})".format(self.flySpeed)


class FlyingPlayer(Player, FlyingCreature):
  def __init__(self, name, age, flySpeed):
    Player.__init__(self, name, age)
    FlyingCreature.__init__(self, flySpeed)
    print("FlyingPerson init")

  def __str__(self):
    return Player.__str__(self) + " " + FlyingCreature.__str__(self)

def main():
  player = Player(name = "Player", heath = 100)
  player.walk()
  player.attack()
  player.attack()
  print(player)


  print("")
  print("")
  print("")

  warriorPlayer = WarriorPlayer(name = "WarriorPlayer", heath = 150)
  warriorPlayer.walk()
  warriorPlayer.attack()
  warriorPlayer.attack()
  print(warriorPlayer)

  print("")
  print("")
  print("")



  wizardPlayer = WizardPlayer(name = "WizardPlayer", heath = 80, manaMax = 5)
  wizardPlayer.walk()
  wizardPlayer.attack()
  wizardPlayer.attack()
  print(wizardPlayer)

if __name__ == "__main__": 
    main()
else: 
    print ("duongdt_Basic_005_OOP.py imported")
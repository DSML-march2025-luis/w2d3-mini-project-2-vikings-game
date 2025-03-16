import random


#
# Soldier
# 
class Soldier():
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
        self.health -= damage

#
# Viking
#
class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    
    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"

    def battleCry(self):
            return "Odin Owns You All!"


#
# Saxon
#
class Saxon(Soldier):
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"


#
# War
#
class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, vikingInstance):
        self.vikingArmy.append(vikingInstance)

    def addSaxon(self, saxonInstance):
        self.saxonArmy.append(saxonInstance)

    def vikingAttack(self):
        return self.armyAttack(self.vikingArmy, self.saxonArmy)

    def saxonAttack(self):
        return self.armyAttack(self.saxonArmy, self.vikingArmy)

    def armyAttack(self, attacking_army, defending_army):
        """
        implements a generic attack 
        (a random soldier from the attacking army attacks a random soldier from the defending army)
        """
        attacker = random.choice(attacking_army)
        defender = random.choice(defending_army)

        strength = attacker.attack()
        result = defender.receiveDamage(strength)

        if defender.health <= 0:
            defending_army.remove(defender)

        return result

    def showStatus(self):
        if not self.saxonArmy:
            return "Vikings have won the war of the century!"
        elif not self.vikingArmy:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
        

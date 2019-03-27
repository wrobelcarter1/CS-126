                                                            # Carter Wrobel
                                                            # CS126L
                                                            # Section 1
                                                            # 11/7/17

'''
    This will go through a sampele class name and
    the chapter 9 problems on objects and classes
'''
class Person:

    def __init__(self):
        self.nickname = ""
        self.characteristics = []

    def get_nickname(self):
        return self.nickname

    def set_nickname(self, x):
        self.nickname = x

    def get_characteristics(self):
        return self.characteristics

    def set_characteristics(self, x):
        self.characteristics = x



Carter = Person()
Carter.set_nickname("C-Wrobel")
Carter.set_characteristics(["Blonde", "Blue Eyes", "Tall",
                            "White", "Athletic"])

class Mutant:

    def __init__(self):
        self.identity = ""
        self.powers = []

    def get_identity(self):
        return self.identity

    def set_identity(self, x):
        self.identity = x

    def get_powers(self):
        return self.powers

    def set_powers(self, x):
        self.powers = x

wolverine = Mutant()
wolverine.set_identity("Jimmy Hudson")
wolverine.set_powers(["Healing Factor", "Retractable Bone Claws",
                      "Enhanced Senses"])
cyclops = Mutant()
cyclops.set_identity("Scott Summers")
cyclops.set_powers(["Projects concussive force from his eyes"])
gambit = Mutant()
gambit.set_identity("Remy LeBeau")
gambit.set_powers(["Explosive Kinetic Energy", "Enhanced Agility",
                   "Hypnotic charm"])

# Problem 1
x = cyclops.get_identity()
print(x)
# Scott Summers


# Problem 2
wolverine.powers[1]= "Adamantium Claws"
x = wolverine.powers
print(x)
# ['Healing Powers', 'Adamantium Claws', 'Enhanced Senses']


# Problem 3
cyclops.powers = "Laser Eyes"
x = cyclops.powers[0]
print(x)
# L


# Problem 4
professorX = Mutant()
professorX.set_identity("Charles Francis")
x = professorX.get_powers()
print(x)
# x = []


# Problem 5
x = cyclops.get_powers()
del(cyclops)
# print(cyclops)
# ERROR name 'cyclops' not found


# Problem 6
gambit.powers[0] = gambit.powers[1]
gambit.powers[2] = gambit.powers[0]
x = gambit.get_powers
print(x)
# <bound method Mutant.get_powers of <__main__.Mutant object at 0x10109d710>>


# Problem 7
x = gambit.get_powers().sort()
print(x)
# None


# Problem 8
storm = Mutant()
storm.set_identity("Ororo Monroe")
storm.set_powers("Weather manipulation")
x = storm.get_powers()[0]
print(x)
# W


# Problem 9
x = gambit.get_identity()
print(x)
# Remy LeBeau


# Problem 10
wolverine.set_identity("Hugh Jackman")
x = wolverine.get_identity()
print(x)
# Hugh Jackman


# Problem 11
x = isinstance(wolverine, Mutant)
print(x)
# True


# Problem 12
x = gambit is wolverine
print(x)
# False

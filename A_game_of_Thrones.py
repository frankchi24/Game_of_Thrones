import random

class chracter(object):

    def __init__(self, name, player, chracter_description, health, mana, attack_1,attack_2,attack_3):
        self.name = name
        self.player = player
        self.chracter_description = chracter_description
        self.health = health
        self.mana = mana
        self.attack_1 = attack_1
        self.attack_2 = attack_2
        self.attack_3 = attack_3

    def description(self):
        print self.chracter_description

    def attack(self,target,player_attack):
        if player_attack == True:
            # player pick moves
            while True:
                number_chose = int(raw_input(
                    "Pick an attack:\n1.%s \n2.%s \n3.%s \n>  "%(
                        self.attack_1['name'],
                        self.attack_2['name'],
                        self.attack_3['name']
                    )))-1
                moves = [self.attack_1,self.attack_2,self.attack_3]
                attack = moves[number_chose]
                # mana calculate
                if self.mana - attack['mana_consum'] >= 0:
                    break
                else:
                    print "no mana"
            #player attack calculate
            self.mana = self.mana - attack['mana_consum']
            target.health = target.health - attack["hurt"]
        else:
            # computer random pick moves
            attack = random.choice([self.attack_1, self.attack_2, self.attack_3])

            # mana calculate
            while self.mana - attack["mana_consum"] < 0:
                attack = random.choice([self.attack_1, self.attack_2, self.attack_3])

            # computer attack calcualate
            self.mana = self.mana - attack["mana_consum"]
            target.health = target.health - attack["hurt"]

        print attack["description"] % (self.name, target.name)        
        print "%s has %d health left" % (target.name, target.health)
        print "%s has %d mana left" % (target.name, target.mana)




Jon_Snow = chracter(
        "Jon Snow", 
        True,
        "I am Jon Snow.Bastard son of Lord Eddard Stark of Winterfell, lord commandar of the watch.",
        120,
        50,
        attack_1 = {
            "name" : "Long Claw",
            "description" : "%s swings his Long Claw at %s",
            "mana_consum": 0,
            "hurt" : 30},
        attack_2 = {
            'name':'Roar of Stark',
            'description':'%s roars and a warewolf jumps out and bites %s',
            'mana_consum':20,
            'hurt':30},
        attack_3 = {
              'name':'Night Watch',
              'description':'%s roars and a group of black men appear and attack %s',
              'mana_consum':20,
              'hurt':30
              }
        ) 
The_Red_Woman = chracter(
        "The Red Woman",
        False,
        "My name is Melisandre, may the lord of light be with you.",
        80,
        130,
        attack_1 = {
            "name" : "Seduction",
            "description" : "%s strips her cloth and gives %s a seductive smile.",
            "mana_consum": 0,
            "hurt" : 20},
        attack_2 = {
            'name':'Poison',
            'description':'%s offers %s a goblet of wine.',
            'mana_consum':20,
            'hurt':40},
        attack_3 = {
              'name':'The Shadow',
              'description':'%s summons a black shadow and it starts strangling %s',
              'mana_consum':50,
              'hurt':50,
              }
        )
Daenerys_Targaryen = chracter(
        "Daenerys Targaryen",
        False,
        "I am Daenerys Stormborn, of House Targaryen. Rightful heir to the Iron Throne, \
Queen of the Seven Kingdoms of Westeros, the Rhoynar, and the First Men. I am the Mother of Dragons, \
the Khaleesi of the Great Grass Sea, the Unburnt, and Breaker of Chains.",
        80,
        120,
        attack_1 = {
            'name':'The Unsullied',
            'hurt':30,
            'mana_consum':0,
            'description':'''%s shouts out:"Who will fight for me?!"\nA group of pikemen starts attacking %s''',
            },
        attack_2 = {
            'name':'Daario Naharis',
            'hurt':30,
            'mana_consum':20,
            'description':'''%s shouts out:"Who will fight for me?!"\nA strong man roars and swings his sword at %s''',
            },
        attack_3 = {
            'name':'Dracarys',
            'hurt':50,
            'mana_consum':120,
            'description':'%s roars and a dragon swoops in and breathes fire on %s'
            }    
        )
Tyrian_Lannister = chracter(
        "Tyrian Lannister",
        False,
        "I am Tyrian Lannister, the smartest man in Westero.",
        90,
        130,
        attack_1 = {
            'name':'Crossboat',
            'hurt':15,
            'mana_consum':0,
            'description':'%s takes out a crossboat and shoot %s',
            },
        attack_2 = {
            'name':'Poison',
            'hurt':30,
            'mana_consum':20,
            'description':'%s asks %s to drink with him, and ...',
            },
        attack_3 = {
            'name':'Wild Fire',
            'hurt':40,
            'mana_consum':90,
            'description':'%s takes out a bottle of green fire and pours it on %s',
            }    
        )
# Game Start Here
print "Welcome to Westeros!"
raw_input() 
# Pick chracter
print "May I ask your name, my Lord?"
chracters = [Jon_Snow,The_Red_Woman,Daenerys_Targaryen,Tyrian_Lannister]
chracter_player_chose  = int(raw_input("Pick a chracter:\n1. Jon Snow\n2. The Red Woman\n3. Daenerys Targaryen\n4. Tyrian Lannister\n>  "))-1

player = chracters[chracter_player_chose]
chracters.pop(chracter_player_chose)
target = random.choice(chracters)

print "You have chosen %s.\nhealth: %d\nmana:%d"%(player.name,player.health,player.mana)
player.description()
raw_input() 
print "Your target is %s\nhealth: %d\nmana:%d " %(target.name,target.health,target.mana)
target.description()
raw_input() 



while player.health > 0 and target.health > 0:
    player.attack(target,True)

    if player.health <= 0:
        print "You have been killed by %s"%(target.name)
        break
    
    elif target.health <= 0 :
        print "You have killed %s"%(target.name)
        break

    raw_input()
    target.attack(player,False)
    raw_input() 


print "Game Over"



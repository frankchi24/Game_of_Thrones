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

    def attack(self,target):
        # player pick move
        number_chose = int(raw_input(
            "Pick an attack:\n1.%s \n2.%s \n3.%s \n>  "%(
                self.attack_1['name'],
                self.attack_2['name'],
                self.attack_3['name']
            )))-1
        moves = [self.attack_1,self.attack_2,self.attack_3]
        attack = moves[number_chose]

        #player attack calculate
        self.mana = self.mana - attack["mana_consum"]
        target.health = target.health - attack["hurt"]
        print attack["description"] % (self.name, target.name)        
        print "%s has %d health left" % (target.name, target.health)
        print "%s has %d mana left" % (self.name, self.mana)

        raw_input()
        #computer random pick moves
        attack_back = random.choice([target.attack_1,target.attack_2,target.attack_3])
    
        target.mana = target.mana - attack_back["mana_consum"]
        self.health = self.health - attack_back["hurt"]
        print attack_back['description'] % (target.name, self.name)
        print "%s has %d health left" % (self.name, self.health)
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
              'description':'%s roars and a group of black man appear and attack %s',
              'hurt':30,
              'mana_consume':20,
              }
        )
The_Red_Woman = chracter(
        "The Red Woman",
        False,
        "My name is Melisandre, may the lord of light be with you.",
        100,
        100,
        attack_1 = {
            "name" : "Seduction",
            "description" : "%s strips her close and winks at %s",
            "mana_consum": 50,
            "hurt" : 30},
        attack_2 = {
            'name':'Roar of Stark',
            'description':'%s roars and a warewolf jumps out and bites %s',
            'mana_consum':20,
            'hurt':30},
        attack_3 = {
              'name':'Night Watch',
              'description':'%s roars and a group of black man appear and attack %s',
              'hurt':30,
              'mana_consume':20,
              }
        )
Daenerys_Targaryen = chracter(
        "The Red Woman",
        False,
        "My name is Daenerys Targaryen",
        100,
        100,
        attack_1 = {
            "name" : "Seduction",
            "description" : "%s strips her close and winks at %s",
            "mana_consum": 50,
            "hurt" : 30},
        attack_2 = {
            'name':'Roar of Stark',
            'description':'%s roars and a warewolf jumps out and bites %s',
            'mana_consum':20,
            'hurt':30},
        attack_3 = {
              'name':'Night Watch',
              'description':'%s roars and a group of black man appear and attack %s',
              'hurt':30,
              'mana_consume':20,
              }    
        )
# Game Start Here
print "Welcome to Westeros!"
raw_input() 
# Pick chracter
print "May I ask your name, my Lord?"
chracters = [Jon_Snow,The_Red_Woman,Daenerys_Targaryen]
chracter_player_chose  = int(raw_input("Pick a chracter:\n1. Jon Snow\n2. The Red Woman\n3. Daenerys Targaryen\n>  "))-1

player = chracters[chracter_player_chose]
chracters.pop(chracter_player_chose)
target = random.choice(chracters)

print "You have chosen %s."%(player.name)
player.description()
raw_input() 
print "Your target is %s\nhealth: %d\nmana:%d " %(target.name,target.health,target.mana)
target.description()

Jon_Snow.attack(The_Red_Woman)

# # pick target
# while Jon_Snow.health and The_Red_Woman.health > 0: 
#     Jon_Snow.attack(The_Red_Woman)
#     The_Red_Woman.attack(Jon_Snow,attack1)
#     print ""
#     print "-------------------------"

# print "%s has %d left" %(Jon_Snow.name, Jon_Snow.health)
# print "%s has %d left" %(The_Red_Woman.name, The_Red_Woman.health)
# print "%s has killed %s" %(Jon_Snow.name, The_Red_Woman.name)
# print "game over"
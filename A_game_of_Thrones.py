import random

class chracters(object):
    def __init__(self,name,attack_or_not):
        self.name = name
        if self.name == "Jon Snow":
            self.string = {   
                'name':'Jon Snow',
                'chracter_description':'I am Jon Snow.Son,bastard son of Lord Eddard Stark of Winterfell, lord commandar of the watch.',
                'health_hits':120,
                'mana_points':40,
            }
            self.attack_one={
                'name':'Long Claw',
                'hurt':30,
                'mana_consume':0,
                'description':'%s swings his LongClaw at %s',
            }
            self.attack_two={
                'name':'Roar of Stark',
                'hurt':30,
                'mana_consume':20,
                'description':'%s roars and a warewolf jumps out and bites %s',
            }
            self.attack_three={
                'name':'Nights watch',
                'hurt':30,
                'mana_consume':20,
                'description':'%s roars and a group of black man appear and attack %s',
            }
        elif self.name == "The Red Woman":
            self.string = {   
                'name':'The Red Woman',
                'chracter_description':'My name is Melisandre, may the lord of light be with you.',
                'health_hits':80,
                'mana_points':120,
            }
            self.attack_one={
                'name':'Seduction',
                'hurt':20,
                'mana_consume':10,
                'description':'%s strips her cloth and gaves %s a seductive smile.',
            }
            self.attack_two={
                'name':'Poison',
                'hurt':30,
                'mana_consume':0,
                'description':'%s offer %s a goblet of wine.',
            }
            self.attack_three={
                'name':'The Shadow',
                'hurt':30,
                'mana_consume':20,
                'description':'%s summon a black shadow and it starts strangling %s',
            }
        elif self.name == "Daenerys Targaryen":
            self.string = {   
                'name':'Daenerys Targaryen',
                'chracter_description':'''I am Daenerys Stormborn, of House Targaryen. Rightful heir to the Iron Throne,\
Queen of the Seven Kingdoms of Westeros, the Rhoynar, and the First Men.I am the Mother of Dragons, \
the Khaleesi of the Great Grass Sea, the Unburnt, and Breaker of Chains.''',
                'health_hits':80,
                'mana_points':120,
            }
            self.attack_one={
                'name':'The Unsullied',
                'hurt':30,
                'mana_consume':0,
                'description':'''%s shouts out:"Who will fight for me?!"\nA group of pikemen starts attacking %s''',
            }
            self.attack_two={
                'name':'Daario Naharis',
   
                'hurt':30,
                'mana_consume':20,
                'description':'''%s shouts out:"Who will fight for me?!"\nA strong man roars and swings his sword at %s''',
            }
            self.attack_three={
                'name':'Dracarys',
                'hurt':50,
                'mana_consume':120,
                'description':'%s roars and a warewolf jump out and hurt %s',
            }
        elif self.name == "Tyrian Lannister":
            self.string = {   
                'name':'Tyrian Lannister',
                'chracter_description':'I am Tyrian Lannister.',
                'health_hits':100,
                'mana_points':100,
            }
            self.attack_one={
                'name':'Long Claw',
                'hurt':30,
                'mana_consume':0,
                'description':'%s uses longclaw to hurt %s',
            }
            self.attack_two={
                'name':'Roar of Stark',
                'hurt':30,
                'mana_consume':20,
                'description':'%s roars and a warewolf jump out and hurt %s',
            }
            self.attack_three={
                'name':'Nights watch',
                'hurt':30,
                'mana_consume':20,
                'description':'%s roars and a warewolf jump out and hurt %s',
            }
        else:
            print "bugs!!"  
    def description(self):
        if self.attack_or_not == True:
            print "Your have chosen "+ self.string['name']+"\nYou have %d health points and %d mana points." \
            % (self.string['health_hits'],self.string['mana_points'])
            print self.string['chracter_description']   
            raw_input()
        else: 
            print "Your target is " + self.string['name'] + "\nwith %d health points and %d mana points." \
            % (self.string['health_hits'],self.string['mana_points'])
            print self.string['chracter_description']   
            raw_input()
    def attack(self):
        if computer.attack_or_not == True:
            which_attack = [1,2,3]
            attack = random.choice(which_attack)
        elif player.attack_or_not == True:
            attack = int(raw_input("Attack! Pick a number\n1."+ self.attack_one['name']+"\n2."+self.attack_two['name']+"\n3."+self.attack_three['name']+"\n> "))
        else:
            print "bugs"
        
        if attack == 1:
            attack_type = self.attack_one
        elif attack == 2:
            attack_type = self.attack_two
        elif attack == 3:
            attack_type = self.attack_three
        else:
            print "Please type in a number, my lord."
            return self.attack()   

        if player.attack_or_not==True:
            if player.string['mana_points']-attack_type['mana_consume'] >= 0:
                print attack_type['description'] % (player.name,computer.name)
                computer.string['health_hits'] = computer.string['health_hits'] - attack_type['hurt']
                player.string['mana_points'] = player.string['mana_points'] - attack_type['mana_consume']
                print "%s health : %d mana :%d " % (player.name,player.string['health_hits'],player.string['mana_points'])
                print "%s health : %d mana :%d" % (computer.name,computer.string['health_hits'],computer.string['mana_points'])
            else: 
                print "No mana."
                return player.attack()  

        elif computer.attack_or_not == True:
            if  computer.string['mana_points']-attack_type['mana_consume'] >= 0:
                print attack_type['description'] % (computer.name,player.name)
                player.string['health_hits'] = player.string['health_hits'] - attack_type['hurt']
                computer.string['mana_points'] = computer.string['mana_points'] - attack_type['mana_consume']
                print "%s health : %d mana :%d " % (player.name,player.string['health_hits'],player.string['mana_points'])
                print "%s health : %d mana :%d" % (computer.name,computer.string['health_hits'],computer.string['mana_points'])
            else: 
                return computer.attack()  
        else:
            print "bugs"
    
def combact(player,computer):
    while computer.string['health_hits'] > 0 and player.string['health_hits'] > 0:
        print "Player attacks"
        player.attack()
        raw_input("  ")   
        if computer.string['health_hits'] <= 0 or player.string['health_hits'] <= 0:
            break   
        else:
            player.attack_or_not = False
            computer.attack_or_not = True
            computer.attack()
            raw_input("  ")
            player.attack_or_not = True
            computer.attack_or_not = False  

    if computer.string['health_hits'] <= 0 and player.string['health_hits'] >= 0:   
        print "Your just killed %s." % (computer.name)
    else:
        print "You are killed by %s." %(computer.name)



#instanciate 4 objects
#Assign 4 chracters objects into a list
chracter_objects = [chracters("Jon Snow",False),chracters("The Red Woman",False),chracters("Daenerys Targaryen",False),chracters("Tyrian Lannister",False)]

print "Welcome to Westeros!"
raw_input() 
print "May I ask your name, my Lord?"
#opening greeting 
chracter_player_chose   = int(raw_input("Pick a chracter:\n1. Jon Snow\n2. The Red Woman\n3. Daenerys Targaryen\n4. Tyrian Lannister\n>  "))-1
#Ask users pick a number from a list, assingn it to the variable chracter_player_chose
#Minus 1 to get the right one in list, will need a if statement to rule out wrong input
number_list = [0,1,2,3]
if chracter_player_chose not in number_list:
    chracter_player_chose = int(raw_input("Pick a chracter:\n1. Jon Snow\n2. The Red Woman\n3. Daenerys Targaryen\n4. Tyrian Lannister\n>  "))-1
else:
    player = chracter_objects[chracter_player_chose]
    #Assign the number of the list
    #plyaer varialbe now equals the object users choose

chracter_objects.pop(chracter_player_chose)
#delete the object users chose
computer = random.choice(chracter_objects)
#computer randomly choose an opponent from the chracter list 

player.attack_or_not = True
computer.attack_or_not = False
# set the flag on player and computer, know which is attacking and assgin right description
player.description()
computer.description()
combact(player,computer)


print "Game Over"
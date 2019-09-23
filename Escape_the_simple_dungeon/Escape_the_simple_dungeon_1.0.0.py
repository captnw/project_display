import random # get random functionality

actiondictionary = {'Sword':{"Inspect":"Rusted metal weapon. It boosts your attack by ? points.","Equip":7}, 'Candy':{"Inspect":"Sealed package with faded logo that says \"Nice candy\". It raises your health by ? points.","Eat":7}}
enemydictionary = {'Bat':{"hp":2,"dmg":3},'Skeleton':{"hp":7,"dmg":5},'Dark_Knight':{"hp":30,"dmg":13},'GRAND_DAD':{"hp":999,"dmg":50},'Golem':{"hp":60,"dmg":7}}
phealth = 20
pattack = 5
roomwandl = 6 # room size

rooms = [["?" for i in range(roomwandl)] for i in range(roomwandl)]
stuffinrooms = [["?" for i in range(roomwandl)] for i in range(roomwandl)]
inventory = [] # just append name of objects to inventory list, the actions can be referred by looking at actiondictionary
enemiesslain = [] # just append to this list for the enemies that player slain
typed = "not valid"
startgame, aboutmode, quitgame, waitmode = False, False, False, False
positionx, positiony = random.randint(0,roomwandl-1), random.randint(0,roomwandl-1)

exitx, exity = random.randint(0,roomwandl-1), random.randint(0,roomwandl-1) # this code chunk just makes sure that the the exit position is not the same as player position
while exitx==positionx and exity==positiony:
  exitx, exity = random.randint(0,roomwandl-1), random.randint(0,roomwandl-1)

exitdiscovered = False
rooms[positiony][positionx] = "@"
stuffinrooms[positiony][positionx] = "@"
stuffinrooms[exity][exitx] = "O"

# ~~~~~~~~~~~~~~~~~~~~~~~~~ Variable declaration zone ~~~~~~~~~~~~~~~~~~~~~~~~~~

def begin():
  print('}Escape the simple dungeon - a text adventure game version 1.0.0')
  print('}Type \'begin\' to play, \'about\' to read credits, or \'quit\' to quit')

def checkphrase(word, stringexamine): # instead of a long if statement for checking if a characters in a word is in the right order, use this.
  # NOTE CHECKPHRASE WILL NOT WORK WITH PHRASES THAT HAVE MORE THAN ONE OF THE SAME LETTER IN THEM ... LIKE "CHOCOLATE" (TWO O'S!)
  condition = True
  word = word.lower()
  spaceindex = stringexamine.find(" ") # if this is not -1, it means there's more than one word
  lastwordindex = -1 # the index of the char in the typed var (but fits the word)
  for index in range(len(word)): # does the input have these character?
    if stringexamine.find(word[index]) < 0:
      condition = False
    else:
      if index == (len(word)-1): # basically if the last word exists ...
        lastwordindex = stringexamine.find(word[index]) # save the position of the index
  
  if spaceindex>-1: # This deals with inputs that have spaces (two words)
    tempslice = -1
    if lastwordindex>spaceindex: # if the word we're looking for is after the space
      tempslice = stringexamine[spaceindex+1:]  # return the position of the beginning of the word ... then return position of the end of the word ... we will only examine that interval.
    else: # otherwise the word is before the space 
      tempslice = stringexamine[:spaceindex]
    if len(word)!=len(tempslice): # if "tempslice" different length than "word" this will avoid the 'string index out of range' problem / we'll know that this isn't the word
      condition = False
      return condition
    for index in range(1,len(tempslice)):
      if tempslice.find(word[index]) < tempslice.find(word[index-1]): 
        condition = False
  else: # This deals with inputs that has only 1 space (1 word)
    for index in range(1,len(word)): # is the word in order?
      if stringexamine.find(word[index]) < stringexamine.find(word[index-1]): 
        condition = False
  return condition 

def drawBoard(): # DRAWS THE BOARD
  for i in range(len(rooms)):
    print("----",end="")
  print("")
  for elementnum in range(len(rooms)): 
    for listelement in range(len(rooms[elementnum])):
      if listelement==0:
        print("[ "+str(rooms[elementnum][listelement])+" ", end="")
      else:
        print("| "+str(rooms[elementnum][listelement])+" ", end="") # concat string and add to the end of each other
    print("]") # new line
  for i in range(len(rooms)):
    print("----",end="")
  print("")

def checkmode(): # returns False/True, False/True, etc .. based on if a word exists in input
  if checkphrase('quit',typed): # if you type these arguments in your input ... chooses argument based on input
    return False, False, True, False
  elif checkphrase('about',typed):
    return False, True, False, False
  elif checkphrase('begin',typed): # doesn't work with 'Start' for some reason
    return True, False, False, False
  else: # need to do this so it won't have a NoneType error
    return False,False,False,True

def damagedeal(maxdmg, attacker, victimhp): # Damage dealing client .. has print statements for attack and returns the hp for the player / enemy attacked.
  whosedmg=random.randint(1,maxdmg) # utilizes random module from imported random library
  victimhp-=whosedmg
  if attacker=="Player":
    if whosedmg>10:
      print("}You smighted the enemy with "+str(whosedmg)+" damage!")
    elif whosedmg>7:
      print("}You striked the enemy with "+str(whosedmg)+" damage.")
    elif whosedmg>4: 
      print("}You slashed the enemy with "+str(whosedmg)+" damage.")
    elif whosedmg>2:
      print("}You attacked for "+str(whosedmg)+" damage.")
    elif whosedmg<=2:
      print("}You fumbled and hurt the enemy for "+str(whosedmg)+" damage.")
    return victimhp
  else:
    if whosedmg>10:
      print("}You were devasted for "+str(whosedmg)+" damage!")
    elif whosedmg>7:
      print("}You were struck for "+str(whosedmg)+" damage.")
    elif whosedmg>4: 
      print("}You were slashed for "+str(whosedmg)+" damage.")
    elif whosedmg>2:
      print("}You were damaged for "+str(whosedmg)+" hitpoints.")
    elif whosedmg<=2:
      print("}You were slapped? for "+str(whosedmg)+" damage.")
    return victimhp

def checkwin(): # this is a real simple function ... just returns True.
  if positionx == exitx and positiony == exity:
    rooms[positiony][positionx]="O"
    stuffinrooms[positiony][positionx]="O"
    print("}You stumble upon what appears to be an exit.")
    return True 
  
def movement(px,py): # returns playerx, and playery respectively (px = positionx, py = positiony)
  if stuffinrooms[py][px]!="O" and stuffinrooms[py][px]!="X":
    rooms[py][px]="_" # clears player at old position, add underscore to show that it was "explored"
    stuffinrooms[py][px]="_"
  elif stuffinrooms[py][px]=="X": # only change to an underscore for the other function to update the locatio nf the chest after the player leaves that room.
    rooms[py][px]="_"
  if checkphrase("up",typed):
    if py==0:
      print("}You hit a wall. Unable to move up.")
      return px, py    
    py-=1
  elif checkphrase("down",typed):
    if py==(roomwandl-1): # last index would be one less than roomwandl ... arrays start at 0 
      print("}You hit a wall. Unable to move down.")
      return px, py    
    py+=1
  elif checkphrase("left",typed):
    if px==0:
      print("}You hit a wall. Unable to move left.")
      return px, py 
    px-=1
  elif checkphrase("right",typed):
    if px==(roomwandl-1): # last index would be one less than roomwandl ... arrays start at 0 
      print("}You hit a wall. Unable to move right.")
      return px, py    
    px+=1
  else:
    print("}Type a direction along with move. Example:\"Move right\"")
  return px, py
    
def events(): # This function does the random events when you go to a room you haven't discovered.
  if stuffinrooms[positiony][positionx]=="?":
    chance = random.randint(1,10)
    if chance<6:
      print("}You see an empty room.")
    elif chance<9:
      print("}Enemy encounter!", end=" ")
      enemchance = random.randint(1,10)
      ranenemy = chooserandomenemy(enemchance)
      fightmode=False
      responded=False
      global phealth# use global statement
      while not responded:
        print("}Do you attack? You will not be able to escape the battle. (Type 'fight') Or do you run away (Type 'run')?. You WILL get damaged by running.")
        eventresponse = str(input())
        eventresponse = eventresponse.lower()
        if checkphrase("fight",eventresponse):
          print('}You\'re fighting '+ranenemy+' with '+str(enemydictionary[ranenemy]["hp"])+ ' hitpoints and '+str(enemydictionary[ranenemy]["dmg"])+' potential damage.')
          fightmode=True
          enemhp = enemydictionary[ranenemy]["hp"]
          while fightmode==True:
            if enemhp<=0: 
              print('}You\'ve slain the '+ranenemy+'.')
              enemiesslain.append(ranenemy)
              fightmode=False
            elif phealth<=0:
              print('}The '+ranenemy+' had struck a fatal blow ... You feel extremely weak.')
              fightmode=False
            if fightmode: # if the battle is over, don't do this again.
              enemdmg = enemydictionary[ranenemy]['dmg']
              print("}Your current health is "+str(phealth)+" and current potential damage is "+str(pattack)+" hitpoints.")
              print("}Your enemy has "+str(enemhp)+" hitpoints and is able to damage you for a max of "+str(enemdmg)+ " hitpoints.\n")
              print("}Type 'fight' to attack and 'block' to block a 1/4 of the damage.")
              eventresponse = str(input())
              eventresponse = eventresponse.lower()  
              
              if checkphrase("fight",eventresponse):
                print("}You engage the enemy!")
                enemhp = damagedeal(pattack,'Player',enemhp)
                if enemhp<=0:
                  print("}The "+ranenemy+" was struck with a fatal blow!")
                else:
                  print("}The enemy swings back!")
                  phealth = damagedeal(enemdmg,'enem',phealth)
              elif checkphrase("block",eventresponse):
                print("}You raise your fists to defend.")
                print("}The enemy strikes!")
                enemreduceddmg = enemdmg - (enemdmg//4)
                if enemreduceddmg < 0:
                  enemreduceddmg=0 
                phealth = damagedeal(enemreduceddmg,'enem',phealth)
              else:
                print("}You need to type 'fight' or 'block'!")
          responded=True
        elif checkphrase("run",eventresponse):
          print("}Running away ...",end=" ")
          randamage = random.randint(0,(enemydictionary[ranenemy]["dmg"])//0.80)+1 # enemy gets a free hit on you, but their attack is slightly increased and increased by 1.
          phealth-=randamage
          print("the "+ranenemy+" inflicted "+str(randamage)+" damage on you before you got away!")
          responded=True
      print("}The room is now empty, and the enemy is nowhere to be found.")
    elif chance>=9:
      print("}Chest found!")
      chance=random.randint(1,3)
      print("}You've obtained "+str(chance)+" item(s)!")
      for i in range(chance):
        obtain, obtainstat = random.choice(list(actiondictionary.items())) # USE THIS FOR RANDOM ITEMS IN CHESTS.
        print("}A "+str(obtain)+" was added to your inventory.")
        inventory.append(obtain)
      stuffinrooms[positiony][positionx]="X"
  elif stuffinrooms[positiony][positionx]=="_":
    print("}You've been in this empty room.")
  elif stuffinrooms[positiony][positionx]=="X":
    print("}You remembered opening a chest in this empty room.")

def updatelocation(): # this just marks the rooms with chests with an X if you find a chest in them. This overides the underscore marker.
  for rowindex in range(len(stuffinrooms)):
    for elemindex in range(len(stuffinrooms[rowindex])):
      if stuffinrooms[rowindex][elemindex]=="X" and rooms[rowindex][elemindex]!="@": # This will only work if the @ is changed to a _.
        rooms[rowindex][elemindex]="X"
      
def chooserandomenemy(thechance): # it just returns enemies depending on what "thechance" is.
  if thechance<5:
    print("It's a bat\n")
    return "Bat"
  elif thechance<8:
    print("It's a skeleton\n")
    return "Skeleton"
  elif thechance<10:
    print("It's a dark knight\n")
    return "Dark_Knight"
  elif thechance==10:
    ranchance2=random.randint(1,10)
    if ranchance2<6: 
      print("A golem appears!\n")
      return "Golem"
    else: # GRAND_DAD has 5% chance of appearing. good luck meeting him.
      print("GRAND_DAD appears! You feel his strong presence . . .\n")
      return "GRAND_DAD"

def interact(option): # This is how you would interact the items in your inventory ... Like "Equip sword" or "Eat candy"
  global phealth
  global pattack
  if checkphrase("candy",typed) and "Candy" in inventory and option=="Inspect":
    print(actiondictionary["Candy"]["Inspect"])
  elif checkphrase("candy",typed) and "Candy" in inventory and option=="Eat":
    ranhp=random.randint(1,actiondictionary["Candy"]["Eat"])
    oldhp=phealth
    phealth+=ranhp
    print("}You munch on the candy. You increase your "+str(oldhp)+" hp to a "+str(phealth)+" hp by "+str(
      ranhp)+" health points.")
    inventory.remove("Candy")
  elif checkphrase("sword",typed) and "Sword" in inventory and option=="Inspect":
    print(actiondictionary["Sword"]["Inspect"])
  elif checkphrase("sword",typed) and "Sword" in inventory and option=="Equip":
    ranattackup=random.randint(1,actiondictionary["Sword"]["Equip"])
    oldattack=pattack
    pattack+=ranattackup
    inventory.remove("Sword")
    print("}You somehow equipped the sword. It increased your existing "+str(oldattack)+" dmg to a "+str(pattack)+" dmg by "+str(ranattackup)+" damage points.")
  else:
    print("}What do you mean by \'"+str(typed)+"\'? You might be missing an item from your inventory to do that.")

begin()
typed = str(input())
typed = typed.lower()
startgame, aboutmode, quitgame, waitmode = checkmode() # checkmode returns True/False

while not checkphrase('quit',typed) and not quitgame: # while the player didn't decide the quit
  if aboutmode:
    print('}Made in June 1, 2018 for a intro to programming final project.')
    print('}By William Nguyen\n')
    print('}Special thanks to Mr. Lavrov for being an awesome teacher.') # Thank you for all you do.
    print('}press \'begin\' to start and \'quit\' to quit')
    typed = str(input())
    typed = typed.lower()
    startgame, aboutmode, quitgame, waitmode = checkmode()
    if not startgame and not quitgame: # if the player decides to type in random stuff ... stay in "aboutmode"
      startgame, aboutmode, quitgame, waitmode = False, True, False, False
  elif waitmode:
    print('}You should type one of the following:')
    print('}Type \'begin\' to play, \'about\' to read credits, or \'quit\' to quit')
    typed = str(input())
    typed = typed.lower()
    startgame, aboutmode, quitgame, waitmode = checkmode() # checkmode returns True/False
  elif startgame:
    if checkphrase("move",typed):
      positionx, positiony = movement(positionx, positiony)
      events() # this is the event handler
      rooms[positiony][positionx] = "@" # don't do stuffinrooms[positiony][positionx] = "@" ... this will break other code
      updatelocation()
    if checkphrase("help", typed):
      print('}Some directions you can type: left, right, up, down. You cannot go pass the boundries of the grid.')
    if checkphrase("self", typed): # This checks your stats and inventory!
      print('}Your health is: '+str(phealth)+' hitpoints, and you can do up to a maximum of '+str(pattack)+ ' damage.')
      print('}Your inventory consists of:',end=' ')
      for item in inventory:
        print(item,end=' ')
      if len(inventory)>0: # if there is at least something in the inventory ...
        print('')
        print('}Things you can do with your inventory:', end=' ')
        for key, val in actiondictionary.items():
          for key2, val2 in actiondictionary[key].items():
            if key in inventory: # if the candy / sword is in the inventory
              print(key2, key, end=' | ')
        print('')
      else:
        print("nothing.")
    if checkphrase("inspect", typed):
      interact("Inspect")
    elif checkphrase("eat",typed):
      interact("Eat")
    elif checkphrase("equip",typed):
      interact("Equip")
    drawBoard() # draw the board
    
    # this is my 'dev view'. Where i can see the exit of the dungeon.
    #if checkphrase("son", typed): 
    #  for a in range(len(stuffinrooms)): 
    #    for b in range(len(stuffinrooms[a])):
    #      print(" "+str(stuffinrooms[a][b])+" ", end="") # concat string and add to the end of each other
    #    print("|\n") # new line
    
    if checkwin():
      print('}You can keep moving (type "move left" or something). Or you can leave the dungeon by typing \'out\'.')
      if checkphrase('out', typed):
        print('}Leaving the dungeon . . .')
        print('}Your stats are as follows: ')
        print('}You have '+str(phealth)+' health points remaining.')
        print('}Your inventory currently contains: ',end=' ')
        if len(inventory)==0:
          print('nothing')
        for item in inventory:
          print(item,end=', ')
        print('')
        print('}You\'ve slain: ',end=' ')
        if len(enemiesslain)==0:
          print('nobody')
        for item in enemiesslain:
          print(item,end=', ')
        print('')
        quitgame=True
      else:
        typed = str(input())
        typed = typed.lower()
    else: # you either are at the door (win) or not at the door (not win)
      if phealth<=0: # if you're dead ...
        phealth=0
        print('}You collapse on the ground. Gameover.')
        print('}Your stats are as follows: ')
        print('}You have '+str(phealth)+' health points remaining.')
        print('}Your inventory currently contains: ',end=' ')
        if len(inventory)==0:
          print('nothing')
        for item in inventory:
          print(item,end=', ')
        print('')
        print('}You\'ve slain: ',end=', ')
        if len(enemiesslain)==0:
          print('nothing')
        for item in enemiesslain:
          print(item,end=', ')
        print('')
        quitgame=True
        break
      print('}Type \'move direction\' to move your icon (@). Type \'Help\' for some help. Type \'self\' to check your stats and inventory. Or type \'quit\' if you want to stop playing.')
      typed = str(input())
      typed = typed.lower()
print('}Thanks for playing!')

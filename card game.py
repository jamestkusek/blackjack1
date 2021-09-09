import random
import tkinter as tk
from PIL import Image, ImageTk
import time
cards = []
suits = ["Hearts","Diamonds","Spades","Clubs"]
picturecards = ["Ace","Jack","Queen","King"]
playernum = 5
playerdecks = []
scorescounter = []
status = []
for i in range(0,playernum):
    status.append([])
masterwindow = tk.Tk()
masterwindow.geometry("825x400+0+0")


cardcounter = []
for x in range(playernum):
    cardcounter.append([])
print(cardcounter)

    
        


def shuffling():
    for i in range(2,10):
        for x in suits:
            cards.append((x,i))
    for x in suits:
        for i in picturecards:
            cards.append((x,i))

def dealing():
    for i in range(playernum):
        playerdecks.append([])
    for x in  playerdecks:
        for i in range(0,2):
            card = random.choice(cards)
            x.append(card)
            cards.remove(card)

        

def roundcheck():
    global scorescounter
    scorescounter = []
    for x in playerdecks:
        playerscore = 0
        for i in x:
            try:
                int(i[1])
                playerscore += int(i[1])
            except ValueError:
                if i[1] == "Ace":
                    playerchoice = input("Player " + str(playerdecks.index(x) + 1) + ", Enter value of your Ace: 1 or 11")
                    while playerchoice != "11" and playerchoice != "1":
                        playerchoice = input("Player " + str(playerdecks.index(x) + 1) + ", Enter value of your Ace: 1 or 11")
                    if playerchoice == "11":
                        playerscore += 11
                    else:
                        playerscore += 1
                    playerscore += 0
                else:
                    playerscore += 10
        if playerscore > 21:
            print("Player " + str(playerdecks.index(x) + 1) +" has gone bust at " + str(playerscore))
            scorescounter.append(0)
        else:
            print("Player " + str(playerdecks.index(x) + 1) +"'s score is " + str(playerscore))
            scorescounter.append(playerscore)
def cardnaming():
    
    global cardimages
    cardimages = []
    for x in playerdecks:
        cardimages.append([])
    for x in range(len(cardimages)):
        for y in playerdecks[x]:
            cardimages[x].append([])
        
        
           
            

    for x in playerdecks:
        currentpos = playerdecks.index(x)
        for i in range(len(x)):
            try:
                int(x[i][1])
                cardimages[currentpos][i].append(str(x[i][1]))
            except ValueError:
                cardimages[currentpos][i].append(str(x[i][1][0]))
            cardimages[currentpos][i].append(str(x[i][0][0]))
       

def carddisplayprocedure():
    coordinatecount = 0
    for x in cardimages:
        for y in x:
            carddisplay = tk.Label(masterwindow)
            carddisplay.place(x=25 + coordinatecount, y = 200)
            cardname = (y[0] + y[1] + ".png")
            card = Image.open(str("/home/jtk/Documents/" + cardname))
            card = card.resize((50,75))
            card = ImageTk.PhotoImage(card)
            carddisplay.photo = card
            carddisplay["image"] = card
            coordinatecount += 20
            time.sleep(0.1)
        playercaption = tk.Label(text="Player " + str(cardimages.index(x)+1))
        playercaption.place(x= coordinatecount - 15, y = 290)    
        coordinatecount += 120
    carddisplay.update()

def scoredisplay():
    coordinatecount = 0
    print(scorescounter)
    for x in scorescounter:
        playerscore = tk.Label(text="Score: " + str(x))
        playerscore.place(x = 25 + coordinatecount, y = 310)
        playerscore.update()
        coordinatecount += 160
        print("Yes")
        



        
    
                        
       
def gameround():
    global scorescounter
    for x in playerdecks:
        playerposition = playerdecks.index(x)
        if status[playerposition] == ['S']:
            continue
        else:
            stickorhit = input("Player " + str(playerposition + 1) + ", type H for hit, S for stick")
            while stickorhit != "H" and stickorhit != "S":
                stickorhit = input("Player " + str(playerposition + 1) + ", type H for hit, S for stick")
            if stickorhit == "H":
                global newcarddetails
                global playerinfo
                playerinfo = playerdecks.index(x)
                newcard = random.choice(cards)
                x.append(newcard)
                newcarddetails = newcard
                cardcounter[playerdecks.index(x)].append("1")
                cardaddprocedure()

            else:
                status[playerposition].append("S")

              
                
       
    

def cardaddprocedure():
    try:
        str(newcarddetails[1][0])
        cardname = (str(newcarddetails[1][0]) + str(newcarddetails[0][0]) + ".png")
    except TypeError:
        cardname = (str(newcarddetails[1]) + str(newcarddetails[0][0]) + ".png")
    print(cardname)
    print(playerinfo)
    print(cardcounter)
    cardadd = tk.Label(masterwindow)
    cardadd.place(x=25 + (160*int(playerinfo)) + (20*(len(cardcounter[playerinfo])+ 1)), y = 200)
    print(len(cardcounter[playerinfo]))
    card2 = Image.open(str("/home/jtk/Documents/" + cardname))
    card2 = card2.resize((50,75))
    card2 = ImageTk.PhotoImage(card2)
    cardadd.photo = card2
    cardadd["image"] = card2
    cardadd.update()
    


                
shuffling()
dealing()
cardnaming()
carddisplayprocedure()
roundcheck()
scoredisplay()

for i in range(3):
    gameround()


### so far everything working well :)###
###current next steps###

# "hit" and "stick" widgets. should be added during carddisplayprocedure and remain throughout game
# widgets trigger modified version of roundcheck loop
# get game update working "player has gone bust at" and "player wins the round" after everyone sticks.












    
   





            






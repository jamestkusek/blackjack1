import random
import tkinter as tk
from PIL import Image, ImageTk
import time
cards = []
suits = ["Hearts","Diamonds","Spades","Clubs"]
picturecards = ["Ace","Jack","Queen","King"]
playernum = 5
playerdecks = []
masterwindow = tk.Tk()
masterwindow.geometry("825x600")
mastercanvas = tk.Canvas(width=825, height = 1000)
mastercanvas.pack()
global cardref
cardref = []
global status
status = []
global scorescounter
scorescounter = []
for i in range(playernum):
    cardref.append([])
    status.append([])
def setup():
    
    global cardcounter
    cardcounter = []
    for x in range(playernum):
        cardcounter.append([])
    for i in range(2,10):
        for x in suits:
            cards.append((x,i))
    for x in suits:
        for i in picturecards:
            cards.append((x,i))

    for i in range(playernum):
        playerdecks.append([])
    for x in  playerdecks:
        for i in range(0,2):
            card = random.choice(cards)
            x.append(card)
            cards.remove(card)
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
       
    
    for x in cardimages:
        coordinatecount = 0
        for y in x:
            carddisplay = tk.Label(masterwindow)
            cardname = (y[0] + y[1] + ".png")
            card = Image.open(str("/home/jtk/Python Things/assets/" + cardname))
            card = card.resize((75,100))
            card = ImageTk.PhotoImage(card)
            carddisplay.photo = card
            cardimage = mastercanvas.create_image(50 + (165* cardimages.index(x)) + coordinatecount,200, image = card)
            cardref[cardimages.index(x)].append(cardimage)
            mastercanvas.update()
            time.sleep(0.1)
            coordinatecount += 25
        mastercanvas.create_text(50 + (165* cardimages.index(x)),260, text = "Player " + str(cardimages.index(x)+1))
        mastercanvas.update()
    
                        
     
def gameround():
    while min(status) != ["1"]:
        for x in playerdecks:
            
            global playerposition
            playerposition = playerdecks.index(x)
            if status[playerposition] == ['1']:
                continue
            else:
                global proceed
                proceed = tk.IntVar()
                decision1 = tk.Button(text = "Stick", height = 1, width = 1, command = stick)
                decision2 = tk.Button(text = "Hit", height = 1, width = 1, command = hit)
                decision1.place(x = 22 + (150* playerposition) , y = 290)
                decision2.place(x= 57 + (150* playerposition) , y = 290)
                mastercanvas.update()
                masterwindow.wait_variable(proceed)
                decision1.destroy()
                decision2.destroy()
                mastercanvas.update()
                if min(status) == ["1"]:
                    endscore()
            


def stick():
    status[playerposition].append("1")
    for b in cardref[playerposition]:
        mastercanvas.move(b, 0, -30)
        mastercanvas.update()
        proceed.set(1)
        
def hit():
        global newcard
        newcard = random.choice(cards)
        playerdecks[playerposition].append(newcard)
        cardcounter[playerposition].append("1")
        cardaddprocedure()
        acecount = 0
        playerscore = 0
        for a in playerdecks[playerposition]:
            try:
                int(a[1])
                playerscore += int(a[1])
            except ValueError:
                if a[1] == "Ace":
                    acecount += 1
                else:
                    playerscore += 10
                

            if (playerscore + (1 * acecount)) > 21:
                print("Player " + str(playerposition + 1) + " has gone bust.")
                bust = tk.Label(masterwindow)
                cross = Image.open(str("/home/jtk/Python Things/assets/cross.png"))
                cross = cross.resize((70,70))
                cross = ImageTk.PhotoImage(cross)
                bust.photo = cross
                cross = mastercanvas.create_image(75 + (165*int(playerposition)) + 12.5*(len(cardcounter[playerposition]) - 1) ,200, image = cross)
                mastercanvas.update()
                playerscore = 0
                status[playerposition].append("1")
                proceed.set(1)
            else:
                playerscore += acecount
                        
                
                
        proceed.set(1)
                

              

    

def cardaddprocedure():
    try:
        str(newcard[1][0])
        cardname = (str(newcard[1][0]) + str(newcard[0][0]) + ".png")
    except TypeError:
        cardname = (str(newcard[1]) + str(newcard[0][0]) + ".png")
    
    cardadd = tk.Label(masterwindow)
    card2 = Image.open(str("/home/jtk/Python Things/assets/" + cardname))
    card2 = card2.resize((75,100))
    card2 = ImageTk.PhotoImage(card2)
    cardadd.photo = card2
    card = mastercanvas.create_image(50 + (165*int(playerposition)) + (25*(len(cardcounter[playerposition])+ 1)),200, image = card2)
    cardref[int(playerposition)].append(card)
    mastercanvas.update()
  

def endscore():
    global acecount
    global playerscore
    for x in playerdecks:
        playerposition = playerdecks.index(x)
        acecount = 0
        playerscore = 0
        for a in x:
            try:
                int(a[1])
                playerscore += int(a[1])
            except ValueError:
                if a[1] == "Ace":
                    acecount += 1
                else:
                    playerscore += 10
        if acecount > 0:
            acedecision()
            scorescounter.append(playerscore)
        else:
            scorescounter.append(playerscore)

    
    for i in range(0, playernum):
        if scorescounter[i] > 21:
            mastercanvas.create_text(150,(350 + (i * 20)),text=("Player "+str(i+1)+" went bust at "+str(scorescounter[i])+"."))
        else:
            mastercanvas.create_text(150,(350 + (i * 20)),text=("Player "+str(i+1)+" finishes with a score of "+str(scorescounter[i])+"."))
            mastercanvas.update()
            time.sleep(0.1)
    for x in scorescounter:
        position = scorescounter.index(x)
        if x > 21:
            scorescounter[position] == 0
            print(scorescounter[position])
            
    winningplayer = max(scorescounter)
    mastercanvas.create_text(150,(350 + (playernum* 30)),text=("Player "+ str(int(scorescounter.index(winningplayer))+1)+" WINS with a score of "+str(max(scorescounter))))
    mastercanvas.update()
    

def acedecision():
    global playerscore
    if playerscore + (11 * acecount) < 21:
        playerscore += 11 * acecount
        return
    elif playerscore + (11 * (acecount- 1)) + 1*1 < 21:
        playerscore += (11 * (acecount- 1)) + 1*1
        return
    elif playerscore + (11 * (acecount- 2)) + 1*2 < 21:
        playerscore += (11 * (acecount- 2)) + 1*2
        return
    elif playerscore + (11 * (acecount- 3)) + 1*3 < 21:
        playerscore += (11 * (acecount- 3)) + 1*3
        return
    else:
        playerscore += (1 * 4)
        return
                

    
setup()
gameround()

####all that is needed now is to exclude players who are bust from the scorescounter list (maybe make a seperate list for people who arent bust#
#so the winner printed is in fact the winner#

#pretty much done after that :))) well done#















    
   





            






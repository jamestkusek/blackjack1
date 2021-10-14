import random
import tkinter as tk
from PIL import Image, ImageTk
import time
import tkinter.font as tf
cards = []
suits = ["Hearts","Diamonds","Spades","Clubs"]
picturecards = ["Ace","Jack","Queen","King"]
playernumber = (input("How many Players?"))

while playernumber not in ["2", "3", "4", "5", "6", "7", "8"]:
    playernumber = (input("How many Players?"))

playernum = int(playernumber)
playerdecks = []
masterwindow = tk.Tk()
geometrysize = str(str((playernum * 165)) +"x600")         
masterwindow.geometry(geometrysize)
masterwindow.resizable(0,0)
mastercanvas = tk.Canvas(width = playernum * 165, height = 1000)
mastercanvas.pack()
exitbutton = tk.Button(text = "Exit.", height = 1, width = 3,bg = "RED",command = masterwindow.destroy)
exitbutton.place(x = 125 +  165* (playernum-1), y = 10)
title = mastercanvas.create_text(100, 20, font = ("Gothic",30), text="Blackjack", )
mastercanvas.update
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
            card = Image.open(str("assets/" + cardname))
            card = card.resize((65,86))
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
                decision1 = tk.Button(text = "Stick", height = 1, width = 3, command = stick)
                decision2 = tk.Button(text = "Hit", height = 1, width = 3, command = hit)
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
                bust = tk.Label(masterwindow)
                cross = Image.open(str("assets/cross.png"))
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
    card2 = Image.open(str("assets/" + cardname))
    card2 = card2.resize((65,86))
    card2 = ImageTk.PhotoImage(card2)
    cardadd.photo = card2
    card = mastercanvas.create_image(50 + (165*int(playerposition)) + (25*(len(cardcounter[playerposition])+ 1)),200, image = card2)
    cardref[int(playerposition)].append(card)
    mastercanvas.update()
  

def endscore():
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
            scoreafterace = acedecision(playerscore, acecount)
            scorescounter.append(scoreafterace)
            
        else:
            scorescounter.append(playerscore)

    
    for i in range(0, playernum):
        if scorescounter[i] > 21:
            mastercanvas.create_text(150,(350 + (i * 20)),justify = "left",text=("Player "+str(i+1)+" went bust at "+str(scorescounter[i])+"."))
        else:
            mastercanvas.create_text(150,(350 + (i * 20)),justify = "left",text=("Player "+str(i+1)+" finishes with a score of "+str(int(scorescounter[i]))+"."))
            mastercanvas.update()
            time.sleep(0.1)
    finallist = []
    for x in scorescounter:
        if x > 21:
            finallist.append(0)
        else:
            finallist.append(x)
            
            
    winningplayer = max(finallist)
    playerpos = finallist.index(winningplayer)
    if finallist.count(winningplayer) > 1:
        tielist = [i for i,j in enumerate(finallist) if j == winningplayer]
        tietext = str()
        num = 0
        for i in tielist:
            if num == 0:
                tietext += (str(i+1))
                num += 1
            else:
                tietext += str(", " + str(i+1))
        mastercanvas.create_text(150,(350 + (playernum* 25)),text=("Player "+ tietext+" have tied at "+str(int(max(finallist)))+"."))
        for i in tielist:
            winnericon = tk.Label(masterwindow)
            banner = Image.open(str("assets/winner.png"))
            banner = banner.resize((120,120))
            banner = ImageTk.PhotoImage(banner)
            winnericon.photo = banner
            winnerpic = mastercanvas.create_image(65 + (165*int(i) + 12.5*(len(cardcounter[i])) - 1) ,285, image = banner)
            mastercanvas.update()
        
    else:
        print(playerposition)
        mastercanvas.create_text(150,(350 + (playernum* 25)),justify = "left",text=("Player "+ str(int(playerpos+1))+" WINS with a score of "+str(int(winningplayer))))
        winnericon = tk.Label(masterwindow)
        banner = Image.open(str("assets/winner.png"))
        banner = banner.resize((120,120))
        banner = ImageTk.PhotoImage(banner)
        winnericon.photo = banner
        winnerpic = mastercanvas.create_image(65 + (165*int(playerpos)) + 12.5*(len(cardcounter[playerpos]) - 1) ,285, image = banner)
        mastercanvas.update()
       

def acedecision(playerscore, acecount):
    if playerscore + (11 * acecount) <= 21:
        print("choice 1")
        return playerscore + (11 * acecount)

    elif playerscore + (11 * ((abs(acecount- 1) + acecount-1)/2)) + 1*1  <= 21:
        print("choice 2")
        return playerscore + (11 * ((abs(acecount- 1) + acecount-1)/2)) + 1*1

    elif playerscore + (11 * ((abs(acecount- 2) + acecount-2)/2)) + 1*2 <= 21:
        print("choice 3")
        return playerscore + (11 * ((abs(acecount- 2) + acecount-2)/2)) + 1*2

    elif playerscore + (11 * ((abs(acecount- 3) + acecount-3)/2)) + 1*3 <= 21:
        print("choice 4")
        return playerscore + (11 * ((abs(acecount- 4) + acecount-3)/2)) + 1*3

    else:
        print("choice 5")
        return playerscore + (1 * acecount)
                
setup()
gameround()
















    
   





            






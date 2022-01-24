import tkinter as tk
from tkinter import ttk
import win32print, win32api
#======================

orderNumber = 0

#======================
def confButtonPress() :
    global orderNumber
    
    choice = radChoiceVal.get()-1
    total = products[choice]["Price"]
    extra = 0
    orderNumber += 1
    
    print ('Pedido Finalizado'.center(30, "=") + "\n")
    print (f"Pedido N° {orderNumber}".center(30, "=") + "\n")
    print (products[choice]["Name"].center(30) + "\n")
    
    if radChoiceVal.get() in (1, 2, 3): #Acai
        print ("Acompanhamentos: ") #Reads and prints out all the chosen optional items
        
        for i in optFree : #Analizes each item, checking if it's marked 
            if i[1].get() == 1 :
                print (i[0])
                extra += 1
        
        if extra > 3 : #If more than 3 items are added, adds R$1,00, for each extra item, to the total
            total += (extra-3)
        
        for i in optEsp : #If an item from the special list is chosen, adds R$2,00 
            if i[1].get() == 1 :
                print (i[0])
                total += 2

        for i in optPremium : #If an item from the premium list is chosen, adds R$4,00
            if i[1].get() == 1 :
                print (i[0])
                total += 4

    elif radChoiceVal.get() in (4, 5) : #Milkshake
        print (f"Sabor: {shakeFlavors[shakeChosen.get()]}")
        print (f"Cobertura: {toppingFlavors[toppingChosen.get()]}")
        if boozeOpts[boozeChosen.get()] != "Nenhum" :
            print (f"Álcool: {boozeOpts[boozeChosen.get()]}")
            total += 5
        
    else :
        print ("NENHUM PRODUTO SELECIONADO") #None selected
        total = 0
    
    if total > 0 :
        print ("\n" +"-"*30)
        print (f"Pedido N° {orderNumber}".center(30, "="))
        print (products[choice]["Name"].center(30))
        print (f"Preço final: R${total:.2f}")
        print ("\n" +"-"*30)

#=========================================================================

window = tk.Tk() #Main Window
window.title("Pedidos")
radChoiceVal = tk.IntVar() #Stores the code referent to the chosen product

#=========================================================================

products = [
    {"Name" : "Açaí 330ml", "Price" : 12.00},
    {"Name" : "Açaí 440ml", "Price" : 15.00},
    {"Name" : "Açaí 550ml", "Price" : 18.00},
    {"Name" : "Milkshake 440ml", "Price" : 9.00},
    {"Name" : "Milkshake 550ml", "Price" : 10.00}]

#==========================================================================

#Frames division
acaiFrame = ttk.LabelFrame(window, text="Açaí")
acaiFrame.grid(column=0, row=0, sticky=tk.W)

shakeFrame = ttk.LabelFrame(window, text="Milkshake")
shakeFrame.grid(column=0, row=1, sticky=tk.W)

choicesFrame = ttk.LabelFrame(window)
choicesFrame.grid(column=0, row=2, sticky=tk.W)

acaiFreeOptFrame = ttk.LabelFrame(choicesFrame, text="Opcionais Gratuitos (Até 3)")

acaiEspOptFrame = ttk.LabelFrame(choicesFrame, text="Opcionais Extras (R$2,00)")

acaiPremiumOptFrame = ttk.LabelFrame(choicesFrame, text="Opcs Premium (R$4,00)")

shakeFlavorsFrame = ttk.LabelFrame(choicesFrame, text="Sabor do milkshake")

shakeToppingFrame = ttk.LabelFrame(choicesFrame, text="Sabor da cobertura")

shakeBoozeFrame = ttk.LabelFrame(choicesFrame, text="Bebida Alcoólica")

def menuChanger() : #Toggles the display between acai/milkshake related options
    choice = radChoiceVal.get()
    if choice in (4, 5) :
        shakeFlavorsFrame.grid(column=0, row=0, sticky="NW")        
        shakeToppingFrame.grid(column=1, row=0, sticky="NW")
        shakeBoozeFrame.grid(column=0, row=1, columnspan=2, sticky='NW')
        acaiPremiumOptFrame.grid_remove()
        acaiFreeOptFrame.grid_remove()
        acaiEspOptFrame.grid_remove()
    else :
        acaiPremiumOptFrame.grid(column=1, row=1, sticky="NW")
        acaiFreeOptFrame.grid(column=0, row=0, rowspan=2, sticky="NW")
        acaiEspOptFrame.grid(column=1, row=0, sticky="NW")
        shakeFlavorsFrame.grid_remove()
        shakeToppingFrame.grid_remove()
        shakeBoozeFrame.grid_remove()

#======================
#Acai Header selector
#Acai 330
ttk.Radiobutton(
    acaiFrame, 
    text="Açaí 330ml", 
    variable=radChoiceVal, 
    value=1,
    command=menuChanger
    ).grid(column=0, row=0, sticky=tk.W)

#Acai 440
ttk.Radiobutton(
    acaiFrame, 
    text="Açaí 440ml", 
    variable=radChoiceVal, 
    value=2,
    command=menuChanger
    ).grid(column=1, row=0, sticky=tk.W)

#Acai 550
ttk.Radiobutton(
    acaiFrame, 
    text="Açaí 550ml", 
    variable=radChoiceVal, 
    value=3,
    command=menuChanger
    ).grid(column=2, row=0, sticky=tk.W)

#Milkshake header selector
#Shake 440
ttk.Radiobutton(
    shakeFrame,
    text="Milkshake 440ml",
    variable=radChoiceVal,
    value=4,
    command=menuChanger
    ).grid(column=0, row=0, sticky=tk.W)

#Shake 550
ttk.Radiobutton(
    shakeFrame,
    text="Milkshake 550ml",
    variable=radChoiceVal,
    value=5,
    command=menuChanger
    ).grid(column=1, row=0, sticky=tk.W)

#=======================================
#Acai

optFree = [
    ["Leite condensado", tk.IntVar()],
    ["Leite em pó", tk.IntVar()],
    ["Granola", tk.IntVar()],
    ["Confeti", tk.IntVar()],
    ["Morango", tk.IntVar()],
    ["Paçoca", tk.IntVar()], 
    ["Banana", tk.IntVar()],
    ["Oreo", tk.IntVar()],
    ["Mel", tk.IntVar()]
]

optEsp = [
    ["Stikadinho", tk.IntVar()],
    ["Bis preto", tk.IntVar()],
    ["Abacaxi", tk.IntVar()],
    ["Manga", tk.IntVar()],
    ["Kiwi", tk.IntVar()]
]

optPremium = [
    ["Nutella", tk.IntVar()],
    ["KitKat", tk.IntVar()]
]

#Create a checkbox for each acai free optional item
for i in range (len(optFree)) :
    box = tk.Checkbutton(
        acaiFreeOptFrame,
        text=optFree[i][0],
        variable=optFree[i][1])
    box.grid(column=0, row=i, sticky=tk.W)

#Create a checkbox for each acai special optional item
for i in range (len(optEsp)) :
    box = tk.Checkbutton(
        acaiEspOptFrame,
        text=optEsp[i][0],
        variable=optEsp[i][1])
    box.grid(column=0, row=i, sticky=tk.W)
    
#Create a checkbox for each acai premium optional item
for i in range (len(optPremium)) :
    box = tk.Checkbutton(
        acaiPremiumOptFrame,
        text=optPremium[i][0],
        variable=optPremium[i][1])
    box.grid(column=0, row=i, sticky=tk.W)

#=========================================
#Milkshakes
shakeFlavors = [
    "Creme", "Morango",
    "Chiclete", "Flocos",
    "Chocolate","Chocomenta"]

shakeChosen = tk.IntVar() #Shake flavor number

#Create a radio button for each milkshake flavor
for i in range (len(shakeFlavors)) :
    radFlavor = ttk.Radiobutton(
        shakeFlavorsFrame, 
        text=shakeFlavors[i], 
        variable=shakeChosen, 
        value=i)
    radFlavor.grid(column=0, row=i, sticky=tk.W)


toppingFlavors = [
    "Nenhuma", "Caramelo",
    "Chocolate", "Morango"]

toppingChosen = tk.IntVar() #Topping flavor index

#Create a radio button for each shake topping flavor
for i in range (len(toppingFlavors)) :
    radTopp = ttk.Radiobutton(
        shakeToppingFrame, 
        text = toppingFlavors[i],
        variable = toppingChosen,
        value = i)
    radTopp.grid(column=0, row=i, sticky=tk.W)
    

#Alcoholic milkshake
boozeOpts = [
    "Nenhum", "Gin",
    "Vodka", "Whisky"]

boozeChosen = tk.IntVar() #Chosen booze index

#Create a radio button for each alcoholic option
for i in range (len(boozeOpts)) :
    radBooze = ttk.Radiobutton(
        shakeBoozeFrame,
        text = boozeOpts[i],
        variable = boozeChosen,
        value = i)
    radBooze.grid(column=i, row=0, sticky=tk.W)

#=======================================
#Bottom display:

confButton = ttk.Button(
    window,
    text="Confirmar pedido",
    command=confButtonPress)
confButton.grid(column=0, row=3)

#======================
window.mainloop() #Runs the GUI
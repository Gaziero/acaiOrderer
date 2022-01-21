import tkinter as tk
from tkinter import ttk
#======================
def radTest() :
    #print(radChoiceVal.get())
    print("")

def confButtonPress() :
    total = products[radChoiceVal.get()-1]["Price"]
    extra = 0
    
    print('Pedido Finalizado')
    print (products[radChoiceVal.get()-1]["Name"])
    if radChoiceVal.get() in (1, 2, 3):
        print ("Acompanhamentos: ")
        for i in opcFree :
            if i[1].get() == 1 :
                print (i[0])
                extra += 1
        if extra > 3 :
            total += (extra-3)
    elif radChoiceVal.get() in (4, 5) :
        print (f"Sabor: {shakeFlavors[shakeChosen.get()]}")
        print (f"Cobertura: {toppingFlavors[toppingChosen.get()]}")
        
    else :
        print ("NENHUM PRODUTO SELECIONADO")
        total = 0
    
    print (f"Preço final: R${total:.2f}")
        

#======================
window = tk.Tk()
window.title("Pedidos")
radChoiceVal = tk.IntVar() #Stores the code referent to the chosen product

products = [
    {"Name" : "Açaí 330ml", "Price" : 12.00},
    {"Name" : "Açaí 440ml", "Price" : 15.00},
    {"Name" : "Açaí 550ml", "Price" : 18.00},
    {"Name" : "Milkshake 440ml", "Price" : 9.00},
    {"Name" : "Milkshake 550ml", "Price" : 10.00}
]
#======================
#Frames division
acaiFrame = ttk.LabelFrame(window, text="Açaí")
acaiFrame.grid(column=0, row=0, sticky=tk.W)

shakeFrame = ttk.LabelFrame(window, text="Milkshake")
shakeFrame.grid(column=0, row=1, sticky=tk.W)

choicesFrame = ttk.LabelFrame(window)
choicesFrame.grid(column=0, row=2, sticky=tk.W)

acaiFreeOptFrame = ttk.LabelFrame(choicesFrame, text="Opcionais Gratuitos (Até 3)")
acaiFreeOptFrame.grid(column=0, row=0, rowspan=2, sticky=tk.W)

shakeFlavorsFrame = ttk.LabelFrame(choicesFrame, text="Sabor do milkshake")
shakeFlavorsFrame.grid(column=1, row=0, sticky=tk.N)

shakeToppingFrame = ttk.LabelFrame(choicesFrame, text="Sabor da cobertura")
shakeToppingFrame.grid(column=1, row=1, sticky=tk.N)

bottomFrame = ttk.LabelFrame(window, text="Preço R$")
bottomFrame.grid(column=0, row=3, sticky=tk.W)
#======================
#Acai Header selector
#Acai 330
ttk.Radiobutton(
    acaiFrame, 
    text="Açaí 330ml", 
    variable=radChoiceVal, 
    value=1,
    command=radTest
    ).grid(column=0, row=0, sticky=tk.W)

#Acai 440
ttk.Radiobutton(
    acaiFrame, 
    text="Açaí 440ml", 
    variable=radChoiceVal, 
    value=2,
    command=radTest
    ).grid(column=1, row=0, sticky=tk.W)

#Acai 550
ttk.Radiobutton(
    acaiFrame, 
    text="Açaí 550ml", 
    variable=radChoiceVal, 
    value=3,
    command=radTest
    ).grid(column=2, row=0, sticky=tk.W)

#Milkshake header selector
#Shake 440
ttk.Radiobutton(
    shakeFrame,
    text="Milkshake 440ml",
    variable=radChoiceVal,
    value=4,
    command=radTest
    ).grid(column=0, row=0, sticky=tk.W)

#Shake 550
ttk.Radiobutton(
    shakeFrame,
    text="Milkshake 550ml",
    variable=radChoiceVal,
    value=5,
    command=radTest
    ).grid(column=1, row=0, sticky=tk.W)

#=======================================
#Acai
opcFree = [
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

chosenOpcs = []
#Create a checkbox for each acai free optional item
for i in range (len(opcFree)) :
    box = tk.Checkbutton(acaiFreeOptFrame, text=opcFree[i][0], variable=opcFree[i][1])
    box.grid(column=0, row=i, sticky=tk.W)
    
#=========================================
#Milkshakes
shakeFlavors = [
    "Creme", "Morango", "Chocomenta",
    "Chocolate", "Chiclete", "Flocos"]

shakeChosen = tk.IntVar() #Shake flavor number

#Create a radio button for each milkshake flavor
for i in range (len(shakeFlavors)) :
    radFlavor = ttk.Radiobutton(
        shakeFlavorsFrame, 
        text=shakeFlavors[i], 
        variable=shakeChosen, 
        value=i)
    radFlavor.grid(column=0, row=i, sticky=tk.W)


toppingFlavors = ["Nenhuma", "Caramelo", "Chocolate", "Morango"]

toppingChosen = tk.IntVar() #Topping flavor index

#Create a radio button for each shake topping flavor
for i in range (len(toppingFlavors)) :
    radTopp = ttk.Radiobutton(
        shakeToppingFrame, 
        text = toppingFlavors[i],
        variable=toppingChosen,
        value=i)
    radTopp.grid(column=0, row=i, sticky=tk.W)

#=======================================
#Bottom display:
ttk.Label(bottomFrame, text="00,00").grid(column=0, row=0)

confirm = 0

confButton = ttk.Button(bottomFrame, text="Finalizar", command=confButtonPress)
confButton.grid(column=1, row=0)
#======================
window.mainloop() #Runs the GUI

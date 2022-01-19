import tkinter as tk
from tkinter import Variable, ttk
#======================
def radTest():
    radNum = radChoiceVal.get()
    print(radNum)

#======================
window = tk.Tk()
window.title("Pedidos")
#======================
#Frames division
acaiFrame = ttk.LabelFrame(window, text="Açaí")
acaiFrame.grid(column=0, row=0, sticky=tk.W)

shakeFrame = ttk.LabelFrame(window, text="Milkshake")
shakeFrame.grid(column=0, row=1, sticky=tk.W)

bottomFrame = ttk.LabelFrame(window, text="Preço R$")
bottomFrame.grid(column=0, row=3, sticky=tk.W)
#======================
radChoiceVal = tk.IntVar()
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
#Bottom display:
ttk.Label(bottomFrame, text="00,00").grid(column=0, row=0)

confirm = 0
def confButtonPress() :
    confirm = 1
    print(confirm)
    return confirm

confButton = ttk.Button(bottomFrame, text="Finalizar", command=confButtonPress)
confButton.grid(column=1, row=0)

confirm = confButtonPress()
print (confirm)
#======================
if confirm == 1:
    print ("Exiting")
window.mainloop() #Runs the GUI

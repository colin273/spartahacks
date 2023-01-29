from tkinter import *
from colorchang import *
currentcolor = ""

class colorLens(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        self.pack(fill=BOTH, expand=1)

        exitButton = Button(self, text="Exit", command=self.clickExitButton, height=1, width=9)
        grayScale = Button(self, text="Gray Scale", command=self.clickGrayScaleFilter, height=1, width=9, bg="#808080")
        inverse = Button(self, text="Inverse", command=self.clickInverseFilter, height=1, width=9, bg="#00FFFF")
        sepia = Button(self, text="Sepia", command=self.clickSepiaFilter, height=1, width=9, bg="#704214")
        protan = Button(self, text="Protan", command=self.clickProtanFilter,height=1, width=9, bg="#bdd9bf")
        tritan = Button(self, text="Tritan", command=self.clickTritanFilter,height=1, width=9, bg="#CBC3E3")
        deuter = Button(self, text="Deuter", command=self.clickDeuterFilter,height=1, width=9, bg="#195d26")

        exitButton.place(x=25, y=10)
        grayScale.place(x=25, y=40)
        inverse.place(x=25, y=70)
        sepia.place(x=25, y=100)
        protan.place(x=25, y=130)
        tritan.place(x=25, y=160)
        deuter.place(x=25, y=190)

    ##big code smell
        
    def clickExitButton(self):
        currentcolor = resetcolor()
        exit()

    def clickGrayScaleFilter(self):
        color = "Grayscale"
        global currentcolor
        print(color, currentcolor)
        if(color != currentcolor):
            currentcolor = setcolor(color)
        else:
            currentcolor = returncolor(color)
            
    def clickInverseFilter(self):
        color = "Inversion"
        global currentcolor
        print(color, currentcolor)
        if(color != currentcolor):
            currentcolor = setcolor(color)
        else:
            currentcolor = returncolor(color)
    

    def clickSepiaFilter(self):
        color = "Sepia"
        global currentcolor
        print(color, currentcolor)
        if(color != currentcolor):
            currentcolor = setcolor(color)
        else:
            currentcolor = returncolor(color)
    

    def clickProtanFilter(self):
        color = "Protanopia"
        global currentcolor
        print(color, currentcolor)
        if(color != currentcolor):
            currentcolor = setcolor(color)
        else:
            currentcolor = returncolor(color)
    

    def clickTritanFilter(self):
        color = "Tritanopia"
        global currentcolor
        print(color, currentcolor)
        if(color != currentcolor):
            currentcolor = setcolor(color)
        else:
            currentcolor = returncolor(color)
    

    def clickDeuterFilter(self):
        color = "Deuteranopia"
        global currentcolor
        print(color, currentcolor)
        if(color != currentcolor):
            currentcolor = setcolor(color)
        else:
            currentcolor = returncolor(color)
    



gui = Tk()
app = colorLens(gui)
gui.wm_title("ColorLens")
gui.geometry("225x225")
gui.mainloop()

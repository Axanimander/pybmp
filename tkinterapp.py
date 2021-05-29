from tkinter import *
from tkinter import filedialog
from bmpreader import *


class app(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.bmpReader = None
        self.filename = ""
        root.mainloop()
    def create_widgets(self):
        self.quit = Button(self, text="Quit", fg="red",command=self.master.destroy)
        self.load = Button(self, text="Open BMP", fg="red", command=self.open_file) 
        self.load.pack(side="bottom")
        self.quit.pack(side="bottom")
        
    def open_file(self):
        self.filename = filedialog.askopenfilename(title = "Select BMP", filetypes=(("bmp files", "*.bmp"),("All files","*.*")))
        self.bmpReader = bmpReader(self.filename)
        self.savefile = Button(self, text="Save Pixels", fg="green", command=self.save_hex_data)
        self.savefile.pack(side="bottom")

    def save_hex_data(self):
        self.savefilename = filedialog.asksaveasfile(filetypes = [('text file', '*.txt')])
        print(self.savefilename)
        self.bmpReader.outputRawPixelData()
        strings = [str(n) for n in self.bmpReader.pixelArray]
        with open(self.savefilename.name, "w") as file:
            file.write(",".join(strings))
        

root = Tk()

z = app(root)

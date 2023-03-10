from tkinter import *
import random as rdm
class Main(Frame):
    def __init__(sef,root):
        super(Main, self).__init__(root)
        self.startUI()
    def startUI(self):
        pass
if __name__ == '__main__':
    root = Tk()
    root.geometry("500x500+200+200")
    root.title("Камень, ножницы, бумага")
    root.resizable(False, False)
    root["bg"] =  "#FF"
    app = Main(root)
    app.pack()
    root.mainLoop()


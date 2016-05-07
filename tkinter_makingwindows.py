from tkinter import *

from PIL import Image, ImageTk

class Window(Frame):

	def __init__(self, master = None):
		Frame.__init__(self, master)

		self.master = master

		self.init_window()

	def init_window(self):
		self.master.title('GUI')
		self.pack(fill=BOTH, expand=1)

		# quitButton = Button(self,text="Quit",command=self.clinet_exit)

		# quitButton.place(x=0, y=0)
        
        # define a menu
		menu = Menu(self.master)
		self.master.config(menu=menu)

        # create a file button
		file = Menu(menu)
		file.add_command(label = 'Exit', command=self.clinet_exit)
		file.add_command(label = 'Save')
		menu.add_cascade(label='File', menu=file)
        # create a edit button
		edit = Menu(menu)
		edit.add_command(label='Show Image', command=self.showImg)
		edit.add_command(label='Show Text', command=self.showTxt)
		menu.add_cascade(label='Edit', menu=edit)


	def clinet_exit(self):
		exit()

	def showImg(self):
		load = Image.open('Anne-Hathaway_1.jpg')
		render = ImageTk.PhotoImage(load)

		img = Label(self, image=render)
		img.image = render
		img.place(x=0,y=0)

	def showTxt(self):
		text = Label(self, text='Hey there good looking!')
		text.pack()

  

root = Tk()
root.geometry("400x300") #dimention of the window
app = Window(root)
root.mainloop()

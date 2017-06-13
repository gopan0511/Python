from Tkinter import *
c = 0
def bbsr():
	'''global c
	c+=1
	print 'Okay Pressed',c'''
	print 'Hello',name.get()

def ctc():
	print 'I am going to exit'
	#exit(0)
	win.destroy()

win = Tk()
l = Label(text = "Hello World")
l.pack()

name = Entry()
name.pack()

id = Entry()
id.pack()

b1 = Button(text = "Okay",command = bbsr)
b1.pack()

b2 = Button(text = 'Exit', command = ctc)
b2.pack()


win.mainloop()



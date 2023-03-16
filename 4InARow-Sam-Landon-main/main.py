#import
import turtle as t

wn=t.Screen()
# wn.screensize(1280, 720)
wn.setup(1280,720)
fontTitle=("Time New Roman",100,"normal")
fontPlay=("Time New Roman",50,"normal")
menu_image = "./mainMenu.gif"
wn.addshape(menu_image)
playBt = t.Turtle()
tourBt = t.Turtle()
hiddenBt = t.Turtle()
t.shape(menu_image)

def Clicked(x,y):
	global menu_image
	if menu_image=="./mainMenu.gif":#buttons for main menu
		if (x>-149.0 and x<130.0 and y>-166.0 and y<-68.0):
			menu_image="./playOpt.gif"
			wn.addshape(menu_image)
			t.shape(menu_image)
		if (x>-280.0 and x<263.0 and y>-316.0 and y<-220.0):
			menu_image="./directions.gif"
			wn.addshape(menu_image)
			t.shape(menu_image)

	if menu_image=="./playOpt.gif":#buttons for play options
		if (x>-118.0 and x<103.0 and y>-163.0 and y<-68.0):
			print("pvp")
		if (x>-116.0 and x<102.0 and y>-312.0 and y<-220.0):
			print("pvc")

	if (x>-611.0 and x<-452.0 and y>253.0 and y<311.0):
		menu_image="./mainMenu.gif"
		wn.addshape(menu_image)
		t.shape(menu_image)
	print(x,y)
wn.onscreenclick(Clicked)
    
# def Clicked(x,y):
#     print("bob was clicked")
#     print(x,y)
#     t.clear()
 
# # playBt.onclick(onClick)

# # hiddenBt.ht()
# hiddenBt.penup()
# hiddenBt.goto(20,10)
# hiddenBt.shape("square")
# hiddenBt.shapesize(5, 10, 12)
# # hiddenBt.right(270)
# # hiddenBt.fd(10)
# #playButton
# # playBt.pencolor("White")
# playBt.penup()
# playBt.ht()
# playBt.goto(-50,0)
# playBt.write("Play!",font=fontPlay)

# #dirButton
# tourBt.penup()
# tourBt.ht()
# tourBt.goto(-140,-150)
# tourBt.write("Directions!",font=fontPlay)


# hiddenBt.onclick(Clicked)
wn.mainloop()
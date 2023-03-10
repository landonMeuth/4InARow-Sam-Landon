#import
import turtle as t

wn=t.Screen()
# wn.screensize(1280, 720)
wn.setup(1280,720)
fontTitle=("Time New Roman",100,"normal")
fontPlay=("Time New Roman",50,"normal")
menu_image = "Mainu.png"
wn.addshape(menu_image)
bob = t.Turtle(shape=menu_image)
playBt = t.Turtle()
tourBt = t.Turtle()
hiddenBt = t.Turtle()

#title
bob.speed(0)
bob.penup()
# bob.ht()
bob.goto(-1280/5,150)
# bob.write("4 in A Row",font=fontTitle)


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
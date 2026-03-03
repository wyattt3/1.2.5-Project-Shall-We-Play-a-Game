from operator import index
import turtle as trtl
wn = trtl.Screen()
#create the game grid

wn.setup(width=1.0, height=1.0)
wn.bgpic("grid_resized.gif")
wn.bgcolor("cornflowerblue")

#provide instructions on the screen
instructions = trtl.Turtle()
instructions.hideturtle()
instructions.penup()
instructions.goto(-400, 400)
instructions.write("Press 'a' to move left, 'd' to move right, 's' to drop the coin, and 'w' to pick a spot", font=("Arial", 16, "normal"))

#create red and yellow coins
coin = trtl.Turtle()
colors = ["red", "yellow"]
coin.penup()
coin.goto(0,500)
coin.fillcolor(colors[0])
coin.shape("circle")
coin.shapesize(5)


#define the key functions
def left():
    coin.back(20)
    
def right():
    coin.forward(20)

def drop():
    if coin.ycor() > -330:
        coin.sety(coin.ycor() - 20)
    else: 
        coin.sety(-330)
    
    

colors = ["red", "yellow"]

def pickspot():
    coin.stamp()
    #make it reset and change color
    coin.hideturtle
    coin.goto(0,500)
    coin.showturtle
    colors.append(colors.pop(0))
    coin.fillcolor(colors[0])





#create the key bindings
wn.onkeypress(left,"a")
wn.onkeypress(right, "d")
wn.onkeypress(drop, "s")
wn.onkeypress(pickspot, "w")








wn.listen()
wn.mainloop()
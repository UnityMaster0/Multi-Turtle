import random as rndm
import turtle as trtl
import time

#Defines Turtle variable
t = trtl.Turtle()

#Controller function for drawSpiral()
def fullspiral():
  
  screen = trtl.Screen()
  screen.onclick(drawSpiral)

  wn = trtl.Screen()
  wn = trtl.mainloop()

def fullrandom():
  
  screen = trtl.Screen()
  screen.onclick(rmdrawing)

  wn = trtl.Screen()
  wn = trtl.mainloop()

#Draw spirals based on screen clicks
def drawSpiral(x, y):
  t.penup()
  t.goto(x, y)
  t.pendown()

#Ask for angle input after every click
  angle = trtl.numinput('Angle', 'What do you want the angle of the spiral to be?: ')
  
  p = 0

#Draw spiral for 100 interations
  while (p == 0):
    count = 1
    while count < 100:
      for multiColor in ['red','orange','yellow','green','blue','purple']:
        count += 1
        t.color(multiColor)
        t.forward(count)
        t.speed(count)
        t.right(angle)
    break

#Create variables x and y
def y_x_var(x, y):
  global var_x, var_y
  var_x = x
  var_y = y

#Controller function for rmdrawing()
def rndminput():
  global timerCount
  global start
  timerCount = trtl.numinput('Timer Set', 'How long do you want the program to run?: ')
  start = time.time()
  print('Running for', timerCount, 'seconds')
  
  
#Create psudo-random drawing for an inputed amount of seconds
def rmdrawing(x, y):

    t.penup()
    t.goto(x, y)
    t.pendown()

    i = 0

    while (i == 0):
      for multiColor in ['red','orange','yellow','green','blue','purple']:
        t.forward(rndm.randint(1, 100))
        t.right(rndm.randint(1, 360))
        t.speed(rndm.randint(1, 10))
        t.width(rndm.randint(1, 5))
        t.color(multiColor)

        end = time.time()
        print(end - start)

        if end - start >= timerCount:
            i = 1
            print('Drawing complete')
            wn = trtl.Screen()
            wn = trtl.mainloop()

#Draw a circle of inputed size
def drawCircle():
  size = trtl.numinput('Set Circle Size', 'What do you want the size of the circle to be?: ')
  
  t.circle(size)

  wn = trtl.Screen()
  wn = trtl.mainloop()

#Input to select random, spiral, or circle
setting = trtl.textinput('Mode Select','Do you want to draw random, spiral, or circle (r or s or c)?: ')

if setting == 'r' or setting == 'random' or setting == 'Random':
  rndminput()
  fullrandom()

if setting == "s" or setting == 'spiral' or setting == 'Spiral':
  fullspiral()

if setting == "c" or setting == 'circle' or setting == 'Circle':
  drawCircle()

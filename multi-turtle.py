import random as rndm
import turtle as trtl
import time


def rmdrawing():

    t = trtl.Turtle()

    timerCount = trtl.numinput('Timer Set', 'How long do you want the program to run?: ')
    print('Running for', timerCount, 'seconds')

    i = 0

    start = time.time()

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


def fullspiral():

    angle = trtl.numinput('Angle', 'What do you want the angle of the spiral to be?: ')

    t = trtl.Turtle()

    def drawCircle(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

        p = 0

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

    def goto_var(x, y):
      global var_x, var_y
      var_x = x
      var_y = y

    t.penup()
    screen = trtl.Screen()
    screen.onclick(drawCircle)

    wn = trtl.Screen()
    wn = trtl.mainloop()


setting = trtl.textinput('Mode Select','Do you want to draw random or spiral (r or s)?: ')

if setting == 'r':
    rmdrawing()

if setting == "s":
    fullspiral()

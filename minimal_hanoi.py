#!/usr/bin/env python3

# original by turtledemo in Python 3.9

# 11/30/2021 added changing numbers of discs
# by micnanzel@gmail.com

"""       turtle-example-suite:

         tdemo_minimal_hanoi.py

A minimal 'Towers of Hanoi' animation:
A tower of 6 discs is transferred from the
left to the right peg.

An imho quite elegant and concise
implementation using a tower class, which
is derived from the built-in type list.

Discs are turtles with shape "square", but
stretched to rectangles by shapesize()
 ---------------------------------------
       To exit press STOP button
 ---------------------------------------
"""

import turtle
from turtle import *

class Disc(Turtle):
    def __init__(self, n, nmax):
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(1.5, n*1.5, 2) # square-->rectangle
        self.fillcolor(1.*n/nmax, 0, 1-1.*n/nmax)
        self.st()

class Tower(list):
    "Hanoi tower, a subclass of built-in type list"
    def __init__(self, x):
        "create an empty tower. x is x-position of peg"
        self.x = x
    def push(self, d):
        d.setx(self.x)
        d.sety(-150+34*len(self))
        self.append(d)
    def pop(self):
        d = list.pop(self)
        d.sety(150)
        return d

def hanoi(n, from_, with_, to_):
    if n > 0:
        hanoi(n-1, from_, to_, with_)
        to_.push(from_.pop())
        hanoi(n-1, with_, from_, to_)

def play():
    onkey(None,"space")
    clear()
    try:
        hanoi(diskSum, t1, t2, t3)
        write("press STOP button to exit",
              align="center", font=("Courier", 16, "bold"))
    except Terminator:
        pass  # turtledemo user pressed STOP

def main():
    #diskSum = int(input('Enter number of disks: ')
    global t1, t2, t3, diskSum
    ht(); penup(); goto(0, -225)   # writer turtle


    # diskSum = int(turtle.textinput("Hanoi Towers", "Enter num of disks"))
    
    while True: # window with number of discs choice
        try:
            diskSum = int(turtle.textinput("Hanoi Towers", "Enter num of disks"))
            if diskSum > 0:
                break
            else:
                print('Equal or less then 0')
        except :
            print('Not number')
        
    # make tower of 6 discs
    t1 = Tower(-250 - diskSum*30)
    t2 = Tower(0)
    t3 = Tower(250 + diskSum*30)

    for i in range(diskSum,0,-1):
        t1.push(Disc(i, diskSum))

    # prepare spartanic user interface ;-)
    write("press spacebar to start game",
          align="center", font=("Courier", 16, "bold"))
    onkey(play, "space")
    listen()
    return "EVENTLOOP"

if __name__=="__main__":
    msg = main()
    print(msg)
    mainloop()

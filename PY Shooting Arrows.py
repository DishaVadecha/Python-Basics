import turtle
import random
import math
import time

def drawCircle(pen, colorFill, size, x, y):
  pen.penup()
  pen.color(colorFill)
  pen.fillcolor(colorFill)
  pen.goto(x,y)
  pen.begin_fill()
  pen.circle(size)
  pen.end_fill()
  pen.pendown()
    
def drawTarget(pen):
  drawCircle(pen, "#000000", 152, 0,-152)
  drawCircle(pen, "#FFFFFF", 150, 0,-150)
  drawCircle(pen, "#000000", 120, 0,-120)
  drawCircle(pen, "#33AAFF", 90, 0,-90)
  drawCircle(pen, "#FF0000", 60, 0,-60)
  drawCircle(pen, "#FFFF00", 30, 0,-30)

def drawCross(pen, color, size, x, y):
  pen.pensize(3)
  pen.color(color)
  pen.penup()
  pen.goto(x-size,y-size)
  pen.pendown()
  pen.goto(x+size,y+size)
  pen.penup()
  pen.goto(x-size,y+size)
  pen.pendown()
  pen.goto(x+size,y-size)

def writeScore(pen, text):
  pen.penup()
  pen.goto(-65, 190)
  pen.color("#000000")
  pen.write(text)
  time.sleep(1)
  pen.undo()

def calculateScore(arrowx,arrowy,totalscore):
  score = 0
  distance = 0
  distance = math.sqrt((arrowx - 0)**2 + (arrowy - 0)**2)

  if distance >= 0 and distance <= 30:
    score = 10
  elif distance >= 31 and distance <= 60:
    score = 5
  elif distance >= 61 and distance <= 90:
    score = 3
  elif distance >= 91 and distance <= 120:
    score = 2
  elif distance >= 121 and distance <= 150:
    score = 1
  elif distance >= 151:
    score = 0

  totalscore = totalscore + score
  return score,totalscore



myPen = turtle.Turtle()
turtle.tracer(0)
myPen.speed(1)
myPen.shape("arrow")
drawTarget(myPen)

totalscore=0
score=[0,0]

#Shooting the arrow 
while True:
  arrowx= random.randint(-118,118)
  arrowy= random.randint(-118,118)
  time.sleep(5)
  drawCross(myPen,"#FF7777",10,arrowx,arrowy)

#Calculate and display score
  score = calculateScore(arrowx,arrowy,score[1])
  writeScore(myPen,"Your Score: + " + str(score[0]) + "\n\nYour Total Score: + " + str(score[1]))

#Hide the pen
  myPen.penup()
  myPen.goto(-300,-300)


from turtle import Turtle
import random
def cCurve(t, x1, y1, x2, y2, level):
   
   def drawLine(x1, y1, x2, y2):
      """Draws a line segment between the endpoints,
      using a random color."""
      t.pencolor(random.randint(0, 255),
                 random.randint(0, 255),
                 random.randint(0, 255))
      t.up()
      t.goto(x1, y1)
      t.down()
      t.goto(x2, y2)
      
   if level == 0:
      drawLine(x1, y1, x2, y2)
   else:
      xm = (x1 + x2 + y1 - y2) // 2
      ym = (x2 + y1 + y2 - x1) // 2
      cCurve(t, x1, y1, xm, ym, level - 1)
      cCurve(t, xm, ym, x2, y2, level - 1)
def main():
   level = int(input("Enter the level (0 or greater): "))
   t = Turtle()
   t.hideturtle()
   cCurve(t, 50, -5, 50, 50, level)
if __name__ == "__main__":
   main()

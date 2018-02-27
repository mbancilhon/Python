# fractalTree.py
# Melanie Bancilhon
#
# Draws a fractal tree on the graphic window.
#
from graphics import *
import math
import time
import random

# dimensions of the window
MAXWIDTH = 800
MAXHEIGHT = 800

   
# recursive tree-drawing function
# 
def draw_tree(win   ,       # the canvas
              order,        # the level of recursion.  Starts positive.
              theta,        # angle of new branch leaving this trunk
              sz,           # size of this branch
              x, y,         # coordinates of base of this branch
              heading,      # angle of direction of this branch
              color,        # color
              width):       # width

   trunk_ratio = 0.49       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk

   # compute x, y of end of the current branch
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   x2, y2 = x + delta_x, y + delta_y

   
   # draw current branch
   branch = Line( Point( x, y), Point( x2, y2 ) )
   branch.setFill( color )
   branch.setWidth( width )
   branch.setOutline( color )
   branch.draw( win )


   # if this branch has sub-branches, then recurse
   if order > 0:
       #if order is greater than 1, that is, not last branch
       if order>1:
           # make the recursive calls to draw the two subtrees
           newsz = sz*(1 - trunk_ratio)
           draw_tree(win,
                    order-1, theta, newsz, x2, y2, heading-theta,
                    "red",width-2 )
           draw_tree(win,
                    order-1, theta, newsz, x2, y2, heading+theta,
                    "blue", width-2 )
       #if order is 1, that is last branch
       elif order==1:
           # make the recursive calls to draw the two subtrees
           newsz = sz*(1 - trunk_ratio)
           draw_tree(win,
                    order-1, theta, newsz, x2, y2, heading-theta,
                    "red",width-2 )
           draw_tree(win,
                    order-1, theta, newsz, x2, y2, heading+theta,
                    "blue", width-2 )
           #draw the leaves
           circle= Circle(Point(x2,y2), 10)
           circle.setFill("light green")
           circle.draw(win)
           
   #width starts at 19 and decreases by 2 for each order, starting at order 9
   #oranges need to be drawn on the second to last branch
   #which has width 13
   if width== 13:
              circle= Circle(Point(x2,y2), 20)
              circle.setFill("orange")
              circle.draw(win)      

# draw 1 tree in the middle of the screen, shooting straight up.
def main():
    win = GraphWin("Melanie Bancilhon", MAXWIDTH, MAXHEIGHT )
    theta = 0.65      # use 0.02 for tall skinny trees, 0.7 for fat trees
    width=19          #initial width
    draw_tree(win,
              9,
              theta,
              MAXWIDTH*0.9, MAXWIDTH//2,
              MAXHEIGHT-50,
              -math.pi/2,
              "brown",width)
        
    win.getMouse()
    win.close()

main()
	 	  	    	    	 		      	   	 	

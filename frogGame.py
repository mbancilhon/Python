#final exam problem 3
#Melanie Bancilhon

#Having one object moving on the screen from left to right
#and coming through left again when it's out of window (cars)
#Having a second row of the same object, this time coming from right
#to left and coming again when it's out of the window (cars)
#Another object going up and down when clicking on button (frog)
#Make frog go back to initial position and change banner
#when it hits a car
#Or when it crosses the road


from graphics import *
from random import *

HEIGHT=600
WIDTH=600

initialLives=3
initialCrossing=0 

class Banner:
    def __init__( self, message ):
        """constructor.  Creates a message at the top of the graphics window"""
        self.text = Text( Point( WIDTH//2, 20 ), message )
        self.text.setFill( "black" )
        self.text.setTextColor( "black" )
        self.text.setSize( 20 )
        
    def draw( self, win ):
        """draws the text of the banner on the graphics window"""
        self.text.draw( win )
        self.win = win
        
    def setText( self, message ):
        """change the text of the banner."""
        self.text.setText( message )
       
class Car:
    def __init__( self, refPoint):
        x1 = refPoint.getX()
        y1 = refPoint.getY()
        x2 = x1 + 90
        y2 = y1 + 30
        
        self.body= Rectangle ( Point(x1,y1), Point(x2,y2)  )
        
        # create wheels
        self.w1 = Wheel( Point(x1+20, y1+30), 10)
        self.w2 = Wheel( Point(x1+70, y1+30), 10)


    def draw( self, win ):                   
        self.body.draw( win )
        self.w1.draw( win )
        self.w2.draw( win )


class Wheel:
    def __init__( self, center, radius ):
        self.c1 = Circle( center, radius)
        self.c2 = Circle( center, radius/2 )
        self.c1.setFill( "black" )
        self.c2.setFill( "white" )

    def draw( self, win ):
        self.c1.draw( win )
        self.c2.draw( win )

    
    def move(self,dx,dy):
        self.c1.move(dx,dy )
        self.c2.move(dx,dy)
        
#create derived class from class car
class OperateCar( Car ):
    def setColor(self,color):
        self.body.setFill(color)

    def move(self,dx,dy):
        self.body.move(dx,dy )
        self.w1.move(dx,dy)
        self.w2.move(dx,dy)

        xcoord=self.body.getCenter().getX()
        ycoord=self.body.getCenter().getY()
        #if cars from first row got out of window
        #move them so that they re appear to the other side
        if dx>0 and xcoord > WIDTH :
            self.body.move(-WIDTH-10,0)
            self.w1.move(-WIDTH-10,0)
            self.w2.move(-WIDTH-10,0)
        #if cars from second row got out of window
        #move them so that they re appear to the other side
        if dx<0 and xcoord < 0:
            self.body.move(WIDTH+10,0)
            self.w1.move(WIDTH+10,0)
            self.w2.move(WIDTH+10,0)
            
    def accident(self,win, frogx,frogy):
        global initialLives
        xcoord=self.body.getCenter().getX()
        ycoord=self.body.getCenter().getY()
        #if car and froggy intersect
        #move frog
        #update lives left
        if (abs(xcoord-frogx)<=45) and (abs(ycoord-frogy)<=25):           
            moveFrog(win, frog, (545- frogy))
            initialLives=initialLives-1
            return(initialLives)

    def accident2(self,win, frogx,frogy):
        global initialLives
        xcoord=self.body.getCenter().getX()
        ycoord=self.body.getCenter().getY()
        #if car and froggy intersect
        #move frog
        #update lives left
        if (abs(xcoord-frogx)<=45) and (abs(ycoord-frogy)<=25):
            moveFrog(win, frog, (545- frogy))
            initialLives=initialLives-1
            return(initialLives)
            
        
def moveFrog(win,frog,dy):
    frog.move(0,dy)
    
def main():
    global WIDTH, HEIGHT, frog, initialLives,initialCrossing
    

    #Create graphics window
    win= GraphWin("Final 3", HEIGHT, WIDTH)

    #draw lower road
    road1= Rectangle(Point(0,180), Point(WIDTH, 190))
    road1.setFill("grey")
    road1.setOutline("black")
    road1.draw(win)

    #draw upper road
    road2= Rectangle(Point(0,480), Point(WIDTH, 490))
    road2.setFill("grey")
    road2.setOutline("black")
    road2.draw(win)

    #draw line in between two roads
    line= Line( Point(0,330),Point(WIDTH, 330))
    line.setWidth(5)
    line.setFill("grey")
    line.draw(win)
    
    #Draw cars of first lane:
    #call OperateCar class derived from super class car      
    #pass the color as a parameter
    #draw the car 
    car= OperateCar(Point(0,200))
    car.setColor("blue")
    car.draw(win)
    
    car2=OperateCar(Point(200,200))
    car2.setColor("red")
    car2.draw(win)
    
    car3=OperateCar(Point(400,200))
    car3.setColor("black")
    car3.draw(win)

    #Draw cars of second lane:
    #call OperateCar class derived from super class car      
    #pass the color as a parameter
    #draw the car
    carb= OperateCar(Point(0,400))
    carb.setColor("blue")
    carb.draw(win)
    
    carb2=OperateCar(Point(200,400))
    carb2.setColor("red")
    carb2.draw(win)
    
    carb3=OperateCar(Point(400,400))
    carb3.setColor("black")
    carb3.draw(win)

    #draw the froggy
    frog= Image(Point(300,545), "Frog3.gif")
    frog.draw(win)

    #draw initial banner      
    banner = Banner("{0:1} life point(s) left,{1:1} crossing(s)".format(initialLives,initialCrossing))
    banner.draw( win )

    #make cars and frog move  
    while True:

        #get the point where the user clicks
        clickedPoint=win.checkMouse()
             
        #if user did not click on window
        if clickedPoint==None:
            #make cars move
            car.move(7,0)
            car2.move(7,0)
            car3.move(7,0)
            carb.move(-7,0)
            carb2.move(-7,0)
            carb3.move(-7,0)


        abovePoint= road1.getCenter().getY()
        belowPoint= road2.getCenter().getY()
        dy= 30
        #if we're here, user has clicked screen
        if clickedPoint!=None:
            #user clicks below road
            if clickedPoint.getY()<belowPoint:              
                moveFrog(win,frog,-dy)
                car.move(7,0)
                car2.move(7,0)
                car3.move(7,0)
                carb.move(-7,0)
                carb2.move(-7,0)
                carb3.move(-7,0)
            #user clicks above road               
            if clickedPoint.getY()>abovePoint: 
                moveFrog(win,frog,dy)
                car.move(7,0)
                car2.move(7,0)
                car3.move(7,0)
                carb.move(-7,0)
                carb2.move(-7,0)
                carb3.move(-7,0)

        frogy=frog.getAnchor().getY()
        #if froggy makes a crossing and goes above road
        #bring froggy back to its initial position
        #and reset banner
        if frogy<abovePoint:              
               moveFrog(win, frog, (545- frogy))
               initialCrossing=initialCrossing+1
               banner.setText("{0:1} life point(s) left,{1:1} crossing(s)".format(initialLives,initialCrossing))


        frogx= frog.getAnchor().getX()
        #call function to verify is froggy has hit a car
        #accident is for the first row of cars
        #accident2 is for the second row
        car.accident(win,frogx,frogy)
        car2.accident(win,frogx,frogy)
        car3.accident(win,frogx,frogy)
        carb.accident2(win,frogx,frogy)
        carb2.accident2(win,frogx,frogy)
        carb3.accident2(win,frogx,frogy)
        #reset banner
        #initialLives will change if an accident was made (initialLives is global)
        #else banner will just stay the same
        banner.setText("{0:1} life point(s) left,{1:1} crossing(s)".format(initialLives,initialCrossing))

        #if no more lives left
        #update banner
        #getMouse to close window
        #then exit
        if initialLives<1:
            banner.setText("Game over: Froggy crossed 3 time(s)")
            win.getMouse()
            win.close()
            break

                                    
                                
main()
	 	  	    	    	 		      	   	 	

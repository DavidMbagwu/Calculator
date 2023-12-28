#This program aims to simulate a Calculator utilizing user input

#Introduction to the program
import random 
import math
from graphics import *  #This imports the graphics library necessary for animation

    

#Create a graphics window with game introduction at the top of the screen
win = GraphWin("Summer Calculator", 900, 720) 
win.setBackground("grey")

#Introductory text
message = Text(Point(600, 56), "Summer Calculator")
message.setSize(20)
message.setFace("courier")
message.setStyle("bold")
message.setTextColor('black')
message.draw(win)

#Draw button to the window
button = Text(Point(610, 300), "End Program")
button.draw(win)
button = Text(Point(400, 300), "Click to End")
button.draw(win)
button = Text(Point(400, 180), "Answer:")
button.draw(win)
Rectangle(Point(710, 350), Point(510, 250)).draw(win)
Rectangle(Point(810, 440), Point(410, 360)).draw(win)
Rectangle(Point(740, 200), Point(480, 160)).draw(win)

def aline(pt1,pt2,pt3,pt4):
    aLine = Line(Point(pt1,pt2), Point(pt3,pt4))
    aLine.draw(win)
    aLine.setWidth(8)
    aLine.setFill("black")
    
def rec(pt1,pt2,pt3,pt4):
    rect = Rectangle(Point(pt1,pt2), Point(pt3,pt4))  
    rect.setFill(color_rgb(98, 49, 0))  #Fills the shape with the solid color 
    rect.setOutline("black") #Fills the outline of the shape 
    rect.setWidth(5) #You can set the width of the shapes outline 
    rect.draw(win)
    
def circ(pt1,pt2,pt3):
    cir1 = Circle(Point(pt1, pt2), pt3)  #The values 100 and 120 are the center of the circle while 70 is the radius
    cir1.setFill("yellow") # You can get color RGB codes from the Paint app
    cir1.draw(win)    
    
rec(20,158,80,620)
rec(10,600,420,620)
aline(80,160,180,160)
aline(180,160,180,260)
circ(180,300,40)

def main():
    
    user_list = []
    user_list1 = [] 
    Ans = 0
    sqrt = math.sqrt
    ln = math.log
    log = math.log10
    π = math.pi
    e = math.e
    #Turn userlist to a sentence and display
    message1 = Text(Point(600,400), "")    
    
    while True:
        def sin(x):
            sn = math.sin((math.radians(int(x))))
            return sn
        def cos(x):
            cs = math.cos((math.radians(int(x))))
            return cs
        def tan(x):
            tn = math.tan((math.radians(int(x))))
            return tn
        def button(a,b,c,d,e,f,g):
            button = Text(Point(a, b), str(c))
            button.draw(win)
            Rectangle(Point(d, e), Point(f, g)).draw(win)
            #clickPoint = win.getMouse()
            #print(clickPoint)
            #if clickPoint :
                #input = c
                #print(input)
        
        button(483,465,7,500,480,470,450)
        
        button(533,465,8,550,480,520,450)
        
        button(583,465,9,600,480,570,450)
        
        button(633,465,' Del',650,480,620,450)
        
        button(683,465,' AC',700,480,670,450)
        
        button(733,465,' sqrt',750,480,720,450)
        
        button(483,515,4,500,530,470,500)
        
        button(533,515,5,550,530,520,500)
        
        button(583,515,6,600,530,570,500)
        
        button(633,515,' x',650,530,620,500)
        
        button(683,515,' /',700,530,670,500)
        
        button(733,515,' Ln',750,530,720,500)
        
        button(483,565,1,500,580,470,550)
        
        button(533,565,2,550,580,520,550)
        
        button(583,565,3,600,580,570,550)
        
        button(633,565,' +',650,580,620,550)
        
        button(683,565,' -',700,580,670,550)
        
        button(733,565,' Log',750,580,720,550)
        
        button(483,615,0,500,630,470,600)
        
        button(533,615,' .',550,630,520,600)
        
        button(583,615,' Exp',600,630,570,600)
        
        button(633,615,' Ans',650,630,620,600)
        
        button(683,615,' =',700,630,670,600)
        
        button(733,615,' e',750,630,720,600)
        
        button(483,665," (",500,680,470,650)
        
        button(533,665," )",550,680,520,650)
        
        button(583,665," Sin",600,680,570,650)
        
        button(633,665," Cos",650,680,620,650)
        
        button(683,665," Tan",700,680,670,650)
        
        button(733,665," π",750,680,720,650)
        
        
        #Assigns values to the buttons
        clickPoint = win.getMouse()
        pt1 = clickPoint.getX()
        pt2 = clickPoint.getY()
        #Create list for user button clicks        
            
        if 710 >= pt1 >= 510 and 350 >= pt2 >= 250 :
            win.close()
            break
        
        if 500 >= pt1 >= 470 and 480 >= pt2 >= 450 :
            #clickPoint = win.getMouse()            
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            user_input = int(7)
            #print(user_input)
            user_list.append(7)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win) 
            
            #user_list1 = []
            #print(pt1)
            #print(pt2)
            
        elif 550 >= pt1 >= 520 and 480 >= pt2 >= 450 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(8)
            #print(user_input)
            user_list.append(8)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))            
            message1.draw(win) 
            #user_list1 = []
            #print(pt1)
            #print(pt2) 
            
        elif 600 >= pt1 >= 570 and 480 >= pt2 >= 450 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(9)
            #print(user_input)
            user_list.append(9)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)             
            #print(pt1)
            #print(pt2)
            
        elif 650 >= pt1 >= 620 and 480 >= pt2 >= 450 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'Del'
            user_list.pop(-1)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)             
            #print(user_input)                        
            #print(pt1)
            #print(pt2) 
            
     
        elif 700 >= pt1 >= 670 and 480 >= pt2 >= 450 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'AC'
            user_list.clear()
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)             
            #print(user_input)             
            #print(pt1)
            #print(pt2) 
            
        elif 750 >= pt1 >= 720 and 480 >= pt2 >= 450 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'sqrt('
            user_list.append('sqrt')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)             
            #print(user_input)                        
            #print(pt1)
            #print(pt2)             
            
        if 500 >= pt1 >= 470 and 530 >= pt2 >= 500 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(4)
            user_list.append(4)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)             
            #print(user_input)
            #print(pt1)
            #print(pt2)
            
        elif 550 >= pt1 >= 520 and 530 >= pt2 >= 500 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(5)
            user_list.append(5)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)             
            #print(user_input)
            #print(pt1)
            #print(pt2) 
            
        elif 600 >= pt1 >= 570 and 530 >= pt2 >= 500 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(6)
            user_list.append(6)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)             
            #print(user_input)            
            #print(pt1)
            #print(pt2)
            
        elif 650 >= pt1 >= 620 and 530 >= pt2 >= 500 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = '*'
            user_list.append(' * ')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)            
            #print(user_input)                        
            #print(pt1)
            #print(pt2) 
            
     
        elif 700 >= pt1 >= 670 and 530 >= pt2 >= 500 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = '/'
            user_list.append('/')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)             
            #print(user_input)             
            #print(pt1)
            #print(pt2)
            
        elif 750 >= pt1 >= 720 and 530 >= pt2 >= 500 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'ln('
            user_list.append('ln( ')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)            
            #print(user_input)                        
            #print(pt1)
            #print(pt2)             
            
        if 500 >= pt1 >= 470 and 580 >= pt2 >= 550 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(1)
            user_list.append(1)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)
            #print(pt1)
            #print(pt2)
            
        elif 550 >= pt1 >= 520 and 580 >= pt2 >= 550 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(2)
            user_list.append(2)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)
            #print(pt1)
            #print(pt2) 
            
        elif 600 >= pt1 >= 570 and 580 >= pt2 >= 550 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(3)
            user_list.append(3)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)            
            #print(pt1)
            #print(pt2)
            
        elif 650 >= pt1 >= 620 and 580 >= pt2 >= 550 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = '+'
            user_list.append(' + ')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)                        
            #print(pt1)
            #print(pt2) 
            
     
        elif 700 >= pt1 >= 670 and 580 >= pt2 >= 550 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = '-'
            user_list.append('-')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)             
            #print(pt1)
            #print(pt2)
            
        elif 750 >= pt1 >= 720 and 580 >= pt2 >= 550 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'log('
            user_list.append('log( ')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)                        
            #print(pt1)
            #print(pt2)            
            
        if 500 >= pt1 >= 470 and 630 >= pt2 >= 600 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = int(0)
            user_list.append(0)
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)
            #print(pt1)
            #print(pt2)
            
        elif 550 >= pt1 >= 520 and 630 >= pt2 >= 600 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = '.'
            user_list.append('.')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)
            #print(pt1)
            #print(pt2) 
            
        elif 600 >= pt1 >= 570 and 630 >= pt2 >= 600 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()        
            
            user_input = '^'
            user_list.append('**')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)            
            #print(pt1)
            #print(pt2)
            
        elif 650 >= pt1 >= 620 and 630 >= pt2 >= 600 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'Ans'
            user_list.append('Ans')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)                        
            #print(pt1)
            #print(pt2) 
            
        elif 500 >= pt1 >= 470 and 680 >= pt2 >= 650 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = '('
            user_list.append('( ')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)            
            #print(user_input)
            
        elif 750 >= pt1 >= 720 and 630 >= pt2 >= 600 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'e'
            user_list.append('e')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)                         
            #print(user_input)                        
            #print(pt1)
            #print(pt2)            
            
        elif 550 >= pt1 >= 520 and 680 >= pt2 >= 650 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = ')'
            user_list.append(' )')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)            
            #print(user_input)
            
        elif 600 >= pt1 >= 570 and 680 >= pt2 >= 650 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'sin'
            user_list.append('sin( ')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)            
            #print(user_input)
            
        elif 650 >= pt1 >= 620 and 680 >= pt2 >= 650 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'cos'
            user_list.append('cos( ')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)            
            #print(user_input)             
            
        elif 700 >= pt1 >= 670 and 680 >= pt2 >= 650 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'tan'
            user_list.append('tan( ')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)            
            #print(user_input) 
            
        elif 750 >= pt1 >= 720 and 680 >= pt2 >= 650 :
            #clickPoint = win.getMouse()
            message1.undraw()
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            user_input = 'π'
            user_list.append('π')
            user_list1 = user_list.copy()
            print("".join(str(e) for e in user_list1))
            message1 = Text(Point(600,400), ("".join(str(e) for e in user_list1)))
            message1.draw(win)            
            #print(user_input)                      
     
        elif 700 >= pt1 >= 670 and 630 >= pt2 >= 600 :
            #clickPoint = win.getMouse()
            message1.undraw()
            user_list1 = user_list.copy()
            print(round(eval("".join(str(e) for e in user_list1)),4))
            message1 = Text(Point(600,180), round(eval("".join(str(e) for e in user_list1)),4))
            message1.draw(win)
            Ans = round(eval("".join(str(e) for e in user_list1)),4)
            pt1 = clickPoint.getX()
            pt2 = clickPoint.getY()
            
            #print(pt1)
            #print(pt2) 
            
            
        #else:      
            #break
            ##win.getMouse()
            ##win.close()
    
        continue
        #check = input("Do you want to quit or start again? enter Y to restart or N to end: ")
        #if check.upper() == "Y": #go back to the top
            #continue
    
        #else:
            #break        
        
        
        
        
        
        
        
        
        
main()

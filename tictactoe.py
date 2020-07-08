from tkinter import *

# Root Widget Creation
root = Tk()                         # App instance
root.minsize(300,300)               # App size
root.title('Tic Tac Toe')           # Title
root.resizable(0,0)                 # No maximize

icon = PhotoImage(file='ttt.png')   # Title Icon
root.iconphoto(False,icon)


# Global count variable, to keep an account of number of times clicked on the board
count = None

# Global canvas, empty board placed over the root, with the same size
canvas = None

# Places where someone has already clicked
clicked = []
x_clicks = []
o_clicks = []

# Global Boxes
Boxes = {1:[0,0],2:[0,1],3:[0,2],4:[1,0],5:[1,1],6:[1,2],7:[2,0],8:[2,1],9:[2,2]}

# Global win
win = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]

# The game
def newgame():
    global canvas,count,clicked,x_clicks,o_clicks
    clicked = []
    x_clicks = []
    o_clicks = []
    count = 0
    canvas = Canvas(root,height = 300,width = 300,bd=0)
    canvas.pack(anchor=CENTER)


    # Creating cross lines on the board
    canvas.create_line(100,0,100,300,width=5)
    canvas.create_line(200,0,200,300,width=5)
    canvas.create_line(0,100,300,100,width=5)
    canvas.create_line(0,200,300,200,width=5)

    canvas.bind("<Button-1>", coord)        # Binding click event with the board
    # So everytime the left mouse button is clicked on the canvas area, coord method is called


def draw_shape(coords,shape):

    if shape == 1:  # Draw X at given co-ordinates
        canvas.create_line(coords[0][0],coords[0][1],coords[3][0],coords[3][1],width=5)
        canvas.create_line(coords[1][0],coords[1][1],coords[2][0],coords[2][1],width=5)
    else:           # Draw O at given co-ordinates
        canvas.create_oval(coords[0][0],coords[0][1],coords[3][0],coords[3][1],width=5)

def kill(event):                        # Kill the canvas
    global canvas
    canvas.destroy()
    newgame()                           # Start newgame

def drawWinner(box_no,draw):            # Draw winning green line
    if not draw:                        # if Draw, no winning line will be drawn
        global Boxes

        start_x = Boxes[box_no[0]][0] * 100 + 50
        start_y = Boxes[box_no[0]][1] * 100 + 50
        end_x = Boxes[box_no[2]][0] * 100 + 50
        end_y = Boxes[box_no[2]][1] * 100 + 50

        canvas.create_line(start_x,start_y,end_x,end_y,width=5,fill='green')

    canvas.bind('<Button-1>',kill)      # Any case, draw/win, start newgame


def check(x,o):   # Show DRAW, WINNER and New Game
    global win,Boxes,count
    x = sorted(x)
    o = sorted(o)
    for i in win:
        if set(i).issubset(set(x)):                 # if x in win
            # print('X wins')
            drawWinner(sorted(list(set(i)&set(x))),0)
        if set(i).issubset(set(o)):                 # if o in win
            # print('O wins')
            drawWinner(sorted(list(set(i)&set(o))),0)
        if count == 9:                              # if all boxes are filled
            # print('DRAW')
            drawWinner(None,1)                      # No winned, draw is set to 1
            count = 0


# Getting the box_no
def coord(event):       # gets the box no and co-ordinate, calls the draw shape method to draw
                        # the shape at appropriate position

    global count,clicked,Boxes  # Referring variable outside the function
    global x_clicks,o_clicks

    x = event.x         # Get x and y co-ordinate of the click event
    y = event.y
    box_no = None       # To store the current box number
    if x <= 100:
        if y <= 100:
            box_no = Boxes[1]
        elif y > 100 and y < 200:
            box_no = Boxes[2]
        else:
            box_no = Boxes[3]

    if x > 100 and x < 200:
        if y <= 100:
            box_no = Boxes[4]
        elif y > 100 and y < 200:
            box_no = Boxes[5]
        else:
            box_no = Boxes[6]

    if x >= 200:
        if y <= 100:
            box_no = Boxes[7]
        elif y >= 100 and y < 200:
            box_no = Boxes[8]
        else:
            box_no = Boxes[9]

    if box_no not in clicked:       # To check if the box was previously clicked

        count+=1                    # Increment count
        shape = count%2             # Switch shape between X and O based on count

        clicked.append(box_no)

        for num , lst in Boxes.items():
            if box_no == lst:
                if shape == 1:
                    x_clicks.append(num)
                else:
                    o_clicks.append(num)

        # Forming co-ordinates for drawing shapes
        top_left = [box_no[0] * 100 + 20 , box_no[1] * 100 + 20]
        top_right = [box_no[0] * 100 + 20 , box_no[1] * 100 + 80]
        bottom_left = [box_no[0] * 100 + 80 , box_no[1] * 100 + 20]
        bottom_right = [box_no[0] * 100 + 80 , box_no[1] * 100 + 80]

        coords = [top_left,top_right,bottom_left,bottom_right]

        draw_shape(coords,shape)  # Send all the co-ordinates and the required shape to draw
        if count>=5:              # At least 5 clicks are needed for any one player to win
            check(x_clicks,o_clicks)  # Check for winner/DRAW


newgame()                         # Pack canvas

# Root Mainloop
root.mainloop()

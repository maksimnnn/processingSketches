x=100
x2=300
y=200
y2=200
def setup():
    size(400,400)
def draw():
    background(255)
    global x,x2,y,y2
    ellipse(x,y,40,40)
    rect(x,y,50,50)
    ellipse(x2,y2,40,40)
    rect(x2,y2,50,50)
    if keyPressed and key == 'w':
        y-=2
    if keyPressed and key == 'd':
        x+=2
    if keyPressed and key == 's':
        y+=2
    if keyPressed and key== 'a':
       x-=2
    if keyPressed and keyCode == UP:
        y2-=2
    if keyPressed and keyCode == RIGHT:
        x2+=2
    if keyPressed and keyCode == DOWN:
        y2+=2
    if keyPressed and keyCode == LEFT:
       x2-=2

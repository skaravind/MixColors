from mixigColors import mix
nc = 25
r = 0
g = 0
y = 0
value = 0
colr = color(255)
tiles = [[None for _ in range(5)] for _ in range(5)]
class Tile:
    pass

def setup():
    global tiles
    colr = color(255)
    font = createFont('San Serif', 16)
    background(255)
    size(500,580)
    fill(colr)
    stroke(0)
    strokeWeight(2)
    for i in range(0,500,100):
        for j in range(0,500,100):
            rect(i, j, 100, 100)
            tiles[i/100][j/100] = Tile()
            tiles[i/100][j/100].pos = [i,j]
            tiles[i/100][j/100].col = colr
    textAlign(CENTER)
    textFont(font)
    fill(0)
    text('Red = R, Green = G, Click tile to fill. \'C\' to clear', width/2, 520)
    global r, g, nc, y
    text('NC = %d, R = %d, G = %d, Y = %d' %(nc,r,g,y), width/2, 570)

def draw():
    global colr
    global r, g, nc, y
    if mousePressed and mouseY<500 and mouseX<500 and mouseX>0 and mouseY>0:
        XX = mouseX - mouseX%100
        YY = mouseY - mouseY%100
        prev = colr
        tileCol = tiles[XX/100][YY/100].col
        colr = mix(tileCol,colr)
        stroke(0)
        strokeWeight(2)
        fill(colr)
        rect(tiles[XX/100][YY/100].pos[0],tiles[XX/100][YY/100].pos[1], 100,100)
        tiles[XX/100][YY/100].col = colr
        if colr == tileCol:
            pass
        elif colr == color(255,0,0):
            r+=1
            nc-=1
        elif colr == color(0,255,0):
            g+=1
            nc-=1
        elif colr == color(255,255,0):
            y+=1
            if tileCol == color(0,255,0):
                g-=1
            else:
                r-=1
        fill(255)
        noStroke()
        rect(0,555,500,20)
        stroke(0)
        fill(0)
        text('NC = %d, R = %d, G = %d, Y = %d' %(nc,r,g,y), width/2, 570)
        colr = prev

def keyPressed():
    global colr
    if key == 'g':
        fill(255)
        noStroke()
        rect(0,525,500,20)
        colr = color(0,255,0)
        fill(colr)
        text('Green color selected', width/2, 540)
    if key == 'r':
        fill(255)
        noStroke()
        rect(0,525,500,20)
        colr = color(255,0,0)
        fill(colr)
        text('Red color selected', width/2, 540)
    if key == 'c':
        setup()
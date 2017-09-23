from mixigColors import mix

value = 0
colr = color(255)
tiles = [[None for _ in range(5)] for _ in range(5)]
class Tile:
    pass

def setup():
    global tiles
    colr = color(255)
    font = createFont('Georgia', 16)
    background(255)
    size(500,550)
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

def draw():
    global colr
    if mousePressed and mouseY<500 and mouseX<500 and mouseX>0 and mouseY>0:
        XX = mouseX - mouseX%100
        YY = mouseY - mouseY%100
        prev = colr
        colr = mix(tiles[XX/100][YY/100].col,colr)
        stroke(0)
        strokeWeight(2)
        fill(colr)
        rect(tiles[XX/100][YY/100].pos[0],tiles[XX/100][YY/100].pos[1], 100,100)
        tiles[XX/100][YY/100].col = colr
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
'''
Created on 30/01/2014

@author: HasHPIT
'''

import pyglet
# Disable error checking for increased performance
#pyglet.options['debug_gl'] = False
from pyglet.gl import *
from pyglet.window import key
from pyglet.text import Label

from life.life import world
from life.grass import grass
from life.rabbit import rabbit

#initialize and globals
config = Config(sample_buffers=1, samples=4, depth_size=16, double_buffer=True,)
window = pyglet.window.Window(resizable=True, config=config)
#window = pyglet.window.Window(fullscreen=True) #resizable=True)
#window.set_exclusive_mouse()
keys = key.KeyStateHandler()
window.push_handlers(keys)
sx = 0
grid_width = 80
grid_height = 80
grid_px_width = float(window.width/grid_width)
grid_px_height= float(window.height/grid_height)
vertices = []
colors = []
#label = Label("lol", x=0, y=100)
#fps_display = pyglet.clock.ClockDisplay()

verden = world(grid_width,grid_height)
verden.add_life(grass(40,40,verden))

for x in range(grid_width):
    for y in range(grid_height):
        left = x*grid_px_width
        right = x*grid_px_width + grid_px_width
        down = y*grid_px_height
        up = y*grid_px_height+grid_px_height
        vertices += [left,down,left,up,right,up,right,down]  #leftDown,leftUp,rightUp,rightDown
        if x%2: #hvis lige raekke
            if y%2: #og lige kolonne
                colors += [0.1,0.1,0.1]*4
            else:
                colors += [0.2,0.1,0.1]*4
        else:
            if y%2: #og lige kolonne
                colors += [0.1,0.1,0.1]*4
            else:
                colors += [0.5,0.1,0.1]*4

vertices_gl = (GLfloat * len(vertices))(*vertices)
colors_gl = (GLfloat * len(colors))(*colors)
glEnableClientState(GL_VERTEX_ARRAY)
glEnableClientState(GL_COLOR_ARRAY)

@window.event
def on_resize(width, height):
    global vertices
    global vertices_gl
    global grid_px_width
    global grid_px_height
    grid_px_width = float(width/grid_width)
    grid_px_height= float(height/grid_height)
    vertices = []
    for x in range(grid_width):
        for y in range(grid_height):
            left = x*grid_px_width
            right = x*grid_px_width + grid_px_width
            down = y*grid_px_height
            up = y*grid_px_height+grid_px_height
            vertices += [left,down,left,up,right,up,right,down]  #leftDown,leftUp,rightUp,rightDown
    vertices_gl = (GLfloat * len(vertices))(*vertices)

@window.event
def on_draw():
    #window.clear()
    glLoadIdentity()
    glVertexPointer(2, GL_FLOAT, 0, vertices_gl)
    glColorPointer(3, GL_FLOAT, 0, colors_gl)
    glDrawArrays(GL_QUADS, 0, len(vertices)//2)
    #label.draw()
    #fps_display.draw()

def draw_the_world():
    global verden
    global colors
    global colors_gl
    #what is a list of dicts
    for y in range(grid_height):
        for x in range(grid_width):
            pos = y*grid_width+x
            if len(verden.the_world[pos])>0:
                for obj in verden.the_world[y*grid_width+x]: #iterate over a copy of the object list so that we can remove items from the real list
                    if obj.what == "grass":
                        #phew..its just some grass
                        if obj.size==0:
                            #actually there is no grass, just dirt
                            #lets color it
                            colors[y*grid_width*12+x*12:y*grid_width*12+x*12+12] = [0.5,0.35,0.3]*4
                        else:
                            #lets color it
                            colors[y*grid_width*12+x*12:y*grid_width*12+x*12+12] = [0.0,1.0-0.1*obj.size,0.0]*4
                    elif obj.what == "rabbit":
                        #uuh its a bunny....color the bunny
                        colors[y*grid_width*12+x*12:y*grid_width*12+x*12+12] = [1.0,1.0,1.0]*4
                    else:
                        print "theres a " + str(obj.what) + " at " + str(x) + "," + str(y)
                        print "I dont know how to draw that...:("
            else:
                #nothing here
                colors[y*grid_width*12+x*12:y*grid_width*12+x*12+12] = [0.0,0.0,0.1]*4
    colors_gl = (GLfloat * len(colors))(*colors)

def tick(dt):
    #i should pass dt to tock but for testing I am just passing 1
    #a tock should be one hour long
    verden.tock()
    draw_the_world()

tocktryk = 0
spacetryk = 0
running = 0

def update(dt):
    global tocktryk, spacetryk, running
    if keys[key.UP] and tocktryk == 0:
        tick(1)
        tocktryk = 1

    if keys[key.SPACE] and spacetryk == 0:
        spacetryk = 1
        if running == 0:
            pyglet.clock.schedule_interval_soft(tick,0.1)
            running = 1
        else:
            pyglet.clock.unschedule(tick)
            running = 0

    if not keys[key.UP]:
        tocktryk = 0
    if not keys[key.SPACE]:
        spacetryk = 0

if __name__ == '__main__':
    pyglet.clock.schedule(update)
    pyglet.app.run()

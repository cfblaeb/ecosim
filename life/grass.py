'''
Created on 30/01/2014

@author: HasHPIT
'''
from plant import plant
import random

class grass(plant):
    '''
    classdocs
    this is grass
    '''
    what = "grass"

    def tock(self,dt=1):
        self.grow(dt)
        if random.randint(0,99)>(100-dt*10):
            self.spread()
    
    def spread(self):
        #grass will spread +/- 10 x and y
        nx = self.x + random.randint(-10,10)
        ny = self.y + random.randint(-10,10)
        grassy = [x for x in self.world.get_pos_list(nx,ny) if x.what == "grass"]
        if len(grassy) == 0:
            self.world.add_life(grass(nx,ny,self.world))
        else:
            print "tried to grow grass where there already was some"
        
    def eat_me(self,amount=1):
        self.size -= amount
        return self.size

'''
Created on 30/01/2014

@author: HasHPIT
'''
from life import plant
import random

class grass(plant):
    '''
    classdocs
    this is grass
    '''
    what = "grass"

    def tock(self,dt):
        self.grow(dt)
        self.chance_of_spread+= dt
        if random.randint(0,99)<self.chance_of_spread:
            self.spread()
            self.chance_of_spread = 0
    
    def spread(self):
        #grass will spread +/- 10 x and y
        nx = self.x + random.randint(-10,10)
        ny = self.y + random.randint(-10,10)
        grassy = [x for x in self.world.get_pos_list(nx,ny) if x.what == "grass"]
        if len(grassy) == 0:
            self.world.add_life(grass(nx,ny,self.world))
        
    def eat_me(self,amount=1):
        self.size -= amount
        return self.size

    def grow(self, dt):
        '''
        grow the plant
        '''
        self.size += dt*self.growth_per_tock
        if self.size>self.max_size:
            self.size = self.max_size

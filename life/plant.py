'''
Created on 30/01/2014

@author: HasHPIT
'''
from life import *

class plant(object):
    '''
    This is the foundation of any plant
    '''
    def __init__(self, x, y, world, growth_speed=1, size=0, max_size=5):
        '''
        growth_speed is the amount of tocks to growth.
        It will grow until size reaches max_size 
        '''
        self.growth_speed = growth_speed
        self.__tocks_to_growth = growth_speed
        self.size = size
        self.max_size = max_size
        self.x = x
        self.y = y
        self.world = world

    def grow(self, dt=1):
        '''
        grow the plant
        '''
        self.__tocks_to_growth -= dt
        if self.__tocks_to_growth<=0 and self.size<self.max_size:
            self.size+=dt
            if self.size>self.max_size:
                self.size = self.max_size
            self.__tocks_to_growth=self.growth_speed

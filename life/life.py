'''
Created on 31/01/2014

@author: HasHPIT
'''
 
class world(object):
    '''
    Much Life
    '''
    def __init__(self, width, height, time_of_day=8):
        self.width = width
        self.height = height    
        self.the_world = [[] for x in xrange(width*height)]
        self.life_list = []
        self.time_of_day = time_of_day
        self.day = 0
    
    def inbounds(self, x, y):
        if x < self.width and x >= 0 and y < self.height and y>= 0:
            return True
        else:
            return False

    def add_life(self, who):
        if self.inbounds(who.x, who.y):
            self.life_list.append(who)
            self.the_world[self.width*who.y+who.x].append(who)

    def get_pos_list(self,x,y):
        if self.inbounds(x,y):
            for entity in self.the_world[y*self.width + x]:
                yield entity
  
    def tock(self, dt=1):
        self.time_of_day+=dt
        if self.time_of_day>24:
           self.time_of_day = 0
           self.day += 1
        for entity in self.life_list:
            entity.tock(dt)

class plant(object):
    '''
    This is the foundation of any plant
    '''
    def __init__(self, x, y, world, growth_per_tock=0.05, size=0, max_size=5):
        '''
        growth_speed is the amount of tocks to growth.
        It will grow until size reaches max_size 
        '''
        self.growth_per_tock = growth_per_tock
        self.size = size
        self.max_size = max_size
        self.x = x
        self.y = y
        self.world = world
        self.chance_of_spread = 0
        self.age = 0

class animal(object):
    '''
    This is the foundation of any animal
    '''
    def __init__(self, x, y, world):
        '''
        growth_speed is the amount of tocks to growth.
        It will grow until size reaches max_size 
        '''
        self.x = x
        self.y = y
        self.world = world
        self.age = 0

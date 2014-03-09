'''
Created on 31/01/2014

@author: HasHPIT

This represents the basic functions of life
Specific life has individual classes that inherits the base life
'''

class life(object):
    '''
    What does all life have in common?
    A position in the world: x,y, world
    All life has an age
    All life spends energy
    '''
    def __init__(self, world, x, y):
        self.x = x
        self.y = y
        self.world = world
        self.age = 0

class plant(life):
    def __init__(self, growth_per_tock=0.05, size=0, max_size=5, **kwds):
        super(plant, self).__init__(**kwds)
        self.growth_per_tock = growth_per_tock
        self.size = size
        self.max_size = max_size
        self.chance_of_spread = 0

class animal(life):
    def __init__(self, **kwds):
        super(animal, self).__init__(**kwds)
'''
Created on Mar 8, 2014

@author: hashpit

This represents a world.
It keeps track of life in a grid (width,height)
New life can be added
A list of creatures in a specific spot can be returned
And Time can pass
'''

class world(object):
    '''
    Much Life
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._the_world = [[] for x in xrange(width*height)]

        self._life_list = []
        self.time = 0

    def __inbounds(self, x, y):
        if x < self.width and x >= 0 and y < self.height and y>= 0:
            return True
        else:
            return False

    def add_life(self, who):
        if self.__inbounds(who.x, who.y):
            self._life_list.append(who)
            self._the_world[self.width*who.y+who.x].append(who)

    def get_pos_list(self,x,y):
        if self.__inbounds(x,y):
            for entity in self._the_world[y*self.width + x]:
                yield entity

    def tock(self, dt=1):
        self.time+=dt
        for entity in self._life_list:
            entity.tock(dt)

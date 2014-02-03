'''
Created on 31/01/2014

@author: HasHPIT
'''
 
class world(object):
    '''
    Much Life
    '''
    def __init__(self, width, height):
        self.width = width
        self.height = height    
        self.the_world = [[] for x in xrange(width*height)]
        self.life_list = []
    
    def inbounds(self, x, y):
        if x < self.width and x >= 0 and y < self.height and y>= 0:
            return True
        else:
            return False

    def add_life(self, who):
        if self.inbounds(who.x, who.y):
            self.life_list.append(who)
            self.the_world[self.width*who.y+who.x].append(who)
        else:
            print "tried to add " + str(who.what)
            print "at x: " + str(who.x)
            print "and y: " + str(who.y)

    def get_pos_list(self,x,y):
        if self.inbounds(x,y):
            for entity in self.the_world[y*self.width + x]:
                yield entity

    def tock(self, dt=1):
        for entity in self.life_list:
            entity.tock(dt)

'''
Created on 30/01/2014

@author: HasHPIT
'''
from life import animal

class rabbit(animal):
    '''
    This is a rabbit..I guess
    '''
    what = "rabbit"
    def __init__(self, **kwds):
        super(rabbit, self).__init__(**kwds)
    def tock(self, dt):
        pass


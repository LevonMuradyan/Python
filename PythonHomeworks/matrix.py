#!/usr/bin/env python
import math
    
list1 = [[1,2,3], 
         [2,2,2], 
         [7,8,9]]

list2 = [[1,4,7], 
         [2,2,2], 
         [3,6,9]]

print filter(lambda v: math.log(v,2) != int(math.log(v,2)), map(lambda x,y :reduce(lambda x,y: x*y, map(lambda xi,yi: xi+yi, x, y)), list1, list2))

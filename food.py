import random
import queue
class Food:
     def __init__(self,queue):
         self.queue=queue
         self.generate_food()
 
     def generate_food(self):
         x=random.randrange(5,480,10)
         y=random.randrange(5,295,10)
         self.position=(x,y)
         rectangle_position=(x-5,y-5,x+5,y+5)
         self.queue.put({'food':rectangle_position})

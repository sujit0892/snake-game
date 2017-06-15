import threading
import time
import queue
from food import *
class Snake(threading.Thread):
     is_game_over=False

     def __init__(self,queue):
         threading.Thread.__init__(self)
         self.queue=queue
         self.point_earned=0
         self.daemon=True
         self.snake_points=[(495, 55), (485, 55), (475, 55),(465, 55), (455, 55)]
         self.food=Food(queue)
         self.direction='Left'
         self.start()
     
     def run(self):
        while not self.is_game_over:
            self.queue.put({"move":self.snake_points})
            time.sleep(0.1)
            self.move()

     def move(self):
        new_snake_point=self.new_cordinate()
        if new_snake_point==self.food.position:
           self.point_earned+=1
           self.queue.put({"point_earned":self.point_earned})
           self.food.generate_food()
        else:
            self.snake_points.pop(0)
        self.check_game_over(new_snake_point)
        self.snake_points.append(new_snake_point)
    
     def onkeypress(self,e):
         self.direction=e.keysym
     
     def new_cordinate(self):
        last_x, last_y = self.snake_points[-1]
        if self.direction == 'Up':
            new_snake_point = (last_x, last_y - 10)
        elif self.direction == 'Down':
            new_snake_point = (last_x, last_y + 10)
        elif self.direction == 'Left':
            new_snake_point = (last_x - 10, last_y)
        elif self.direction == 'Right':
            new_snake_point = (last_x + 10, last_y)
        return new_snake_point

     def check_game_over(self,snake_point):
         x,y = snake_point
         if not -5 < x < 505 or not -5 < y < 315 or snake_point in self.snake_points:
             self.is_game_over = True
             self.queue.put({'game_over': True})

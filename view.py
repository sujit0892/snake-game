from tkinter import *
import queue
from snake import *
class View(Tk):
     def __init__(self,queue):
         Tk.__init__(self)
         self.queue=queue
         self.create_gui()
         self.queue_handler()

     def create_gui(self):
         self.canvas = Canvas(self, width=495, height=305,
         bg='#FF75A0')
         self.canvas.pack()
         self.snake = self.canvas.create_line((0, 0), (0,0),
         fill='#FFCC4C', width=10)
         self.food = self.canvas.create_rectangle(0, 0, 0, 0,
         fill='#FFCC4C', outline='#FFCC4C')
         self.points_earned = self.canvas.create_text(455, 15,
         fill='white', text='Score:0')
     
     def queue_handler(self):
         try:
             while True:
                 task=self.queue.get_nowait()
                 if 'game_over' in task:
                     self.game_over()
                 elif 'move' in task:
                     points=[x for point in task['move'] for x in point]
                     self.canvas.coords(self.snake,*points)
                 elif 'food' in task:
                     self.canvas.coords(self.food,*task['food'])
                 elif 'point_earned' in task:
                      self.canvas.itemconfigure(self.points_earned, text="Score: {}".format(task['point_earned']))
         except queue.Empty:
             self.after(100,self.queue_handler)
      
     def game_over(self):
         self.canvas.create_text(200, 150, fill='white', text='Game Over')
         quit_button = Button(self, text='Quit', command=self.destroy)
         self.canvas.create_window(200, 180, anchor='nw', window=quit_button)

def main():
    q = queue.Queue()
    gui = View(q)
    snake = Snake(q)
    for key in ("Left", "Right", "Up", "Down"):
        gui.bind("<Key-{}>".format(key), snake.onkeypress)
    gui.mainloop()
if __name__ == '__main__':
    main() 

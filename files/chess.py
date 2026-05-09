import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

import board
import piece

class Main(App):
   def __init__(self, myBoard, **kwargs):
      super().__init__(**kwargs)
      self.myBoard = myBoard

   def build(self):
      ## for starters, board has text equal to 
      grid = GridLayout(cols=8)

      for x in range(8):
         for y in range(8):
            # Each odd button to have background white
            # start from 0 so its actually even
            # background is white white x is even and y is even and when x is odd and y is odd
            if (y % 2 == 0 and x % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
               grid.add_widget(Button(
                  background_color = (5,5,5)
                  ))
            else:
               grid.add_widget(Button(background_color = (1.7,0.7,0.6)))
      return grid


myBoard = board.Board()
Main(App).run()
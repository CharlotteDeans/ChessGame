import kivy
kivy.require('2.3.1')
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget

import board
import piece

class BoardApp(Widget):
   pass

class MainApp(App):
   def __init__(self, myBoard, **kwargs):
      super().__init__(**kwargs)
      self.myBoard = myBoard

   def build(self):
      BoardApp()
      for x in range(8):
         for y in range(8):
            if (y % 2 == 0 and x % 2 == 0) or (y % 2 == 1 and x % 2 == 1):
               BoardApp().add_widget(Button(background_color = (5,5,5)))
            else:
               BoardApp().add_widget(Button(background_color = (1.7,0.7,0.6)))
      return BoardApp()
      
myBoard = board.Board()
MainApp(App).run()
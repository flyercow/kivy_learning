# -*- coding: utf-8 -*-
"""
Basic app from kivy official site
"""

import kivy
kivy.require('2.1.0') # Replace with current kivy version

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    
    def build(self):
        return Label(text="Hello World")
    
if __name__ == '__main__':
    MyApp().run()
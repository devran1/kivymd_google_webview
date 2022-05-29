#!/usr/bin/env python3



from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from cefbrowser import CEFBrowser

class MainApp(MDApp):
    def build(self):
        return CEFBrowser(url="https://www.google.com/")
        

MainApp().run()

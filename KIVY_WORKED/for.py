#!/usr/bin/env python3

from kivy.app import App
from cefbrowser import CEFBrowser

class SimpleBrowserApp(App):
    def build(self):
        return CEFBrowser(url="https://www.google.com/")
SimpleBrowserApp().run()

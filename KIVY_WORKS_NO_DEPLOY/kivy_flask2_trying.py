#!/usr/bin/env python3

import kivy
#kivy.require('1.11.1')  # Set to your Kivy version
from kivy.app import App

from kivy.uix.textinput import TextInput


from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen


from flask import Flask, render_template, request,redirect
from flask_restful import reqparse, abort, Api, Resource
import eventlet
from eventlet import wsgi
from threading import Thread

import sys
import signal
from multiprocessing import Process

from cefpython3 import cefpython as cef3


#print(dir(cef3))
cef3.Initialize(settings={}, switches={'disable-gpu': ""})
cef3.Initialize(settings={}, switches={'allow-insecure-localhost': ""})



from cefbrowser import CEFBrowser
##################################################
"""
import unittest
import logging
"""
"""
from selenium import webdriver

PATH=".chromedriver"

#print(webdriver.current_url)

driver = webdriver.Chrome(executable_path=PATH)
"""
#webdriver.Chrome()
#print(driver.current_url)



"""
from selenium.webdriver import Firefox
from selenium.webdriver.support.events import EventFiringWebDriver, AbstractEventListener

class MyListener(AbstractEventListener):
    def before_navigate_to(self, url, driver):
        print("Before navigate to %s" % url)
    def after_navigate_to(self, url, driver):
        print("After navigate to %s" % url)


class Test(unittest.TestCase):
    def test_logging_file(self):

        driver_plain = webdriver.Chrome(executable_path=r'D:PATHchromedriver.exe');
        edriver = EventFiringWebDriver(driver_plain, MyListener())
        edriver.get("https://google.com")

if __name__ == "__main__":
    unittest.main()
"""


################

app = Flask(__name__)
def start_flask():
   

    #wsgi.server(eventlet.listen(), app)

    @app.route('/')
    def index():
            
        return render_template("index.html")

    app.run()


class MyApp(App):
    
    

    def build(self):
        
        return CEFBrowser("http://127.0.0.1:5000") #http://127.0.0.1:5000 

        


if __name__ == '__main__':
    Process(target=start_flask).start()
    MyApp().run()
        

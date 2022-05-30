#!/usr/bin/env python3

from kivymd.app import App


from flask import Flask, render_template

from threading import Thread

from multiprocessing import Process

from cefpython3 import cefpython as cef3


#print(dir(cef3))
cef3.Initialize(settings={}, switches={'disable-gpu': ""})
cef3.Initialize(settings={}, switches={'allow-insecure-localhost': ""})



from cefbrowser import CEFBrowser



app = Flask(__name__)
def start_flask():
   

    #wsgi.server(eventlet.listen(), app)

    @app.route('/')
    def index():
            
        return render_template("index.html")

    app.run()


class MyApp(App):
    
    

    def build(self):
        
        return CEFBrowser("http://127.0.0.1:5000") 

        


if __name__ == '__main__':
    Process(target=start_flask).start()
    MyApp().run()
        

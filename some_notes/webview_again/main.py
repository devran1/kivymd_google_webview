import kivy                                                                                     
from kivy.app import App                                                                        
from kivy.lang import Builder                                                                   
from kivy.utils import platform                                                                 
from kivy.uix.widget import Widget                                                              
from kivy.clock import Clock      
from android.runnable import run_on_ui_thread 
import os
try:
     from jnius import autoclass

except KeyError:
     os.environ['JDK_HOME'] = "/usr/lib/jvm/java-1.8.0-openjdk-amd64"
     os.environ['JAVA_HOME'] = "/usr/lib/jvm/java-1.8.0-openjdk-amd64"
     from jnius import autoclass

                                                              
#from jnius import autoclass                                                                     
                                                  
                                                                                                
WebView = autoclass('android.webkit.WebView')                                                   
WebViewClient = autoclass('android.webkit.WebViewClient')                                       
activity = autoclass('org.kivy.android.PythonActivity').mActivity                              
                                                                                                
class Wv(Widget):                                                                               
    def __init__(self, **kwargs):                                                               
        super(Wv, self).__init__(**kwargs)                                                      
        Clock.schedule_once(self.create_webview, 0)                                             
                                                                                                
    @run_on_ui_thread                                                                           
    def create_webview(self, *args):                                                            
        webview = WebView(activity)                                                             
        webview.getSettings().setJavaScriptEnabled(True)                                        
        wvc = WebViewClient();                                                                  
        webview.setWebViewClient(wvc);                                                          
        activity.setContentView(webview)                                                        
        webview.loadUrl('http://www.google.com')
                                                                                                
class ServiceApp(App):                                                                          
    def build(self):                                                                            
        return Wv()                                                                             
                                                                                                
if __name__ == '__main__':                                                                      
    ServiceApp().run()

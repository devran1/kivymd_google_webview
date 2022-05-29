#!/usr/bin/env python3

from cefpython3 import cefpython as cef
import platform
import sys



cef.Initialize()
cef.CreateBrowserSync(url="https://www.google.com/",
                          window_title="Hello World!")
cef.MessageLoop()
cef.Shutdown()



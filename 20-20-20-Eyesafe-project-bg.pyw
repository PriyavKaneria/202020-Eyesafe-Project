import win32gui
import win32con
import time
import threading 

def setInterval(interval, times = -1):
    # This will be the actual decorator,
    # with fixed interval and times parameter
    def outer_wrap(function):
        # This will be the function to be
        # called
        def wrap(*args, **kwargs):
            stop = threading.Event()

            # This is another function to be executed
            # in a different thread to simulate setInterval
            def inner_wrap():
                i = 0
                while i != times and not stop.isSet():
                    stop.wait(interval)
                    function(*args, **kwargs)
                    i += 1

            t = threading.Timer(0, inner_wrap)
            t.daemon = True
            t.start()
            return stop
        return wrap
    return outer_wrap

@setInterval(1200,-1)
def offandon(): 
    #to turn off use :-
    win32gui.PostMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, 2)
    time.sleep(2)
    #turn on use :-
    win32gui.PostMessage(win32con.HWND_BROADCAST,win32con.WM_SYSCOMMAND, win32con.SC_MONITORPOWER, -1)
  
timer = offandon()
time.sleep(24000)
timer.set()

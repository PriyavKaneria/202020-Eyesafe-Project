import subprocess
import time
import threading

def setInterval(interval, times=-1):
    def outer_wrap(function):
        def wrap(*args, **kwargs):
            stop = threading.Event()
            def inner_wrap():
                i = 0
                while i != times and not stop.is_set():
                    stop.wait(interval)
                    function(*args, **kwargs)
                    i += 1

            t = threading.Timer(0, inner_wrap)
            t.daemon = True
            t.start()
            return stop
        return wrap
    return outer_wrap

@setInterval(1200, -1)
def offandon():
    # To turn off the monitor
    subprocess.call(['xset', 'dpms', 'force', 'off'])
    time.sleep(2)
    # To turn on the monitor
    subprocess.call(['xset', 'dpms', 'force', 'on'])

timer = offandon()
time.sleep(1200)
timer.set()


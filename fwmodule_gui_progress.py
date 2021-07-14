"""fwmodule_gui_progress"""

import threading
import datetime as dt
import tkinter as tk
import tkinter.ttk

flag_release = False

try:
    import practical_package.release as r
except Exception:
    pass
else:
    flag_release = r.flag

if flag_release:
    from practical_package.fwmodule_general import *
else:
    # variable route path control for VSCode debug
    import sys, os
    if not [i for i in sys.path if i == os.path.dirname(__file__)]:
        sys.path.append(os.path.dirname(__file__))
    from fwmodule_general import *

"""
    GUI Progress Receiver
    details: Sub Calc (Nondeterministic processing)
"""
class ProgressReceiver:
    def __init__(self, place_x, place_y):
        self.flag_loop = False
        self.flag_progress = False
        self.place_x = place_x
        self.place_y = place_y
        self.y_margin = 17
        self.sec = 0.2

        # ascii art (DejaVu Sans)
        self.label_python = []
        self.label_python.append(tk.Label(text="                        (    I      I     I    )"))
        self.label_python.append(tk.Label(text="                        (    I     III    I    )"))
        self.label_python.append(tk.Label(text="                     (    I        III       I    )"))
        self.label_python.append(tk.Label(text="                  ( (  I        I      I        I  ) )"))
        self.label_python.append(tk.Label(text="              ( (  I        I              I        I  ) )"))
        self.label_python.append(tk.Label(text="             ( ( I         I                I         I ) )"))
        self.label_python.append(tk.Label(text="            ( (   I            I        I            I   ) )"))
        self.label_python.append(tk.Label(text="             (   ( I             I    I             I )   )"))
        self.label_python.append(tk.Label(text="              ( ( (  I I           I           I I  ) ) )"))
        self.label_python.append(tk.Label(text="                 ( (( I    I               I    I )) )"))
        self.label_python.append(tk.Label(text="                    ( [(Θ))  I      I  ((Θ)] )"))
        self.label_python.append(tk.Label(text="                      ( (I                    I) )"))
        self.label_python.append(tk.Label(text="                        ( (I                I) )"))
        self.label_python.append(tk.Label(text="                          (    o      o    )"))
        self.label_python.append(tk.Label(text="                            (  __人__  )"))
        cnt_y_margin = counter(self.place_y, self.y_margin)
        for i in self.label_python:
            i.place(x=self.place_x, y=cnt_y_margin.result())
            cnt_y_margin.count()

        # moving label
        self.lines_move = []
        self.lines_move.append("                                   ((")
        self.lines_move.append("                                   ))")
        self.lines_move.append("                                   ((")
        self.lines_move.append("                                   ))")
        self.lines_move.append("                                   ((")
        self.lines_move.append("                                   )(")

        # finish label
        self.lines_end = []
        self.lines_end.append("                                   ^ ")
        self.lines_end.append("                            Complete!!")
        self.lines_end.append("                                     ")
        self.lines_end.append("                                     ")
        self.lines_end.append("                                     ")
        self.lines_end.append("                                     ")

        # Label line number assertion (Debug)
        #assert len(self.lines_move) == len(self.lines_end), "The number of lines in the moving label and finish label do not match."
        
        # set the movement
        self.label_python_move = [tk.Label(text="") for _ in range(len(self.lines_move))]
        cnt_y_margin = counter(self.place_y+self.y_margin*len(self.label_python), self.y_margin)
        for i in self.label_python_move:
            i.place(x=self.place_x, y=cnt_y_margin.result())
            cnt_y_margin.count()

    # progress start
    def progress_start(self):
        while self.flag_loop:
            try:
                time.sleep(self.sec)
                if self.flag_progress:
                    for i, j in enumerate(self.label_python_move):
                        if self.flag_loop:
                            j['text'] = self.lines_move[i]
                            time.sleep(self.sec)
                        else:
                            break
                else:
                    # all clear
                    for i in self.label_python_move:
                        if self.flag_loop:
                            i['text'] = ""
                        else:
                            break
                self.flag_progress = not self.flag_progress
            except Exception:
                # Avoid the Tkinter kill error.
                pass
                
        try:
            # progress finish
            for i, j in enumerate(self.label_python_move):
                j['text'] = self.lines_end[i]
        except Exception:
            # Avoid the Tkinter kill error.
            pass

    # thread start
    def start(self):
        self.thread_progress = threading.Thread(target = self.progress_start)
        self.thread_progress.setDaemon(True)
        self.thread_progress.start()

"""
    GUI Progressbar
    details: Main Calc (Deterministic processing)
"""
class Progressbar:
    def __init__(self, self_root, bar_x, bar_y, bar_len, i=100):
        self.set = tk.ttk.Progressbar(self_root, length=bar_len)
        self.set.configure(value=0, mode="determinate", maximum=i)
        self.set.place(x=bar_x, y=bar_y)

    # progress update
    def update(self, i):
        self.set.configure(value=i+1)
        self.set.update()

    # progress reset
    def reset(self):
        self.set.stop()

"""
    Progress Label
    details: Display the current processing content.
"""
class ProgressLabel:
    def __init__(self, place_x, place_y, text_ready=""):
        if text_ready == "":
            text_ready = "You can start the process..."
        self.label_progress = tk.Label(text=text_ready)
        self.label_progress.place(x=place_x, y=place_y)
        self.start = time.time()
        self.i = 0

    # label update
    def update(self, text_update=""):
        if self.i == 0:
            self.start = time.time()
        self.i += 1
        if text_update == "":
            text_update = str(self.i)

        # Not display when "character U + d4b53" exceeds the range allowed by Tcl (U + 0000-U + FFFF).
        try:
            self.label_progress['text'] = text_update
        except Exception as err:
            #print("error:")
            #print(err + "\n")
            try:
                self.label_progress['text'] = "There are too many characters to display."
            except Exception:
                # Avoid the Tkinter kill error.
                pass

    # label end
    def end(self, text_end="", flag_dt=False, flag_timer=False):
        self.i = 0
        if text_end == "":
            text_end = "You can start again..."
        dt_now = dt.datetime.now()
        self.label_progress['text'] = "{0}{1}{2}".format(
            text_end,
            "【End Datetime: {0}/{1}/{2} | {3}:{4}:{5}】".format(
                dt_now.year,
                dt_now.month if dt_now.month >= 10 else "0" + str(dt_now.month),
                dt_now.day if dt_now.day >= 10 else "0" + str(dt_now.day),
                dt_now.hour if dt_now.hour >= 10 else "0" + str(dt_now.hour),
                dt_now.minute if dt_now.minute >= 10 else "0" + str(dt_now.minute),
                dt_now.second if dt_now.second >= 10 else "0" + str(dt_now.second)
            ) if flag_dt else "",
            "【Operating Time: {}s】".format(time.time() - self.start) if flag_timer else ""
        )

"""
    Moving Progress Label
"""
class MoveProgressLabel:
    def __init__(self, place_x, place_y, text_len=10, text_ready=""):
        if text_ready == "":
            text_ready = "   Ready.   "
        self.flag_loop = False
        self.text_len = text_len
        self.yl = yajirushi_left()
        self.yr = yajirushi_right()
        self.set = ProgressLabel(
            place_x,
            place_y,
            next(self.yl) * self.text_len + text_ready + next(self.yr) * self.text_len
        )

    # moving label end
    def end(self, text_end=""):
        if text_end == "":
            text_end = "   Finish   "
        self.yl = yajirushi_left()
        self.yr = yajirushi_right()
        self.set.end(next(self.yl) * self.text_len + text_end + next(self.yr) * self.text_len)

    # progress start
    def progress_start(self, text_update):
        while self.flag_loop:
            self.set.update(next(self.yl) * self.text_len + text_update + next(self.yr) * self.text_len)
            time.sleep(0.1)

    # thread start
    def start(self, text_update=""):
        if text_update == "":
            text_update = " Processing "
        self.thread_progress = threading.Thread(target = self.progress_start, args=(text_update,))
        self.thread_progress.setDaemon(True)
        self.thread_progress.start()
    
# yajirushi generator left
def yajirushi_left():
    i = 0
    while 1:
        yield ">>>=<<<="[i % 8]
        i += 1

# yajirushi generator right
def yajirushi_right():
    i = 0
    while 1:
        yield "<<<=>>>="[i % 8]
        i += 1

"""
    Tests
"""
if __name__ == "__main__":
    #from fwmodule_gui_progress import *

    """
    # widgets debug
    def debug_conf(ev):
        print(ev)
    """

    """
        GUI Test (Nondeterministic processing)
    """
    class ProcessingTarget:
        def __init__(self, place_x, place_y, num):
            self.receiver = ProgressReceiver(place_x, place_y)
            self.label_progress = ProgressLabel(place_x+80, place_y-25)
            self.num = num      # test variable
            
        def target(self):
            while self.receiver.flag_loop:
                print("num : ", self.num)
                # If there is 1 second, it will not end in the middle.
                #time.sleep(1)
                # Split↓
                # Since the processing is heavy, it is actually about 1.1 seconds.
                for i in range(5):
                    if self.receiver.flag_loop:
                        time.sleep(0.2)
                    else:
                        break

            # handling target that do not loop
            # ▼▼▼▼▼▼
            #
            # ※processing contents※
            #
            self.receiver.flag_loop = False
            # ▲▲▲▲▲▲
            
        def start(self):
            self.thread_target = threading.Thread(target = self.target)
            self.thread_target.setDaemon(True)
            self.thread_target.start()

    class GuiApplication(tk.Frame):
        def __init__(self, master=None):
            window_width = 630
            window_height = 500
            super().__init__(master, width=window_width, height=window_height)
            self.master = master
            self.master.title("GUI Test (Nondeterministic processing)")
            self.master.minsize(window_width, window_height)
            self.pack()
            #self.bind('<Configure>', debug_conf)
            self.target = ProcessingTarget(place_x=350, place_y=50, num=1)
            self.create_widgets()
            
        def create_widgets(self):
            self.button_start = tk.ttk.Button(self, text="START", padding=10, command=self.start_event)
            self.button_start.place(x=100, y=100)
            self.button_change = tk.ttk.Button(self, text="CONV", padding=10, command=self.change_event)
            self.button_change.place(x=100, y=225)
            self.button_end = tk.ttk.Button(self, text="END", padding=10, command=self.end_event)
            self.button_end.place(x=100, y=350)
            
        def start_event(self):
            if not self.target.receiver.flag_loop:
                print("Started")
                self.target.receiver.flag_loop = True
                self.target.receiver.flag_progress = False
                self.target.receiver.start()
                self.target.start()
                self.target.label_progress.update("num : {}".format(self.target.num))
                
        def change_event(self):
            self.target.num += 1
            self.target.label_progress.update("num : {}".format(self.target.num))
            
        def end_event(self):
            if self.target.receiver.flag_loop:
                self.target.receiver.flag_loop = False
                self.target.receiver.flag_progress = False
                self.target.label_progress.end()
                print("Finished")
                
        def kill_tkinter(self):
            self.target.receiver.flag_loop = False
            print("Tkinter killed")
    
    # run application
    print("GUI1 running...")
    window = tk.Tk()
    app1 = GuiApplication(master=window)
    app1.mainloop()
    print("GUI1 ended...")
    
    if app1.target.receiver.flag_loop:
        app1.kill_tkinter()

    """
        GUI Test (Deterministic processing)
    """
    class ProcessingTarget:
        def __init__(self, self_root, bar_x, bar_y, bar_len):
            self.flag_running = False
            self.progressbar = Progressbar(self_root, bar_x, bar_y, bar_len)
            
        def target(self):
            print("Started")
            self.flag_running = True
            
            # processing contents
            # ▼▼▼▼▼▼
            len = 200
            self.progressbar.set.configure(maximum=len)
            for i in range(len):
                self.progressbar.update(i)
                time.sleep(0.01)
            # ▲▲▲▲▲▲
            
            self.flag_running = False
            print("Finished")
            
        def start(self):
            self.thread_target = threading.Thread(target = self.target)
            self.thread_target.setDaemon(True)
            self.thread_target.start()
            
    class GuiApplication(tk.Frame):
        def __init__(self, master=None):
            window_width = 335
            window_height = 150
            super().__init__(master, width=window_width, height=window_height)            
            self.master = master
            self.master.title("GUI Test (Deterministic processing)")
            self.master.minsize(window_width, window_height)
            self.pack()
            #self.bind('<Configure>', debug_conf)
            self.target = ProcessingTarget(self, bar_x=10, bar_y=30, bar_len=315)
            self.create_widgets()
            
        def create_widgets(self):
            self.start_button = tk.ttk.Button(self, command=self.start_event, text="START")
            self.start_button.place(x=60, y=80)
            self.reset_button = tk.ttk.Button(self, command=self.reset_event, text="RESET")
            self.reset_button.place(x=195, y=80)
            
        def start_event(self):
            if not self.target.flag_running:
                self.target.start()
                
        def reset_event(self):
            self.target.progressbar.reset()
            
        def kill_tkinter(self):
            print("Tkinter killed")
    
    # run application
    print("GUI2 running...")
    window = tk.Tk()
    app2 = GuiApplication(master=window)
    app2.mainloop()
    print("GUI2 ended...")
    
    if app2.target.flag_running:
        app2.kill_tkinter()
        

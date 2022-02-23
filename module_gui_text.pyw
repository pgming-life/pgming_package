"""module_gui_text.pyw"""

import collections as cl

is_release = False

try:
    import practical_package.release as r
except Exception:
    pass
else:
    is_release = r.is_release
   
if is_release:
    from practical_package.fwmodule_gui_progress import *
    from practical_package.charcode import *
else:
    # variable route path control for VSCode debug
    import sys, os
    if not [i for i in sys.path if i == os.path.dirname(__file__)]:
        sys.path.append(os.path.dirname(__file__))
    from fwmodule_gui_progress import *
    from charcode import *

"""
    Folder Create
    details: Checking and creating a folder.
    ex) folder_create("[folder path]")
"""
def folder_create(path_folder):
    text_gui = ""

    is_none = False
    if not os.path.exists(path_folder):
        is_none = True
    else:
        text_gui = "Checked a folder. " + path_folder
       
    if is_none:
        os.makedirs(path_folder, exist_ok=True)
        text_gui = "Created a folder. " + path_folder
       
    result = cl.namedtuple('result', 'is_ok, text')
    return result(is_ok=False if is_none else True, text=text_gui)

"""
    File Create
    details: Checking and creating a file.
    ex) file_create("[file path]", list([text in file]), '[encoding name]')
"""
def file_create(path_file, string="", ecd=list_charcode[0]):
    text_gui = ""
   
    is_none = False
    if not os.path.exists(path_file):
        is_none = True
    else:
        text_gui = "Checked a file. " + path_file
       
    if is_none:
        with open(path_file, 'w', encoding=ecd) as f:
            if type(string) is str:
                f.write(string)
            else:   # lines list
                for i, j in enumerate(string):
                    if i != len(string) - 1:
                        f.writelines("{}\n".format(j))
                    else:
                        f.writelines("{}".format(j))
        text_gui = "Created a file. " + path_file
       
    result = cl.namedtuple('result', 'is_ok, text')
    return result(is_ok=False if is_none else True, text=text_gui)

"""
    Path Search - Warnning End
    details: Checking a folder and file.
    ex) path_search_end("[folder path | file path]")
"""
def path_search_end(path):
    text_gui = ""
   
    is_none = False
    if not os.path.exists(path):
        is_none = True
    else:
        text_gui = "Checked. " + path
       
    if is_none:
        text_gui = "There is none... End the process. " + path
       
    result = cl.namedtuple('result', 'is_ok, text')
    return result(is_ok=False if is_none else True, text=text_gui)

"""
    Path Search - Warnning Continue
    details: Checking the folder or file.
    ex) path_search_continue("[folder path | file path]")
"""
def path_search_continue(path):
    text_gui = ""
   
    is_none = False
    if not os.path.exists(path):
        is_none = True
    else:
        text_gui = "Checked. " + path
       
    if is_none:
        text_gui = "None. However, processing continues. " + path
       
    result = cl.namedtuple('result', 'is_ok, text')
    return result(is_ok=False if is_none else True, text=text_gui)

"""
    Read
    details: Read the entire contents of the file as all string.
    ex) file_read("[file path]", '[encoding name]')
"""
def file_read(path_file, ecd=''):
    is_none = False
    text_gui = ""
    text = []
   
    if ecd:
        try:
            with open(path_file, 'r', encoding=ecd) as f:
                text = f.read()
        except Exception:
            pass
       
    if not ecd:
        # brute force
        for i, j in enumerate(list_charcode):
            try:
                with open(path_file, 'r', encoding=j) as f:
                    text = f.read()
            except Exception as err:
                #print("\n{}, file open error".format(j))
                #print("{}\ncontinue...".format(err))
                if i == len(list_charcode) - 1:
                    is_none = True
                    text_gui = "Cannot be read. " + path_file
            else:
                ecd = j
                break
               
    result = cl.namedtuple('result', 'is_ok, encoding, text, data')
    return result(is_ok=False if is_none else True, encoding=ecd, text=text_gui, data=text)

"""
    Read Lines
    details: Read the entire contents of the file as a line list.
    ex) file_readlines("[file path]", '[encoding name]')
"""
def file_readlines(path_file, ecd=''):
    is_none = False
    text_gui = ""
    lines = []
   
    if ecd:
        try:
            with open(path_file, 'r', encoding=ecd) as f:
                data = f.read()
                for line in data.split("\n"):
                    lines.append(line)
        except Exception:
            pass
       
    if not ecd:
        # brute force
        for i, j in enumerate(list_charcode):
            try:
                with open(path_file, 'r', encoding=j) as f:
                    data = f.read()
                    for line in data.split("\n"):
                        lines.append(line)
            except Exception as err:
                #print("\n{}, file open error".format(j))
                #print("{}\ncontinue...".format(err))
                if i == len(list_charcode) - 1:
                    is_none = True
                    text_gui = "Cannot be read. " + path_file
            else:
                ecd = j
                break
   
    result = cl.namedtuple('result', 'is_ok, encoding, text, line')
    return result(is_ok=False if is_none else True, encoding=ecd, text=text_gui, line=lines)

"""
    String Control
    ex) obj=string_pick(lines_list("[string]", "[file path]")[i])
"""
class string_pick:
    def __init__(self, line):
        self.line = line
       
    """
        Pick Strings
        ・s: start position
        ・t: shift
        ・u: number of strings
        ・is_u_strnum=False: the number of strings where the start position of "u" is 0
        ・is_u_strnum=True: the number of strings where the start position of "u" is "+s" and "+t"
        ex) obj.pick("[string1]", s, t, u=obj.set("[string2]", m, n))
    """
    def pick(self, string, s=None, t=None, u=None, is_u_strnum=False):
        s = self.line.find(string, s) if s is not None else self.line.find(string)
        if t is not None:
            if u is not None:
                if is_u_strnum:
                    t += s
                    u += t
                    name_string = self.line[t:u]
                else:
                    t += s
                    name_string = self.line[t:u]
            else:
                t += s
                name_string = self.line[t:]
        elif u is not None:
            if is_u_strnum:
                u += s
                name_string = self.line[s:u]
            else:
                name_string = self.line[s:u]
        else:
            name_string = self.line[s:]
        return name_string
   
    """
        Search Settings - Return Number or Strings
        ・m: start position
        ・n: strings of "n" pieces
        * Used for "s", "t", "u" (other than that: ex) string[obj.set("[string1]", m, n):obj.set("[string2]", m, n)])
        * When used for "u" ⇒ is_u_strnum=False
        * 0 pieces is 1 piece
        * Return -1 if there is no strings of "n" pieces
        ex1) obj.set("[string]", m, n)
    """
    def set(self, string, m=None, n=1):
        m = self.line.find(string, m) if m is not None else self.line.find(string)
        for _ in range(1, n): m = self.line.find(string, m + 1)
        return m

"""
    Lines List
    details:
        Search the specified file from the input character string
        and get the line number and line list where the character string is located.
    ex) lines_list("[string]", "[file path]", '[encoding name]')  
"""
def lines_list(string, path_file, ecd=''):
    is_none = False
    text_gui = ""
    text = ""
   
    if ecd:
        try:
            with open(path_file, 'r', encoding=ecd) as f:
                text = f.read()
        except Exception as err:
            pass
       
    if not ecd:
        # brute force
        for i, j in enumerate(list_charcode):
            try:
                with open(path_file, 'r', encoding=j) as f:
                    text = f.read()
            except Exception as err:
                #print("\n{}, file open error".format(j))
                #print("{}\ncontinue...".format(err))
                if i == len(list_charcode) - 1:
                    is_none = True
                    text_gui = "Cannot be read. " + path_file
            else:
                ecd = j
                break

    list_num_line = []
    list_num_char = []
    list_line = []
    if not is_none:
        lines = file_readlines(path_file, ecd if ecd else '').line
        num_line = 0
        for line in text.splitlines():
            num_line += 1
            cnt = 1
            if line != "":
                s = string_pick(line)
                for _ in range(len(line)):
                    num_char = s.set(string, 0, cnt)
                    if num_char == -1:
                        break
                    list_num_line.append(num_line)
                    list_num_char.append(num_char)
                    cnt += 1
        for num in list_num_line:
            list_line.append(lines[num - 1])
   
    result = cl.namedtuple('result', 'is_ok, encoding, text, num_line, num_char, line')
    return result(is_ok=False if is_none else False if list_num_line == [] else True, encoding=ecd, text=text_gui, num_line=list_num_line, num_char=list_num_char, line=list_line)

"""
    Tests
"""
if __name__ == "__main__":
    #from module_gui_text import *

    """
    # widgets debug
    def debug_conf(ev):
        print(ev)
    """
   
    # test medium
    path_folder = "{}\\__pycache__".format(os.path.dirname(__file__))
    path_file = "{}\\test_text.cpp".format(os.path.dirname(__file__))
    string0 = "//"
    string1 = "return"
    string2 = "FAILED"
   
    try:
        subprocess.run(r"explorer {}".format(path_file))
    except Exception:
        pass
   
    class ProcessingTarget:
        def __init__(self, progress_x, progress_y, label_x, label_y):
            self.receiver = ProgressReceiver(progress_x, progress_y)
            self.label_progress = ProgressLabel(label_x, label_y)
           
        def target(self):
            # folder_create
            self.label_progress.update(folder_create(path_folder).text)
           
            time.sleep(.2)

            # file_create
            self.label_progress.update(file_create(path_file).text)
            time.sleep(.2)

            # path_search_end
            self.label_progress.update(path_search_end(path_file).text)
            time.sleep(.2)

            # path_search_continue
            self.label_progress.update(path_search_continue(path_file).text)
            time.sleep(.2)

            # file_readlines
            is_ok, encoding, text, lines = file_readlines(path_file)
            self.label_progress.update(is_ok)
            time.sleep(.2)
            self.label_progress.update(encoding)
            time.sleep(.2)
            self.label_progress.update(text)
            time.sleep(.2)
            for i in lines:
                self.label_progress.update(i)
                time.sleep(.02)

            # lines_list
            is_ok, encoding, text, list_num_line, list_num_char, list_line = lines_list(string0, path_file)
            self.label_progress.update(is_ok)
            time.sleep(.2)
            self.label_progress.update(encoding)
            time.sleep(.2)
            self.label_progress.update(text)
            time.sleep(.2)
            for num_line, num_char, line in zip(list_num_line, list_num_char, list_line):
                self.label_progress.update(num_line)
                time.sleep(.02)
                self.label_progress.update(num_char)
                time.sleep(.02)
                self.label_progress.update(line)
                time.sleep(.02)

            # string_pick
            list = lines_list(string1, path_file)
            for i in list.line:
                s = string_pick(i)
                name_string = i[s.set(string1):s.set(";")] if s.set(";") != -1 else i[s.set(string1):]
                self.label_progress.update(name_string)
                time.sleep(.2)
                name_string = s.pick(string1, None, len(string1)+1, s.set(";"))
                self.label_progress.update(name_string)
                time.sleep(.2)
                name_string = s.pick(string1, None, len(string1)+1, 1, is_u_strnum=True)
                self.label_progress.update(name_string)
                time.sleep(.2)

            # string_pick - read function arguments recursively
            list = lines_list(string2, path_file)
            for i in list.line:
                s = string_pick(i)
                func_or_val = s.pick("(", s.set(string2), 1, s.set("(", s.set(string2), 2) if s.set("(", s.set(string2), 2) != -1 else s.set(")"))
                self.label_progress.update("Name: " + func_or_val)
                time.sleep(.2)
                if s.set("(", s.set(string2), 2) != -1:
                    m = string_pick(s.pick("(", s.set(s.pick("(", s.set(string2), 1, s.set("(", s.set(string2), 2)))))
                    args = m.pick("(", None, 1, m.set(")", None, m.pick("").count("(")))
                    self.label_progress.update("Args: " + args)
                    time.sleep(.2)
                    if "," in args:
                        n = string_pick(args)
                        for j in range(1, len(args)):
                            arg = args[(0 if j == 1 else n.set(",", None, j-1) + 1):(n.set(",", None, j) if n.set(",", None, j) != -1 else len(args))]
                            self.label_progress.update("Arg: " + arg.strip())
                            time.sleep(.2)
                            if n.set(",", None, j) == -1:
                                break
                        """
                        for j in args.split(","):
                            self.label_progress.update("Arg:  " + j.strip())
                            time.sleep(0.2)
                        """
                       
            self.receiver.is_loop = False
            self.label_progress.end("", is_dt=True, is_timer=True)
           
        def start(self):
            self.thread_target = threading.Thread(target = self.target)
            self.thread_target.setDaemon(True)
            self.thread_target.start()
           
    class GuiApplication(tk.Frame):
        def __init__(self, master=None):
            window_width = 900
            window_height = 500
            super().__init__(master, width=window_width, height=window_height)
            self.master = master
            self.master.title("GUI Text Processing Test")
            self.master.minsize(window_width, window_height)
            self.pack()
            #self.bind('<Configure>', debug_conf)
            self.target = ProcessingTarget(progress_x=350, progress_y=50, label_x=100, label_y=20)
            self.create_widgets()
           
        def create_widgets(self):
            self.button_start = tk.ttk.Button(self, text="START", padding=10, command=self.start_event)
            self.button_start.place(x=100, y=100)
           
        def start_event(self):
            if not self.target.receiver.is_loop:
                self.target.receiver.is_loop = True
                self.target.receiver.is_progress = False
                self.target.receiver.start()
                self.target.start()
   
    # run application
    window = tk.Tk()
    app = GuiApplication(master=window)
    app.mainloop()
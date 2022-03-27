"""module_console_text.py"""

import collections as cl

is_release = False

try:
    import practical_package.release as r
except Exception:
    pass
else:
    is_release = r.is_release

if is_release:
    from practical_package.fwmodule_console_progress import *
    from practical_package.charcode import *
else:
    # variable route path control for VSCode debug
    import sys, os
    if not [i for i in sys.path if i == os.path.dirname(__file__)]:
        sys.path.append(os.path.dirname(__file__))
    from fwmodule_console_progress import *
    from charcode import *

"""
    Folder Create
    details: Checking and creating a folder.
    ex) folder_create("[folder path]")
"""
def folder_create(path_folder: str) -> bool:
    is_none = False
    if not os.path.exists(path_folder):
        is_none = True
    else:
        print("Checked a folder. " + path_folder)
        
    if is_none:
        input("\nThere is no folder. {}\nDo you want to create a folder?\nCreate when the Enter key is pressed...".format(path_folder))
        os.makedirs(path_folder, exist_ok=True)
        print("Created a folder. " + path_folder)
    
    return False if is_none else True

"""
    File Create
    details: Checking and creating a file.
    ex) file_create("[file path]", list([lines in file]), '[encoding name]') 
"""
def file_create(path_file: str, string="", ecd=list_charcode[0]) -> bool:
    is_none = False
    if not os.path.exists(path_file):
        is_none = True
    else:
        print("Checked a file. " + path_file)
        
    if is_none:
        input("\nThere is no file. {}\nDo you want to create a file?\nCreate when the Enter key is pressed...".format(path_file))
        with open(path_file, 'w', encoding=ecd) as f:
            if type(string) is str:
                f.write(string)
            else:   # lines list
                for i, j in enumerate(string):
                    if i != len(string) - 1:
                        f.wirtelines("{}\n".format(j))
                    else:
                        f.writelines("{}".format(j))
        print("Created a file. " + path_file)

    return False if is_none else True

"""
    Path Search - Warnning End
    details: Checking the folders and files.
    ex) path_search_end("[folder path]", "[folder path]", "[file path]", ・・・)
"""
def path_search_end(*args: str, **kwargs: str) -> "exit":
    list_none = []
    for i in args:
        if not os.path.exists(i):
            list_none.append(i)
        else:
            print("Checked. " + i)
    for i in kwargs:
        if not os.path.exists(i):
            list_none.append(i)
        else:
            print("Checked. " + i)
            
    if list_none != []:
        print()
        for i in list_none:
            print("There is no... " + i)
        input("Please confirm.\nEnd the process. Please close this window.\nCloses the window when the Enter key is pressed...")
        sys.exit()

"""
    Path Search - Warnning Continue
    details: Checking the folder or file.
    ex) path_search_continue("[folder path | file path]")
"""
def path_search_continue(path: str) -> bool:
    is_none = False
    if not os.path.exists(path):
        is_none = True
    else:
        print("Checked. " + path)
        
    if is_none:
        print("\nThere is no... " + path)
        input("Do you want to continue processing?\nContinues when the Enter key is pressed...")
        
    return False if is_none else True

"""
    Read
    details: Read the entire contents of the file as all string.
    ex) file_read("[file path]", '[encoding name]')
"""
def file_read(path_file: str, ecd='') -> cl.namedtuple:
    is_none = False
    text = ""

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
                    print("Cannot be read. " + path_file)
            else:
                ecd = j
                break
               
    result = cl.namedtuple('result', 'is_ok, encoding, data')
    return result(is_ok=False if is_none else True, encoding=ecd, data=text)

"""
    Read Lines
    details: Read the entire contents of the file as a line list.
    ex) file_readlines("[file path]", '[encoding name]')
"""
def file_readlines(path_file: str, ecd='') -> cl.namedtuple:
    is_none = False
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
                    print("Cannot be read. " + path_file)
            else:
                ecd = j
                break
    
    result = cl.namedtuple('result', 'is_ok, encoding, line')
    return result(is_ok=False if is_none else True, encoding=ecd, line=lines)

"""
    String Control
    ex) obj=string_pick(lines_list("[string]", "[file path]")[i])
"""
class string_pick:
    def __init__(self, line: str):
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
    def pick(self, string: str, s=None, t=None, u=None, is_u_strnum=False) -> str:
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
        ex) obj.set("[string]", m, n)
    """
    def set(self, string: str, m=None, n=1) -> int:
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
def lines_list(string: str, path_file: str, ecd='') -> cl.namedtuple:
    is_none = False
    text = ""
    
    if ecd:
        try:
            with open(path_file, encoding=ecd) as f:
                text = f.read()
        except Exception:
            pass
        
    if not ecd:
        # brute force
        for i, j in enumerate(list_charcode):
            try:
                with open(path_file, encoding=j) as f:
                    text = f.read()
            except Exception as err:
                #print("\n{}, file open error".format(j))
                #print("{}\ncontinue...".format(err))
                if i == len(list_charcode) - 1:
                    is_none = True
                    print("Cannot be read. " + path_file)
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
    
    result = cl.namedtuple('result', 'is_ok, encoding, num_line, num_char, line')
    return result(is_ok=False if is_none else False if list_num_line == [] else True, encoding=ecd, num_line=list_num_line, num_char=list_num_char, line=list_line)

"""
    Tests
"""
if __name__ == "__main__":
    #from module_console_text import *

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

    @main_decorator
    def main_func() -> None:
        # folder_create
        folder_create(path_folder)

        # file_create
        file_create(path_file)

        # path_search_end
        path_search_end(path_file)

        # path_search_continue
        is_ok = path_search_continue(path_file)
        print("result: " + str(is_ok))
        python_connection()

        # file_read
        root = file_read(path_file)
        for i in root:
            print(i)
        python_connection()

        # file_readlines
        root = file_readlines(path_file)
        for i in root:
            print(i)
        python_connection()
        
        # lines_list
        root = lines_list(string0, path_file)
        print(root.is_ok)
        print(root.encoding)
        for num_line, num_char, line in zip(root.num_line, root.num_char, root.line):
            print(num_line)
            print(num_char)
            print(line)
        python_connection()

        # string_pick
        root = lines_list(string1, path_file)
        for i in root.line:
            s = string_pick(i)
            print("----------------------")
            name_string = i[s.set(string1):(s.set(";") if s.set(";") != -1 else len(i))]
            print(name_string)
            name_string = s.pick(string1, None, len(string1)+1, s.set(";"))
            print(name_string)
            name_string = s.pick(string1, None, len(string1)+1, 1, is_u_strnum=True)
            print(name_string)
        print("----------------------")
        python_connection()
        
        # string_pick - read function arguments recursively
        root = lines_list(string2, path_file)
        for i in root.line:
            s = string_pick(i)
            func_or_val = s.pick("(", s.set(string2), 1, s.set("(", s.set(string2), 2) if s.set("(", s.set(string2), 2) != -1 else s.set(")"))
            print("----------------------")
            print("Name: " + func_or_val)
            if s.set("(", s.set(string2), 2) != -1:
                m = string_pick(s.pick("(", s.set(s.pick("(", s.set(string2), 1, s.set("(", s.set(string2), 2)))))
                args = m.pick("(", None, 1, m.set(")", None, m.pick("").count("(")))
                print("Args: " + args)
                if "," in args:
                    n = string_pick(args)
                    for j in range(1, len(args)):
                        arg = args[(0 if j == 1 else n.set(",", None, j-1) + 1):(n.set(",", None, j) if n.set(",", None, j) != -1 else len(args))]
                        print("Arg:  " + arg.strip())
                        if n.set(",", None, j) == -1:
                            break
                    """
                    for j in args.split(","):
                        print("Arg:  " + j.strip())
                    """
        print("----------------------")

    # execute
    main_func()
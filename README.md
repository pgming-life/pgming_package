# Python Practical Package &middot; [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/pgming-life/pgming_package/blob/main/LICENSE)

This package is a practical python package.
Also, this package mainly specialize in string analysis.

## Packed module contents: :nine:

* CUI control
* GUI application (Tkinter)
* Progress function
* Path search
* Folder and file create
* File read
* Text processing
* Bit conversion
* EXE release mode

## How to use:

<pre>
Directory Tree
[project]
    ├── practical_package
    |       ├── .gitignore
    |       ├── LICENSE
    |       ├── README.md
    |       ├── __init__.py
    |       ├── ・・・.py
    |
    └── main.py
</pre>

```python
"""main.py"""
from practical_package import [module name] as hoge

# use method
hoge.[method]

# instance generation
fuga = hoge.[class]
```

## [UI Creator](https://pgming-ui-creator.com) for GUI application:

**Repository-> pgming-life/[ui-creator](https://github.com/pgming-life/ui-creator)**

![tkinter](https://user-images.githubusercontent.com/84230279/125622613-4f06ffbb-092e-4513-b3c7-42804c104e8a.PNG)

```python
"""Tkinter.pyw"""

import tkinter as tk
import tkinter.ttk
import tkinter.font as f
import math

# GUIアプリケーション
class GuiApplication(tk.Frame):
    # コンストラクタ
    def __init__(self, master=None):
        # ウィンドウサイズ
        window_width = 300
        window_height = 175

        # インプットボックス1
        self.inputbox1_width = 180
        self.inputbox1_height = 25
        self.inputbox1_x = 60
        self.inputbox1_y = 45

        # ボタン1
        self.button1_width = 80
        self.button1_height = 30
        self.button1_x = 110
        self.button1_y = 105

        # Frameクラスを継承
        super().__init__(
            master,
            width=window_width,
            height=window_height,
            )
        
        # 初期値代入
        self.master = master
        self.master.title("Tkinter")
        self.master.minsize(
            window_width,
            window_height,
            )
        self.pack()

        # インプットボックス1作成
        self.inputbox1_font = f.Font(
            family=u'MSゴシック',
            size=math.floor(self.inputbox1_height*0.5),
            )
        self.inputbox1 = tk.Entry(self)
        self.inputbox1.configure(
            font=self.inputbox1_font,
            )
        self.inputbox1.place(
            width=self.inputbox1_width,
            height=self.inputbox1_height,
            x=self.inputbox1_x,
            y=self.inputbox1_y,
            )

        # ボタン1作成
        self.button1 = tk.ttk.Button(
            self,
            text="Button1",
            )
        self.button1.place(
            width=self.button1_width,
            height=self.button1_height,
            x=self.button1_x,
            y=self.button1_y,
            )

# アプリケーション起動
window = tk.Tk()
app = GuiApplication(master=window)
app.mainloop()
```

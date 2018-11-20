import cx_Freeze
import sys
import matplotlib
import os
import subprocess
import tkinter
import youtube_dl

os.environ['TCL_LIBRARY'] = r"C:\ProgramData\Anaconda3\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\ProgramData\Anaconda3\tcl\tk8.6"


base=None
base="Win32GUI"

"""if sys.platform=='win32':
    base="Win32GUI"""
executables=[cx_Freeze.Executable("y.py",base=base,icon='y.ico')]


cx_Freeze.setup(
    name="youtube",
    options={"build_exe": {"packages":["tkinter","subprocess","os","sys","youtube_dl"],"include_files":["y.ico"]}},
    version="0.01",
    description="youtube videos download application",
    executables=executables
)
from http.server import executable
import cx_Freeze
import sys
import os
base=None

if sys.platform=='win32':
    base = "Win32GUI"
    
os.environ['TCL_LIBRARY'] = r""
os.environ['TK_LIBRARY'] = r""

executables = [cs_Freeze.Executable("main.py", base=base, icon="enc.ico")]


cx_Freeze.setup(name="Ficrypt", options={"build.exe": {"package":["tkinter","os","cryptography"]}})
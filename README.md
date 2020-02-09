# A few words...
This keylogger script has been written in Python, and developed using Python 3 language. The code included within this project includes snippets from multiple online resources and hence I do not own an exclusive right to it.
The program is intended for the use on the Windows OS, in order to run the keylogger on the Unix system, the file extension
needs to be changed from .pyw to .py

# How to use
It is necessary to ensure that we have Python and PIP package system installed on the machine, which the file is going to be executed on, before following any of the steps.

1. Clone the repository (https://www.github.com/pjedra96/python-chat) to a directory of your choice.
2. Ensure you have a Python platform installed on your system, along with PIP - the Python package manager
3. If not present on the system, install "pynput" and "logging" packages, using `pip install package_name`
4. Either execute the keylogger.pyw using the "python keylogger.pyw" command in the terminal (Windows and Linux), or simply double-click the keylogger.pyw file (Windows only and Unix with Desktop environment installed).

# Why the file extension .pyw?
The reason for using the .pyw extension, rather than the standard .py extension is that Python scripts (files with the extension .py) are executed by python.exe by default, with the terminal open (even if the executable is clicked), and the .pyw extension causes the script to be executed by pythonw.exe, which runs without a terminal window.
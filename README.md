# SimpleKeyLogger Overview
A desktop-base application that records the real time activity of a computer user including the keystrokes entered into PC
# Features
Record all the applications running on the targeted computer and the text typed in these applications using python modules: pyWin32 and pyHook
Suppressing the terminal window on startup and runs the program in the background 
Perform input validation, including removing characters when backspace is pressed and ignoring non-character input (Shift, Control,Tab, etc) to achieve comprehensive final output
Saves logs on a date-specific file on the local hard drive
# Technical
pyHook: provides callbacks for global mouse and keyboard events in Windows.
pywin32: A set of extension modules that provides access to many of the Windows API functions. 
# Future improvements
Future improvements include the ability to save logs to a remote database or send logs by email, combined with the visual record (screenshots taken periodically) to provide full control over the computer

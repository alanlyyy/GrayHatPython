from ctypes import *
from my_debugger_defines import *

kernel31 = windll.kernel32

class debugger():
    
    def __init__(self):
        pass
        
    
    def load(self, path_to_exe):
        
        #dwCreation flag determines how to create the process
        #set creation_flags = CREATE_NEW_CONSOLE if you want
        #to see the calculator GUI
        
        creation_flags = DEBUG_PROCESS
        
        #instantiate the structs from my_debugger_defines.py
        startupinfo = STARTUPINFO()
        process_information= PROCESS_INFORMATION()
        
        #The following two options allow the started process
        #to be shown as separate window. This also illustrates
        #how different settings in the STARTUPINFO struct can affect
        #the debuggee
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0
        
        #We then initialize the cb variable in the STARTUPINFO struct
        #which is just the size ofthe struct itself
        startupinfo.cd = sizeof(startupinfo)
        
        if kernel32.CreateProcessA(path_to_exe,
                                                        None,
                                                        None,
                                                        None,
                                                        None,
                                                        creation_flags,
                                                        None,
                                                        None,
                                                        byref(startupinfo),
                                                        byref(process_information)):
            
            print( "[*] We have successfully launched the process!")
            print("[*] PID:%d" % process_information.dwProcessId)
            
        else:
            print("[*] Error: 0x%o8x." %kernel32.GetLastError())
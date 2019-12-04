#arrange.py
#Arranges the fiels according to their types for later classification
#uses shutil, os

import os
import shutil
import sys
from pchealth import system_health as sysinfo
#Imports class system_health as sysinfo from the module pchealth


def makeFolders(f):
    if f in os.listdir():
        return
    os.mkdir(f'.\\{f}')

makeFolders('PDF')
makeFolders('Images')
makeFolders('Videos')
makeFolders('Audios')
makeFolders('Programs')
makeFolders('Docs')

def strong_arrange():
        for foldername, subfolders, filenames in os.walk(folder):
            for file in filenames:
                if file.lower().endswith('.pPDF') or file.lower().endswith('.PDF'):
                        print(file)
                        shutil.move(file,'.\\PDF')
                elif file.lower().endswith('png') or file.lower().endswith('jpg') or file.lower().endswith('jpeg') or file.lower().endswith('gif'):
                    print(file)
                    shutil.move(file,'.\\Images')
                elif file.lower().endswith('.mp4') or file.lower().endswith('.mkv') or file.lower().endswith('.avi') or file.lower().endswith('.3gp'):
                    print(file)
                    shutil.move(file,'.\\Videos')
                elif file.lower().endswith('.mp3') or file.lower().endswith('.wav'):
                    print(file)
                    shutil.move(file,'.\\Audios')
                elif file.lower().endswith('.exe'):
                    print(file)
                    shutil.move(file,'.\\Programs')
                elif file.lower().endswith('.ios'):
                    print(file)
                    shutil.move(file,'.\\Ios Files')
                elif (file.lower().endswith('.docx') or file.lower().endswith('.doc') or
                file.lower().endswith('.xlsx') or file.lower().endswith('.xls') or
                file.lower().endswith('.txt') or file.lower().endswith('.csv') or
                file.lower().endswith('.pptx') or file.lower().endswith('.ppt')):
                    print(file)
                    shutil.move(file,'.\\Docs')
         

def arrange():
    for file in os.listdir(folder):
        if file.lower().endswith('.pdf') :
            print(file)
            shutil.move(file,'.\\PDF')
        elif file.lower().endswith('png') or file.lower().endswith('jpg') or file.lower().endswith('jpeg') or file.lower().endswith('gif'):
            print(file)
            shutil.move(file,'.\\Images')
        elif file.lower().endswith('.mp4') or file.lower().endswith('.mkv') or file.lower().endswith('.avi') or file.lower().endswith('.3gp'):
            print(file)
            shutil.move(file,'.\\Videos')
        elif file.lower().endswith('.mp3') or file.lower().endswith('.wav'):
            print(file)
            shutil.move(file,'.\\Audios')
        elif file.lower().endswith('.exe'):
            print(file)
            shutil.move(file,'.\\Programs')
        elif file.lower().endswith('.ios'):
            print(file)
            shutil.move(file,'.\\Ios Files')
        elif (file.lower().endswith('.docx') or file.lower().endswith('.doc') or
        file.lower().endswith('.xlsx') or file.lower().endswith('.xls') or
        file.lower().endswith('.txt') or file.lower().endswith('.csv') or
        file.lower().endswith('.pptx') or file.lower().endswith('.ppt')):
            print(file)
            shutil.move(file,'.\\Docs')
 

def pcinfo():
    if sys.platform == "win32":
        sysinfo.userinfo()
        sysinfo.memory_info()
        sysinfo.virt_memory()
        sysinfo.batteryinfo()
        input()
        # To stop the window termination when
        # executed in command prompt 
    else:
        try:
            sysinfo.userinfo()
            sysinfo.memory_info()
            sysinfo.virt_memory()
            sysinfo.batteryinfo()
            sysinfo.system_temp()
            sysinfo.fan_speed()
            input()
            # To stop the window termination when
            # executed in command prompt 
        except:
            print("It can't be determined for the present OS")
        
 
if __name__ == '__main__':

    print("Arrange files")
    folder=os.getcwd()
    print(folder)

    choice = int(input("Press 1 for Weak arrange\nPress 2 for Strong arrange\nPress 3 for Pc Health and Info\nPress 0 to exit the program"))

    if choice==1:
        arrange()
    elif choice==2:
        strong_arrange()
    elif choice==3:
        pcinfo()
    elif choice==0:
        exit(0)
    

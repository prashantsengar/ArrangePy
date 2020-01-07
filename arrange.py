#arrange.py
#Arranges the fiels according to their types for later classification
#uses shutil, os

import os
import shutil

def makeFolders(f):
    if f in os.listdir():
        return
    os.mkdir(f'.\\{f}')

makeFolders('pPDF')
makeFolders('Pimages')
makeFolders('Pvideos')
makeFolders('Paudios')
makeFolders('Pprograms')
makeFolders('Pdocs')

def strong_arrange():
        for foldername, subfolders, filenames in os.walk(folder):
            for file in filenames:
                if file.lower().endswith('.pPDF'):
                        print(file)
                        shutil.move(file,'.\\pPDF')
                elif file.lower().endswith('png') or file.lower().endswith('jpg') or file.lower().endswith('jpeg') or file.lower().endswith('gif'):
                    print(file)
                    shutil.move(file,'.\\Pimages')
                elif file.lower().endswith('.mp4') or file.lower().endswith('.mkv') or file.lower().endswith('.avi') or file.lower().endswith('.3gp'):
                    print(file)
                    shutil.move(file,'.\\Pvideos')
                elif file.lower().endswith('.mp3') or file.lower().endswith('.wav') or file.lower().endswith('.flac'):
                    print(file)
                    shutil.move(file,'.\\Paudios')
         

def arrange():
    for file in os.listdir(folder):
        if file.lower().endswith('.pdf') :
            print(file)
            shutil.move(file,'.\\pPDF')
        elif file.lower().endswith('png') or file.lower().endswith('jpg') or file.lower().endswith('jpeg') or file.lower().endswith('gif'):
            print(file)
            shutil.move(file,'.\\Pimages')
        elif file.lower().endswith('.mp4') or file.lower().endswith('.mkv') or file.lower().endswith('.avi') or file.lower().endswith('.3gp'):
            print(file)
            shutil.move(file,'.\\Pvideos')
        elif file.lower().endswith('.mp3') or file.lower().endswith('.wav') or file.lower().endswith('.flac'):
            print(file)
            shutil.move(file,'.\\Paudios')
        elif file.lower().endswith('.exe'):
            print(file)
            shutil.move(file,'.\\Pprograms')
        elif (file.lower().endswith('.docx') or file.lower().endswith('.doc') or
        file.lower().endswith('.xlsx') or file.lower().endswith('.xls') or
        file.lower().endswith('.txt') or file.lower().endswith('.csv') or
        file.lower().endswith('.pptx') or file.lower().endswith('.ppt') or file.lower().endswith('.epub')):
            print(file)
            shutil.move(file,'.\\Pdocs')

def custom_arrange():
    a=input("enter the extention you want to locate file with")
    for files in os.listdir(folder):
        if files

if __name__ == '__main__':

    print("Arrange files")
    folder=os.getcwd()
    print(folder)

    choice = int(input("Press 1 for Weak arrange\nPress 2 for Strong arrange \nPress 3 for custom arrange\n0 to exit"))

    if choice==1:
        arrange()
    if choice==2:
        strong_arrange()
    if choice==3:
        custom_arrange()
    if choice==0:
        exit(0)
    

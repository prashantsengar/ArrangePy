# To move the files in a folder into certain placeholders according to the filetype they hold


import os
import shutil
import pandas as pd
import numpy as np

# initialising part

home_path = os.getcwd() # getting the current directory or rather the directory for our working

files = os.listdir(home_path) # the files and folders in the directory this program is being run in

extensions = [] # to store the total extensions found
folders = [] # to store the rest of the folders : other than the placeholders
already_folders = [] # to store the folders already there

dict1 = {} # the reference for the extensions to folder relation
my_topics = [] # to store the folder names that shall act as placeholders

# initialising the global variables

def initialise():
	global dict1
	# global df
	global my_topics
	global already_folders
	global extensions
	global folders
	global df

	files = os.listdir(home_path)

	dict1["media_files"] = np.array(['jpg', 'png', 'mp3', 'mp4'])
	dict1["text_files"] = np.array(['txt', 'md'])
	dict1["code_files"] = np.array(['cpp', 'py'])
	dict1["excel_files"] = np.array(['xlsx', 'csv'])
	dict1["pdf_files"] = np.array(['pdf', 'jsp'])
	# dict1["zips_1412"] = np.array(['zip', 'tar.xz'])
	my_topics = np.array([i for i in dict1.keys()])
	df = pd.DataFrame.from_dict(dict1, orient = 'index')
	# recognising the destination folders 
	for file in files:
		if len(file.split('.')) > 1:
			extensions.append(file.split('.')[-1])
		else:
			if file not in my_topics:
				folders.append(file)
			else:
				already_folders.append(file)

		# file_name, file_ext = os.path.splitext(file)

# to create the destination folders

def create_destinations():
	# making the my folders 
	# this way they are only made if they are not originally present in the parent folder
	for folder in my_topics:
		if folder not in already_folders:
			print(folder)
			os.mkdir(os.path.join(home_path, folder))
		else:
			pass

# to lookup for which container certain extension belongs

def lookup(df, ext):
	l = df[(df == ext).any(1)].index
	if len(l) == 0:
		return ""
	else:
		return l[0]

# to shift the files into the containers

def shift():
	global files
	global df

	for file in files:
		file_name, file_ext = os.path.splitext(file)
		if file_ext == "" or file == 'manage.py':
			pass
		else:
			dest = lookup(df, file_ext[1:])
			if dest != "":
				shutil.move(os.path.join(home_path, file),
					os.path.join(home_path, dest, file))
				# print(os.path.join(home_path, file) + 
				# 	os.path.join(home_path, dest, file))
				print("{} to {}, shifted succesfully!".format(file, dest))


if __name__ == '__main__':
	initialise()
	create_destinations()
	shift()
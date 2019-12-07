import os
import shutil
import pandas as pd
import numpy as np

# initialising part

home_path = os.getcwd()

files = os.listdir(home_path)

extensions = []
folders = []
my_folders = []

dict1 = {}
my_topics = []


def initialise():
	global dict1
	# global df
	global my_topics
	global my_folders
	global extensions
	global folders
	global df

	files = os.listdir(home_path)

	dict1["media_1410"] = np.array(['jpg', 'png', 'mp3', 'mp4'])
	dict1["text_1410"] = np.array(['txt', 'md'])
	dict1["code_1410"] = np.array(['cpp', 'py'])
	dict1["excel_1410"] = np.array(['xlsx', 'csv'])
	dict1["pdf_1410"] = np.array(['pdf', 'jsp'])
	# dict1["zips_1412"] = np.array(['zip', 'tar.xz'])

	df = pd.DataFrame.from_dict(dict1, orient = 'index')

	my_topics = ['media', 'text', 'code', 'excel', 'pdf']

	my_topics = ["{}_1410".format(topic) for topic in my_topics]
	# recognising the destination folders 
	for file in files:
		if len(file.split('.')) > 1:
			extensions.append(file.split('.')[-1])
		else:
			if file[-5:] == '_1410':
				my_folders.append(file)
			else:
			 folders.append(file)
		# file_name, file_ext = os.path.splitext(file)

def create_destinations():

	# making the my folders 
	# this way they are only made if they are not originally present in the parent folder
	for folder in my_topics:
		if folder not in my_folders:
			os.mkdir(os.path.join(home_path, folder))
		else:
			# print(f'{folder} is already there')
			pass

def lookup(df, ext):
	l = df[(df == ext).any(1)].index
	if len(l) == 0:
		return ""
	else:
		return l[0]

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
				print("{} shifted succesfully!".format(file))


if __name__ == '__main__':
	initialise()
	create_destinations()
	shift()

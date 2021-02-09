# ArrangePy
Organizes files in folders and helps you to clean your PC

- Join our Telegram group via the link given [below](#community)
- Read about it on my [blog](https://prashants.in/blog/CleanPy-python-script-to-organize-your-files/)


## What it does
Organizes the files based on their extensions in folders. 

If you run the script in a directory containing hundreds of files of multiple filetypes, the script will arrange all of them in different directories based on the file type. For example, all PDFs are arranged in a directory for PDFs, all document based files (docx, doc, xlsx, pptx etc) are moved to the **docs** directory. 

All these files are moved to a directory named **CleanedPy** in the directory on which the script was executed. So if you ran the script on your **Downloads** directory, a directory named *CleanedPy* will be created in **Downloads**.

You can specify which files to move to which directory using the config.ini file. 


## Features
Currently it has 2 modes

- Easy mode: Organzises files in the current directory
- Hard mode: Organizes files in the current directory and its subdirectories

## How to use

- `git clone https://github.com/prashantsengar/ArrangePy.git`
- `cd ArrangePy`

### Using the CLI (command-line interface)

```
usage: cli.py [-h] [-w | -s | -b] [-nw] [directory]

positional arguments:
  directory          The directory to arrange, default is current working
                     directory

optional arguments:
  -h, --help         show this help message and exit
  -w, --weak         Weak arrange
  -s, --strong       Strong arrange
  -b, --web          Run web GUI
  -nw, --no-warning  Don't show any warnings when running strong arrange
```

**Examples**

- `python cli.py` (Arranges current directory, asks for type of arrange [WEAK/STRONG] )
- `python cli.py -w` (Weak arranges current directory)
- `python cli.py -w PATH/TO/DIRECTORY` (Weak arranges given directory)


### Directly running the script

- `python main.py`

### Running the Web GUI

- `python -m webapp` # for the web interface
  * requires to install Flask for web interface. use `pip install flask` for the first time

### Editing the CONFIG file

Say the initial configuration is this:

```
[ext]
PDF=['pdf'],
Images=['png','jpeg','jpg','gif', 'tiff', 'psd', 'ico'],
```

This will move all PDF files to a directory named *PDF* and all images of mentioned extensions to a directory named *Images*.

#### To add a new file type 
(say .eps) to the *Images* directory, add the new extension to the Images list. So it will change to:

```
[ext]
PDF=['pdf'],
Images=['png','jpeg','jpg','gif', 'tiff', 'psd', 'ico', 'eps'],
```

#### To add a new type of file (new directory)
Say you want to move all the video files along with PDFs and images. You can do that in this way:

```
[ext]
PDF=['pdf'],
Images=['png','jpeg','jpg','gif', 'tiff', 'psd', 'ico', 'eps'],
Videos=['mp4','mkv','avi','3gp'],
```

Now it will arrange all mp4, mkv, avi, 3gp files to the Videos directory.


## Contributing

You can contribue to this project using multiple ways. Here are a few things that you can work on

- Improve this README to explain the idea better. GIFs can be added, for example.
- Adding extensions to the config.ini file will improve the experience for everyone. 
- Improve the code, add new features or fix [issues](https://github.com/prashantsengar/ArrangePy/issues/). 

Please read the [contribution guide](./CONTRIBUTING.md)

## Community 

Read the [contributing guide](./CONTRIBUTING.md)

Join the Telegram group for support and contributing. If you want to contribute, joining the group helps us all a lot because you can get instant feedback.

[<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/1024px-Telegram_logo.svg.png" alt="mTracker Telegram Group" width="150" height="150">](https://t.me/joinchat/INDdLlDf-SFDPURESGgdrQ)

# CleanPy
Organizes files in folders and helps you to clean your PC

## How to use
- `git clone https://github.com/prashantsengar/CleanPy.git`
- `cd CleanPy`
- `python arrange.py`
- It is Preferable to use PYW Files instead of PY Files to run it in the background with the Task Scheduler in Windows
  OS.
- PYW Files can be executed by the command `pythonw battery_notifier.pyw`, by this no command prompt is displayed with
  Task Scheduler.

## What it does
Organizes the files based on their extensions in folders. It notifies about Battery Status giving you it's stats along with a csv file in which usage stats are also recorded. The Time Notifier file notifies you to take breaks for every 20 minutes based on 20-20-20 rule by displaying a tkinter window box for 20 seconds with other options too along with displaying a quote.

### Features
Currently it has 2 modes

- Easy mode: Organzises files in the current directory
- Hard mode: Organizes files in the current directory and its subdirectories

## What's next

### Make it a complete cleaning suite by adding these features

- Add a feature to walk through the PC and get info about large files
- Find duplicate files in PC
- Get info about PC health
from flask import Flask,render_template
from arrange import arrange, strong_arrange
import webbrowser
import time
import os

app = Flask(__name__)

folder = os.getcwd()

@app.route('/')


def startingpage():
    folder_count = (len([1 for x in list(os.scandir(os.getcwd())) if x.is_dir()]))  # counting files and folders
    file_count = (len([1 for x in list(os.scandir(os.getcwd())) if x.is_file()]))
    directory = os.getcwd()
    total_items = folder_count + file_count
    print(directory)
    return render_template("index.html", nfol=folder_count, nfile=file_count, total=total_items, workdir=directory)


@app.route('/standardscan')


def stdScan():
    report = arrange()              # taking reports of the file transfer
    return render_template('completed.html', res=report)

@app.route('/deepscan')


def deepScan():
    report = strong_arrange()
    return render_template('completed.html', res=report)


if __name__ == '__main__':
    print("Running the program..")
    time.sleep(0.5)                             # Delay the run, to give the feeling of loading the app
    webbrowser.open('http://127.0.0.1:5000/')           # opened the browser before running app, cause
    app.run(debug=True)                                 # after running app, browser couldnot be automatically loaded

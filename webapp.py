from flask import Flask, render_template, request, redirect, url_for
import lib.arrange
import lib.utils
import webbrowser
import time
import os

app = Flask(__name__)


def startwork():
    ''' This will create folders to keep files according to their file types.  '''
    nonlocal destination
    destination = os.path.join(TARGET_FOLDER, RESULT_DIR)
    lib.utils.makeFolders(destination, FOLDER_TYPES.keys())

    
@app.route('/dashboard')


def dashboard():
    '''The page where the number of items present in the input location is given'''
    directory = TARGET_FOLDER
    folder_count = (len([1 for x in list(os.scandir(directory)) if x.is_dir()]))  # counting files and folders
    file_count = (len([1 for x in list(os.scandir(directory)) if x.is_file()]))
    total_items = folder_count + file_count
    return render_template("index.html", nfol=folder_count, nfile=file_count, total=total_items, workdir=directory)


@app.route('/input', methods=['POST', 'GET'])


def inputuser():
    '''Take the input of the address from HTML methods'''
    if request.method == 'POST':
        val = request.form['newaddress']
    else:
        val = request.args.get('newaddress')
    if os.path.isdir(val):
        nonlocal TARGET_FOLDER
        TARGET_FOLDER = str(val)
        return redirect(url_for('dashboard'))
    
    else:
        return render_template("error404.html")
    

@app.route('/changelocation')


def changingPage():
    '''Initiate and asks for the address as text input, where the app need to do the cleaning work'''
    return render_template('change.html')


@app.route('/standardscan')


def stdScan():
    '''Initiate the arrange function, and redirect to report page after the process is complete'''
    startwork()
    report = lib.arrange.weak_arrange(TARGET_FOLDER, destination, FOLDER_TYPES)              # taking reports of the file transfer
    return render_template('completed.html', res=report)


@app.route('/deepscan')


def deepScan():
    '''Initiate the strong arrange function, and redirect to the report page after the transfer is complete'''
    startwork()
    report = lib.arrange.strong_arrange(TARGET_FOLDER, destination, FOLDER_TYPES)
    return render_template('completed.html', res=report)


@app.route('/closetheapp')


def close():
    '''Turn the web server OFF '''
    shutdown_server()
    return 'Server shutting down..'


if __name__ == '__main__':
    print("Running the program..")
    time.sleep(0.5)                                                  # Delay the run, to give the feeling of loading the app
    webbrowser.open('http://127.0.0.1:5000/changelocation')          #open the webpage automatically
    app.run(debug=True)                                              

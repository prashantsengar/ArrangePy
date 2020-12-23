from flask import Flask, render_template, request, redirect, url_for
from main import RESULT_DIR, FOLDER_TYPES, TARGET_FOLDER
import lib.arrange
import lib.utils
import webbrowser
import time
import os

app = Flask(__name__)
destination = os.path.join(TARGET_FOLDER, RESULT_DIR)


def startwork():
    """Create folders to keep files according to their file types"""
    destination = os.path.join(TARGET_FOLDER, RESULT_DIR)
    lib.utils.makeFolders(destination, FOLDER_TYPES.keys())


@app.route('/dashboard/<address>')
def dashboard(address):
    """Scan the location for items"""
    dataPacket = {}
    Elements = list(os.scandir(address))
    dataPacket['folder_count'] = (len([1 for x in Elements if x.is_dir()]))
    dataPacket['file_count'] = (len([1 for x in Elements if x.is_file()]))
    dataPacket['total_items'] = len(Elements)
    dataPacket['address'] = address
    return render_template("index.html",data = dataPacket)


@app.route('/input', methods=['POST', 'GET'])
def inputuser():
    """Take the input of the address from HTML methods"""
    if request.method == 'POST':
        val = request.form['newaddress']
    else:
        val = request.args.get('newaddress')
    if os.path.isdir(val):
        TARGET_FOLDER = str(val)
        return redirect(url_for('dashboard', address=TARGET_FOLDER))
    return render_template("error404.html")


@app.route('/changelocation')
def changingPage():
    """Ask for the location to do the cleaning work"""
    return render_template('change.html')


@app.route('/dashboard/standardscan')
def standardScan():
    """Initiate the arrange and redirect to report page"""
    startwork()
    report = lib.arrange.weak_arrange(TARGET_FOLDER, destination, FOLDER_TYPES)
    return render_template('completed.html', res=report)


@app.route('/dashboard/deepscan')
def deepScan():
    """Initiate the strong arrange and redirect to report page"""
    startwork()
    report = lib.arrange.strong_arrange(TARGET_FOLDER, destination, FOLDER_TYPES)
    return render_template('completed.html', res=report)


@app.route('/closetheapp')
def close():
    """Turn the web server OFF"""
    
    return '''Server shutting down.., close this browser tab 
    and close the python compiler by using ctrl+c'''


if __name__ == '__main__':
    print("Running the program..")
    time.sleep(0.5)
    linkofPage = 'http://127.0.0.1:5000/changelocation'
    webbrowser.open(linkofPage)
    app.run(debug=True)

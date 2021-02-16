from flask import Flask, render_template, request, redirect, url_for, make_response
##from arrangepy.main import RESULT_DIR, FOLDER_TYPES
from . import func
from . import utils
import webbrowser
import os
import platform
import subprocess
import logging
logging.basicConfig(filename='.server.log', filemode='w')

import sys

RESULT_DIR = "ArrangedPy"
FOLDER_TYPES = utils.configure()

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None


app = Flask(__name__)

portNumber = 45269
linkofPage = "http://127.0.0.1:" + str(portNumber)

TARGET_FOLDER = '.'

def gettheAddress():
    """Read cache file and create target folder"""
    temp = request.cookies.get("directory")
    if temp is None:
        address = TARGET_FOLDER
    else:
        address = temp
    return address


def startwork(TARGET):
    """Create folders to keep files according to their file types"""
    destination = os.path.join(TARGET, RESULT_DIR)
    utils.makeFolders(destination, FOLDER_TYPES.keys())
    return destination


@app.route("/dashboard/")
def dashboard():
    """Scan the location for items"""
    address = gettheAddress()
    dataPacket = {}
    Elements = list(os.scandir(address))
    dataPacket["folder_count"] = len([1 for x in Elements if x.is_dir()])
    dataPacket["file_count"] = len([1 for x in Elements if x.is_file()])
    dataPacket["total_items"] = len(Elements)
    dataPacket["address"] = address
    return render_template("index.html", data=dataPacket, url=linkofPage)


@app.route("/input", methods=["POST", "GET"])
def inputuser():
    """Take the input of the address from HTML methods"""
    if request.method == "POST":
        val = request.form["newaddress"]
    else:
        val = request.args.get("newaddress")
    if os.path.isdir(val):
        resp = make_response(redirect(url_for("dashboard")))
        resp.set_cookie("directory", str(val))
        return resp
    return render_template("error404.html", url=linkofPage + "/changelocation")


@app.route("/changelocation")
def changingPage():
    """Ask for the location to do the cleaning work"""
    return render_template("change.html", url=linkofPage)


def open_file(path):
    """Open the file in explorer"""
    if platform.system() == "Windows":
        os.startfile(path)
    elif platform.system() == "Darwin":
        subprocess.Popen(["open", path])
    else:
        subprocess.Popen(["xdg-open", path])


@app.route("/openlocation")
def openlocation():
    """Open the destination location in explorer"""
    address = gettheAddress()
    path = os.path.join(address, RESULT_DIR)
    open_file(path)
    response = make_response(redirect(url_for("dashboard")))
    return response


@app.route("/dashboard/standardscan")
def standardScan():
    """Initiate the arrange and redirect to report page"""
    TARGET_DIR = gettheAddress()
    destination = startwork(TARGET_DIR)
    report = func.weak_arrange(TARGET_DIR, destination, FOLDER_TYPES)
    others = "Others(Not_moved)"
    if others not in report:
        if len(report) == 0:
            report[others] = "No file to move,"
        else:
            report[others] = 0
    return render_template("completed.html", res=report, url=linkofPage)


@app.route("/dashboard/deepscan")
def deepScan():
    """Initiate the strong arrange and redirect to report page"""
    TARGET_DIR = gettheAddress()
    destination = startwork(TARGET_DIR)
    report = func.strong_arrange(TARGET_DIR, destination, FOLDER_TYPES)
    others = "Others(Not_moved)"
    if others not in report:
        if len(report) == 0:
            report[others] = "No file to move,"
        else:
            report[others] = 0
    return render_template("completed.html", res=report, url=linkofPage)


@app.route("/dashboard/quit")
def close():
    """Turn the web server OFF"""
    return """Server shutting down.., close this browser tab
    and close the python compiler by using ctrl+c"""


def main(target=None):
    if target is None:
        target = os.getcwd()
    global TARGET_FOLDER
    TARGET_FOLDER = target
    webbrowser.open(linkofPage + "/dashboard")
    app.run("localhost", port=portNumber, debug=False)


if __name__ == "__main__":
    print("Running the program..")
    main()

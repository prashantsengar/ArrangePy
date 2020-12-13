import configparser
import re

def configur():
    config=configparser.ConfigParser()
    config.read('config.ini')
    extension=config['ext']
    p = re.compile(r'\'(.*?)\'')
    FOLDER_TYPES = {key:extension[key] for key in extension}
    for key in FOLDER_TYPES:
        FOLDER_TYPES[key] = p.findall(FOLDER_TYPES[key])

    return FOLDER_TYPES
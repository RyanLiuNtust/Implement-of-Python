#Usage
#python listDir.py ./ ".py" true
#python listDir.py ./ ".py" false
import sys, os
from os import listdir
from os.path import isfile, join

def ls(dir, ext, is_only_filename):
    files = []
    print is_only_filename
    for file in os.listdir(dir):
        if file.endswith(ext):
            if(is_only_filename in ['true']):
                filename_extension_list = os.path.splitext(file)
                files.append(filename_extension_list[0])
            else:
                files.append(file)
    return files

if(len(sys.argv) < 3):
    sys.exit("Usage: %s <dir, ext, is_only_filename>" % sys.argv[0])

else:
    files = ls(sys.argv[1], sys.argv[2], sys.argv[3])
    print files


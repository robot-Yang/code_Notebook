# list the filename which contains subString in mypath

from os import listdir
from os.path import isfile, join

subString = "111"
mypath = "./"
onlyGoodfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and subString in f]  # list the filename which contains subString in mypath
# onlyGoodfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]  # list all  files
# onlyGoodfiles = [f for f in listdir(mypath)]  # list all  files and folders

print (onlyGoodfiles)
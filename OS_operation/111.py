from os import listdir
from os.path import isfile, join
subString = "Mark"
mypath = "../"
onlyGoodfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and subString in f]
print (onlyGoodfiles)
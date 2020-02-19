#! /usr/bin/python

import re

# extract negetive numbers from 
message = 'ddd-20'
result = re.findall(r"[-\d]+", message) 
result = float(result)
print (result)
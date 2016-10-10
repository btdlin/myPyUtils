#!/usr/bin/env python

import os

try:
# create a path
	path = "/tmp/test1"
	#os.makedirs(path, exist_ok=True)
	os.makedirs(path)
	#os.removedirs(path)

except OSError as err:
    print("OS error: {0}".format(err))
 

"""
if not os.path.exists(path):
    os.makedirs(path)

if os.path.exists(path):
    print("path exists!")
    os.removedirs(path)

if not os.path.exists(path):
    print("path removed!")
"""


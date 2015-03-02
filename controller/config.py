#!/usr/bin/python2.7
import os, sys

# Project root is considered the directory this is run in. CSAssess/controller
# This will allow all files below this to access anything within the whole tree
# import using a relative path from the root, replacing / with .

# In the file, include this header
#	import sys
#	from PROJECT_ROOT import PROJECT_ROOT
#	sys.path.insert(0,PROJECT_ROOT)


abspath = lambda *p: os.path.abspath(os.path.join(*p))
PROJECT_ROOT = abspath(os.path.dirname(__file__))
#print(PROJECT_ROOT)

sys.path.insert(0,PROJECT_ROOT)


for dirName, subdirList, fileList in os.walk(PROJECT_ROOT):
	print(dirName)
	with open(os.path.abspath(dirName) + "/PROJECT_ROOT.py", "w+") as f:
		f.write("#!/usr/bin/python2.7\n")
		f.write("PROJECT_ROOT='%s'" % (PROJECT_ROOT))
	with open(os.path.abspath(dirName) + "/__init__.py", "w+") as f:
		f.write("")


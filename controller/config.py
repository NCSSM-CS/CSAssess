#!/usr/bin/python2.7
import os, sys

abspath = lambda *p: os.path.abspath(os.path.join(*p))

PROJECT_ROOT = abspath(os.path.dirname(__file__))
#print(PROJECT_ROOT)

sys.path.insert(0,PROJECT_ROOT)


for dirName, subdirList, fileList in os.walk(PROJECT_ROOT):
	print(dirName)
	with open(os.path.abspath(dirName) + "/PROJECT_ROOT.py", "w+") as f:
		f.write("#!/usr/bin/python2.7\n")
		f.write("import sys\n")
		f.write("PROJECT_ROOT='%s'\n" % (PROJECT_ROOT))
		f.write("sys.path.insert(0,PROJECT_ROOT)")
	with open(os.path.abspath(dirName) + "/__init__.py", "w+") as f:
		f.write("")


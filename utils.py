import os

_path = os.path.dirname(os.path.abspath(__file__))

def getPath():
	return _path

def resolvePath(start, res):
	return os.path.abspath(os.path.join(start,res))
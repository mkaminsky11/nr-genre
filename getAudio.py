import pafy # use this to get metadata, audio
import os
import subprocess

import utils

# https://www.youtube.com/watch?v=XoLouT7TqZY

def download(id, category):
	try:
		v = pafy.new(id)
		for i in range(0,len(v.audiostreams)):
			if v.audiostreams[i].extension == "ogg":
				# get current path
				# path / data / { category } / { id } . ogg
				downloadFile(id, category, v.audiostreams[i].url)
				return "ogg"
		for i in range(0,len(v.audiostreams)):
			if v.audiostreams[i].extension == "webm":
				# get current path
				# path / data / { category } / { id } . ogg
				downloadFile(id, category, v.audiostreams[i].url)
				return "webm"
		for i in range(0,len(v.audiostreams)):
			if v.audiostreams[i].extension == "m4a":
				# get current path
				# path / data / { category } / { id } . ogg
				downloadFile(id, category, v.audiostreams[i].url)
				return "m4a"

		print("missed 1 in {0}".format(category))
		return False
	except:
		print("missed 1 in {0}".format(category))
		return False

def convert(id, category, ext):
	localPath = "data/{0}/{1}".format(category,id)
	fullPath = utils.resolvePath(utils.getPath(),localPath)
	subprocess.call(["ffmpeg","-i",fullPath+".ogg", fullPath+".wav","-loglevel","panic"])
	#subprocess.call(["rm","-rf",fullPath+".ogg"])
	#print("Converted {0}".format(id))
	return fullPath+".wav"

def playlistData(ids, num):
	# array of playlist ids...get num from each
	ret = []
	for id in ids:
		url = "https://www.youtube.com/playlist?list={0}".format(id)
		playlist = pafy.get_playlist2(url)
		playData = []
		for item in playlist:
			#print(item.videoid)
			playData.append(item.videoid)
			if len(playData) == num:
				break
		ret = ret+playData
	return ret

def downloadFile(id, category, url):
	localPath = "data/{0}/{1}.ogg".format(category,id)
	fullPath = utils.resolvePath(utils.getPath(),localPath)
	subprocess.call(["wget",url,"-O",fullPath,"--quiet"])
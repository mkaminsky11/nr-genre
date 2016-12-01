import getAudio
import json
import config

genres = config.genres


#result = getAudio.download(id, category) # download it and convert to .wav

f = open("ids_final.json","r")
ids = json.loads(f.read())["ids"]
f.close()

total = len(ids)
counter = 0

res = []

for item in ids:
	getAudio.convert(item["id"],item["category"],item["ext"])
	counter = counter + 1
	print("Converted {0}/{1}".format(counter,total))
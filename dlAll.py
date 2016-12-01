import getAudio
import json
import config

genres = config.genres


#result = getAudio.download(id, category) # download it and convert to .wav

f = open("ids.json","r")
ids = json.loads(f.read())["ids"]
f.close()

total = len(ids)
counter = 0

res = []

for item in ids:
	result = getAudio.download(item["id"], item["category"])
	counter = counter + 1
	print("Downloaded {0}/{1}".format(counter,total))
	if result == False:
		print("DL failed!")
	else:
		item["ext"] = result
		res.append(item)

f = open("ids_final.json","w+")
f.write(json.dumps({
	"ids": res
}))
f.close()
import getAudio
import json
import config

# think about sources...
	# youtube playlists

# 100 of each

# edm x
# pop x
# rock x
# rap x
# country
# classical
# jazz

genres = config.genres

#id = "XoLouT7TqZY"
#category = "edm"
#result = getAudio.download(id, category) # download it and convert to .wav
#audioPath = getAudio.convert(id,category)
#mels.getMels(audioPath, id, category)
res = []
for cat in genres:
	ids = getAudio.playlistData(genres[cat]["list"],genres[cat]["num"])
	print(len(ids))
	for id in ids:
		res.append({
			"id": id,
			"category": cat
		})
f = open("ids.json","w+")
f.write(json.dumps({
	"ids": res
}))
f.close()
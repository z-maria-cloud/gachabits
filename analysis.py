import json

with open('gachabits.json', 'r') as file:
	data = json.load(file)
	keys = data.keys()
	total_words = 0
	
	print(f"Contains {len(keys)} categories: ")
	for i in keys:
		print(f" → {i}: {len(data[i])} words")
		total_words = total_words + len(data[i])
		
	print(f"This version of Gachabits contains {total_words} words.")

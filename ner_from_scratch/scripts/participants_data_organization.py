import json

# Opening JSON file
f = open("./ner_from_scratch/assets/schedule_random_participants_1000.json")

# returns JSON object as
data = json.load(f)

# Iterating through the json
# saving as jsonl
k = list(data.keys())[0]
with open("./ner_from_scratch/assets/schedule_random_participants_1000.jsonl", 'w') as outfile:
    for entry in data.get(k):
        json.dump(entry, outfile)
        outfile.write('\n')

# Closing file
f.close()


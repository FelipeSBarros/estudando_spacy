import json
import jsonlines

# Opening JSON file
f = open("./ner_demo/assets/schedule_participants_202207141530.json")

# returns JSON object as
data = json.load(f)

# Iterating through the json
# saving as jsonl
k = list(data.keys())[0]
with open("./ner_demo/assets/schedule_participants_202207141530.jsonl", 'w') as outfile:
    for entry in data.get(k):
        json.dump(entry, outfile)
        outfile.write('\n')

# Closing file
f.close()

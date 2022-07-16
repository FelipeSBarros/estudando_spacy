import spacy
import json

nlp = spacy.load('pt_core_news_lg')
with open("./ner_from_scratch/assets/schedule_random_participants_1000.jsonl", 'r') as json_file:
    json_list = list(json_file)

original_ner = []
for json_str in json_list[:10]:
    result = nlp(json.loads(json_str).get('participants'))
    doc = result.text
    data = {"entities":
             [
                 (entity.start_char, entity.end_char, entity.text, entity.label_)
                 for entity in result.ents if result]}
    #print(data)
    original_ner_tuple = (doc, data)
    original_ner.append(original_ner_tuple)

#print(original_ner)

with open("./ner_from_scratch/assets/schedule_participants_100_train.json", 'w') as outfile:
    json.dump(original_ner, outfile, indent=2)

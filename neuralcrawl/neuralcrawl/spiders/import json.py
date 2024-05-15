import json

with open('outputets2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

for entry in data:
    for key, value in entry.items():
        if isinstance(value, str):
            entry[key] = value.replace('\n', '').replace('\t', '')
    if entry.end_location().find(entry.start_location):
        print("asda")
# Write the modified data back to the file
with open('outputets2.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False)  # ensure_ascii=False to preserve non-ASCII characters

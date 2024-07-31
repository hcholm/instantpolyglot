import os
import json

path = "docs/eng/"
files = os.listdir(path)
output = {}

for file in files:
    language_name = file.split(".")[0]
    output[language_name] = "dist/" + language_name + ".html"

with open("language_index.json", "w") as f:
    f.write(json.dumps(output, indent = 4))

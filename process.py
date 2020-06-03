#!/usr/bin/env python3
import os
import json

folder = './datasets/startrek_tng'
output_filename = 'eps_101-109.txt'
output = ''
scripts = []

script_data = []
directories = []

os.chdir("raw_data")

for directory in os.listdir():
    directories.append(directory)
    os.chdir(directory)
    for filename in os.listdir():
        try:
            with open(filename, 'r') as file:
                # print(file.read())
                script = file.read()
                title = f"Star Trek: {directory.upper()}"
                genre = ["science fiction"]
                source_url = ""
                content = {"script": script, "genre": genre,
                           "source_url": source_url, "title": title}
                script_data.append(content)

        except:
            print(f"{directory}/{filename} has error. Skipping")
    os.chdir("..")

print(f"{len(script_data)} scripts processed")

scripts_json = json.dumps(script_data)

os.chdir("..")
with open("scripts.json", "w") as file:
    file.write(scripts_json)

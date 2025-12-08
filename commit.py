#! /usr/bin/env python3

import datetime
import os
import json
import sys

hist = json.loads(open('history.json').read())
hnames = list(map(lambda x: x["name"], hist))
os.listdir('posts')
posts = os.listdir('posts')


changed = False

for po in posts:
  if po.endswith('.md') and not po.startswith("_") and not po in hnames:
    changed = True
    date = datetime.datetime.now()
    hist.append({
      "name": po,
      "date": date.strftime('%B %d, %Y')
    })


for h in hist:
  if not h["name"] in posts:
    changed = True
    hist.remove(h)

text = open("indextemplate.md").read().replace("{}",
  '\n'.join([
    f'* [{x["name"][:-3].replace("_", " ")}](posts/{x["name"]}) [{x["date"]}]'
    for x in reversed(hist)
]))

print(text)

json.dump(hist, open('history.json', 'w'), indent=2)
open("index.md", "w").write(text)

os.system(f'git add .')
os.system(f'git commit -m "blog update"')
os.system(f'git push')

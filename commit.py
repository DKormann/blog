

import os
import json
import sys

hist = json.loads(open('history.json').read())

os.listdir('posts')

posts = os.listdir('posts')

msg = ''

for po in posts:
  if po.endswith('.md') and not po in hist:
    hist.append(po)
    msg += f'added {po}; '

for h in hist:
  if not h in posts:
    hist.remove(h)
    msg += f'removed {h}; '

text = open("indextemplate.md").read().replace("{}",
  '\n'.join([
    f'* [{x[:-3]}](posts/{x})'
    for x in reversed(hist)
    if x.endswith('.md')
]))


json.dump(hist, open('history.json', 'w'))

open("index.md", "w").write(text)


os.system(f'git add .')
os.system(f'git commit -m "{msg}"')
os.system(f'git push')

import os

os.listdir('posts')

text = open("indextemplate.md").read().replace("{}",
  '\n'.join([
    f'* [{x[:-3]}](posts/{x})'
    for x in os.listdir('posts') if x.endswith('.md')
]))

open("index.md", "w").write(text)

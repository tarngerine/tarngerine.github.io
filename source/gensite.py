import os
import misaka
import re
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


def genFromDirectory(root='content', dest='../'):
  for f in os.listdir(root):
    p = os.path.join(root, f)

    # Recurse if directory
    if os.path.isdir(p):
      genFromDirectory(root + '/' + f, dest + f + '/')

    if not p.endswith('.md'):
       continue

    with open(p, 'r', encoding='utf-8') as file:
      s = file.read()

      d = {}  # Data for rendering

      # parse frontmatter: ---key:value---\n
      res = re.search('^(---)([\s\S]*)(---)\n([\s\S]*$)', s)
      if res:
        meta = yaml.load(res.group(2))
        for k in meta:
          d[k] = meta[k]

        content = res.group(4)
      else:
        content = s

      content = protect_cors_url(content)
      md = misaka.Markdown(misaka.HtmlRenderer())

      d['content'] = md(content)

      if not os.path.exists(dest):
        os.makedirs(dest)

      n = os.path.splitext(f)[0]
      with open(dest+n+'.html', 'w', encoding='utf-8') as file:
        env = Environment(
          loader = FileSystemLoader('templates'))
        tmplId = d['template'] if 'template' in d.keys() else 'default'
        tmpl = env.get_template(tmplId+'.html')
        file.write(tmpl.render(page=d))

# Protects cross origin (external) URL links
def protect_cors_url(md):
  a = '<a href="{{URL}}" target="_blank" rel="noopener">{{LABEL}}</a>'
  res = re.findall('(\[([\S ]+?)\]\((http[\S]+?)\))', md)
  if res:
    for l in res:
      l2 = a.replace('{{URL}}', l[2]).replace('{{LABEL}}', l[1])
      md = md.replace(l[0],l2)
    return md
  else:
    return md

genFromDirectory()

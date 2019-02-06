import os
import misaka
import re
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape


def main():
  for f in os.listdir('content'):
    p = os.path.join('content', f)

    # temporary, todo: recursive directory
    if '.md' not in p:
       continue

    with open(p, 'r', encoding='utf-8') as file:
      s = file.read()

      # parse frontmatter: ---key:value---\n
      res = re.search('^(---)([\s\S]*)(---)\n([\s\S]*$)', s)
      if res:
        meta = yaml.load(res.group(2))
        content = res.group(4)
      else:
        content = s

      content = protect_cors_url(content)
      md = misaka.Markdown(misaka.HtmlRenderer())

      d = {
        'content': md(content)
      }

      for k in meta:
        d[k] = meta[k]

      n = os.path.splitext(f)[0]
      with open('../'+n+'.html', 'w', encoding='utf-8') as file:
        env = Environment(
          loader = FileSystemLoader('templates'))
        tmpl = env.get_template(meta['template']+'.html')
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

main()

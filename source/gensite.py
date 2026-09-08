import os
import re
import yaml
import datetime
import markdown2
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup


def genFromDirectory(root='content', dest='../'):
  for f in os.listdir(root):
    p = os.path.join(root, f)

    if os.path.isdir(p):
      genFromDirectory(root + '/' + f, dest + f + '/')

    if not p.endswith('.md'):
       continue

    with open(p, 'r', encoding='utf-8') as file:
      s = file.read()

      d = {}

      # frontmatter
      res = re.search(r'^(---)([\s\S]*)(---)\n([\s\S]*$)', s)
      if res:
        meta = yaml.load(res.group(2), Loader=yaml.FullLoader)
        for k in meta:
          d[k] = meta[k]
        content = res.group(4)
      else:
        content = s

      content = protect_cors_url(content)

      # markdown -> HTML (like misaka did)
      html = markdown2.markdown(content)

      # CRUCIAL: tell Jinja this is already HTML
      d['content'] = Markup(html)

      d['created'] = datetime.datetime.fromtimestamp(
        os.path.getmtime(p)
      ).strftime('%A · %B %d · %Y')

      if not os.path.exists(dest):
        os.makedirs(dest)

      n = os.path.splitext(f)[0]
      with open(dest + n + '.html', 'w', encoding='utf-8') as file_out:
        env = Environment(
          loader=FileSystemLoader('templates'),
          autoescape=select_autoescape(['html', 'xml'])
        )
        tmplId = d['template'] if 'template' in d else 'default'
        tmpl = env.get_template(tmplId + '.html')
        file_out.write(tmpl.render(page=d))


def protect_cors_url(md):
  a = '<a href="{{URL}}" target="_blank" rel="noopener">{{LABEL}}</a>'
  res = re.findall(r'(\[([\S ]+?)\]\((http[\S]+?)\))', md)
  if res:
    for l in res:
      l2 = a.replace('{{URL}}', l[2]).replace('{{LABEL}}', l[1])
      md = md.replace(l[0], l2)
  return md


if __name__ == "__main__":
  genFromDirectory()

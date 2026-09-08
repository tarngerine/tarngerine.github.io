import os
import re
import yaml
import datetime
import markdown2
from jinja2 import Environment, FileSystemLoader, select_autoescape


def genFromDirectory(root='content', dest='../'):
  tree = {}  # Entire file tree

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
      # use raw strings to avoid invalid escape sequence warnings
      res = re.search(r'^(---)([\s\S]*)(---)\n([\s\S]*$)', s)
      if res:
        meta = yaml.load(res.group(2), Loader=yaml.FullLoader)
        for k in meta:
          d[k] = meta[k]

        content = res.group(4)
      else:
        content = s

      content = protect_cors_url(content)

      # actual file contents: convert markdown to HTML
      d['content'] = markdown2.markdown(content)

      # file created
      d['created'] = datetime.datetime.fromtimestamp(
        os.path.getmtime(p)
      ).strftime('%A · %B %d · %Y')

      if not os.path.exists(dest):
        os.makedirs(dest)

      n = os.path.splitext(f)[0]
      with open(os.path.join(dest, n + '.html'), 'w', encoding='utf-8') as out_file:
        env = Environment(
          loader=FileSystemLoader('templates'),
          autoescape=select_autoescape(['html', 'xml'])
        )
        tmplId = d['template'] if 'template' in d else 'default'
        tmpl = env.get_template(tmplId + '.html')
        out_file.write(tmpl.render(page=d))


# Protects cross origin (external) URL links
def protect_cors_url(md):
  a = '<a href="{{URL}}" target="_blank" rel="noopener">{{LABEL}}</a>'
  # use raw string; avoid invalid escape sequence warning
  res = re.findall(r'(\[([\S ]+?)\]\((http[\S]+?)\))', md)
  if res:
    for l in res:
      l2 = a.replace('{{URL}}', l[2]).replace('{{LABEL}}', l[1])
      md = md.replace(l[0], l2)
    return md
  else:
    return md


if __name__ == "__main__":
  genFromDirectory()

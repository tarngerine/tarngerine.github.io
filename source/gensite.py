import os
import markdown
import misaka
import re
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

for f in os.listdir('content'):
  p = os.path.join('content', f)

  with open(p, 'r', encoding='utf-8') as file:
    s = file.read()

    # parse frontmatter: ---key:value---\n
    res = re.search('^(---)([\s\S]*)(---)\n([\s\S]*$)', s)
    if res:
      meta = yaml.load(res.group(2))
      content = res.group(4)
    else:
      content = s

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

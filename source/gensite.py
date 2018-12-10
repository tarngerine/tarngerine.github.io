from jinja2 import Environment, FileSystemLoader, select_autoescape
import markdown
import misaka
import re
import yaml

with open('content/index.md', 'r', encoding='utf-8') as file:
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

  with open('../index.html', 'w', encoding='utf-8') as file:
    env = Environment(
      loader = FileSystemLoader('templates'))
    tmpl = env.get_template('index.html')
    file.write(tmpl.render(page=d))

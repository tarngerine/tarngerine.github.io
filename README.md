Source for [tarng.com](tarng.com)

### Installation
Requires `python3`.
Use `pip3` to install [`misaka`](https://github.com/FSX/misaka) (Markdown parsing), [`PyYaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) (frontmatter extraction since misaka doesn't support it), and [`Jinja2`](http://jinja.pocoo.org) (templating).

### Building
`python3 source/gensite.py`

### Structure
```
/
  source/
    content/ - all markdown files
    templates/ - all templates
      base.html - basic wrapper with <head>, <meta> to be extended
  <exported html files here>
```

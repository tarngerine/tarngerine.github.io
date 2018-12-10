Source for [tarng.com](tarng.com)

### Installation
Requires `python3`.
Use `pip3` to install [`misaka`](https://github.com/FSX/misaka) (Markdown parsing), [`PyYaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) (frontmatter extraction since misaka doesn't support it), and [`Jinja2`](http://jinja.pocoo.org) (templating).

### Building
```
cd source
python3 gensite.py
```

### Structure
```
/
  source/
    content/ - all markdown files
    templates/ - all templates
      base.html - basic wrapper with <head>, <meta> to be extended
    gensite.py
  <exported html files here>
```

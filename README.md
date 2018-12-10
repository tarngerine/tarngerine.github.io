Source for [tarng.com](tarng.com)

### Installation
1. Use Homebrew to install `python3` and [`fswatch`](https://github.com/emcrisostomo/fswatch).
1. Use `pip3` to install [`misaka`](https://github.com/FSX/misaka) (Markdown parsing), [`PyYaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) (frontmatter extraction since misaka doesn't support it), and [`Jinja2`](http://jinja.pocoo.org) (templating).

### Building
```
cd source
./watch
```
`./watch` will watch the `source/` directory for any changes, rebuild (`python3 gensite.py`) and refresh any tabs in Safari (lol sorry not sorry) with local files open.

### Structure
```
/
  source/
    content/ - all markdown files
    templates/ - all templates
      base.html - basic wrapper with <head>, <meta> to be extended
    gensite.py
  <generated html files here>
```

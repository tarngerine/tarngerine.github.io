Source for [tarng.com](tarng.com)

### Installation

1. Use Homebrew to install `python3` and [`fswatch`](https://github.com/emcrisostomo/fswatch) (only necessary for live reload locally).
1. Use `pip` (`python3 -m pip install ...`) to install [`misaka`](https://github.com/FSX/misaka) (Markdown parsing), [`PyYaml`](https://pyyaml.org/wiki/PyYAMLDocumentation) (frontmatter extraction since misaka doesn't support it), and [`Jinja2`](http://jinja.pocoo.org) (templating), as well as `httpwatcher`.

### Building

```
cd source
./watch
httpwatcher
```

1. `./watch` will watch the `source/` directory for any changes, rebuild (`python3 gensite.py`) and refresh any tabs in Safari (lol sorry not sorry) with local files open.
2. Run `httpwatcher` directly in bash/zsh/fish.

You may need to run `./restore_mtime.sh` since git clone doesn't persist the creation time of each file, which effects the `gensite.py`'s automatic date adding for certain content.

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

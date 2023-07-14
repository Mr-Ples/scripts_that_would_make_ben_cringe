# for scripts that would make ben cringe

scripts are standalone, but can be accessed via a CLI tool

# CLI

## Install

```bash
python3 -m pip install -r requirements.txt
```

```bash
ln -s $PWD/scripts $HOME/.local/bin
```

### Bash Completions

```bash
scripts -- --completion >  /tmp/comp.sh
sudo chmod +x /tmp/comp.sh
source /tmp/comp.sh
```

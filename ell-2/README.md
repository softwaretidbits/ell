# Software Tidbits Ell - Part 2

## About
Welcome to a SoftwareTidbits session (ell-2) about using ell-studio as part of your prompt engineering w/ Python and ell. If you missed the first session take a look at 
the [introduction session](https://medium.com/software-tidbits/prompt-engineering-using-ell-language-model-programming-lib-3658287c96e5)

### Activities
1. Execute the four use cases from the 'ell introduction' session to build up some persisted LMP information.
2. Run the ell-studio tool using your command line.  Example: ell-studio --storage ./logdir
3. Open the link upon startup. By default, this is: http://127.0.0.1:8080.
4. Explore and follow along with the blog post related to this project.

Take note of this change from the first session to ensure we have persisted information about the LMPs used in each example.

```python
ell.init(autocommit=True, verbose=True, store='./logdir')
```


## Getting Started
```bash
# Install your python
pyenv install 3.10.12
```

```bash
# Setup a virtual environment
pyenv virtualenv 3.10.12 vtidbits
```

```bash
# Activate your virtual environment
pyenv activate vtidbits
```

```bash
# Installs `ell` and `ell-studio` on your system allowing you to start using the tools for prompt engineering and visualization.
pip install -U ell-ai
```

```bash
# Verify your installation by checking the version of ell:
python -c "import ell; print(ell.__version__)"
```

```python
# Running the ell-studio
ell-studio --storage ./logdir
```

## References
The following sites are useful for getting started and learning more about ell.
* https://docs.ell.so/core_concepts/ell_studio.html
* https://github.com/MadcowD/ell
* https://docs.ell.so/
* https://github.com/softwaretidbits/ell
* https://medium.com/software-tidbits/prompt-engineering-using-ell-language-model-programming-lib-3658287c96e5
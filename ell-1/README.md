# Software Tidbits Ell - Part 1

## About
Ell is a lightweight prompt engineering library treating prompts as functions. Prompts are thought of as programs and not strings with ell. 

Thinking in terms of functions instead of individual strings, LMPs (language model programs) represent functions where a set of functions makeup a program.

The program itself encapsulates either a string prompt or a list of messages to be sent to various multimodal language models.

This is the gist of ell.

## Language Model Programs

LMPs represent functions. Using ell's decorators (as decorators in your Python logic) you can convert a regular Python function into an LMP.

Below is an example of ell's simple decorator used to work with language models that return text.  

```python
ell.simple(model: str, client: Any | None = None, exempt_from_tracking=False, **api_params)
```

LLMs can process and generate various types of content (text, audio, video, and images). As such, there is a decorator (called complex) for this as well.  Let's take a look.

```python
ell.complex(model: str, client: Any | None = None, exempt_from_tracking=False, tools: List[Callable] | None = None, post_callback: Callable | None = None, **api_params)
```

There are many capabilities when using the complex decorator.  

An example of how the complex decorator supports structured outputs is below. 

### Want to retain your versioned prompts for future usage?

```python
ell.init(store='./prompts', autocommit=True)
```

You can explore your prompts using **ell-studio**.

ell-studio is installed by default, just run it!

```bash
ell-studio --storage ./prompts
```

Now you can visualize all of your LMPs saved in the ./prompts directory. Track the changes over time and most importantly inspect their dependencies. Ell will serialize the arbitrary Python code allowing you to track how the LMPs are used through their outputs and inputs. 

Actually making something of higher quality using AI requires construction involving numerous calls to an LLM.  That is prompt engineering.  Using functions breaks down the problem and makes it easier to retain and implement foundational techniques.  Not to mention, your prompt engineering becomes modular and easier to reason about.
* Calls to LLMs are valuable.
* Treats multi-modality as first class.
* Provides tooling using a studio ui.

### Verbose mode
Use verbose mode activation during initialization to get more details of what happens with the language model invocations

```python
ell.init(verbose=True)
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

* https://github.com/MadcowD/ell
* https://docs.ell.so/
* https://github.com/softwaretidbits/ell
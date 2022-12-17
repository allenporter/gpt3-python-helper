# Open Source Projects

This markdown file is training data that describes overview and details for what
good python open source projects look like. This document gives general background
information to gpt-3 about the goals of what we're trying to accomplish and
any other training data needed for context.

## GPT-3

The goal of this project is to use GPT-3 to develop software projects, and create an
entire workflow (much much more beyond just having it produce code snippets, but it does
that too).

The project will use GPT-3 to write the entire project file structure and file contents,
including all the typical setup, precommits, workflows, readmes, tests, etc. A command line
driver program will do the heavy lifting of calling the gpt-3 APIs. The project may
also write command line tools standalone if asked.

The user will interact with gpt-3 through the command line. They will produce a project
file that includes their requirements and goals, then invoke the command line with any
necessary command line flags. The users input file is like the training data (like this file),
and the driver command line produces the output files/artifacts to a specified temp directory.
Since working with gpt-3 requires trial and error, the users workflow will involve editing
their project file, running the program, checking the output, refining the program, etc. until
they are happy.

The gpt-3 API has limitations on response objects, so the driver program needs to call the
API a way to generate complete answers (e.g. streaming or batch API, or whatever is needed).

GPT3 has a python library `openai` that can use the `Completion` API with a model such
as `text-davinci-002`. This is just the standard API and nothing custom for this project.

```python
"""This code snippet calls the completion APi with a prompt and gets the response."""

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.5,
        max_tokens=1024,
    )
```

## Python command line

A python command line tool is used to call libraries interactively or accepting input files
and writes output to a terminal or to other files. A command line tool has a main, parses
the command line flags if any or other arguments, then runs any coded needed to complete
the task either inline or calling other libraries or functions.

Example: my_project/main.py
```python
"""My project is a command line tool that does x, y, and z.

This is more detail about my project.
"""

import argparse
import api

def main():
    """My project command line tool."""
    parser = argparse.ArgumentParser(description="My project")
    args = parser.parse_args()

    print(api.call(args[0]))

if __name__ == "__main__":
    main()
```

## Python Best Practices

Python best practices include using mypy for typing, python3, pytest for testing,
pylint, black, flake8 for formatting and linting. Python libraries are best when
using setup.cfg and minimal setup.py.

Documentation is important for new users to understand the project, as well as
for code authors to remember important facts. Documentation using pydoc best
practices is the best way.

Development is done with 'venv' and pinned python libraries. Dependencies can
be managed with renovatebot.

Project versions use semvar (e.g. major, minor, patch versions) following best practices.

## Project file

The project file is a yaml file that describes the project. The project file is used
by the command line tool to generate the project.

The project file has the following fields:
  - name: The name of the project
  - version: The version of the project
  - description: A description of the project
  - files: A list of files to generate

Each file has the following fields:
  - name: The name of the file
  - description: A description of the file

An example project file may look something like this:
```yaml
name: random-text
version: 0.0.1
description: This project is about creating random text.
files:
  - name: setup.py
    description: Minimal, not really used except to reference setup.cfg
  - name: setup.cfg
    description: Where the library is configured with a description, important dependency pins, etc
  - name: requirements.txt
    description: Development library pins to specific versions
  - name: random_text/__init__.py
    description: Module initialization for random-text library
  - name: random_text/random_text.py
    description: Main library module for random text creation
  - name: tests/test_random_text.py
    description: Tests for the random text creation
  - name: .gitignore
    description: Ignores python files that should not be in the git repo
  - name: .pre-commit-config.yaml
    description: For configuring linting, formatting, etc.
  - name: .github/workflows/python-package.yaml
    description: For running tests, linting, etc for new PRs
  - name: .github/workflows/python-publish.yaml
    description: For publishing to pypi on new releases
  - name: README.md
    description: Overview for the project, goals, and some simple getting started guides
  - name: CONTRIBUTING.md
    description: Contains details about how to setup the project using a python "venv", now to run tests, and encourages uses to submit a PR.
  - name: venv/
    description: Not actually part of the project, but where the users local venv lives. This is ignored by .gitignore.
```

## Command line tools for generating projects

Before we can actually develop the gpt-3 aided software development project, we need to
bootstrap that itself with the help of gpt3. We can start with a simple command line 
program that takes this file as input and outputs the driver cli program. This part is
a little "meta". The driver program itself has the following code comments:

```python
"""
gpt3-develop is a command line program that calls the gpt-3 API for use in developing
software project. The main things that happen in the program are:
  - Gpt-3 api is initialized with an API key
  - Reads the training data markdown file and yaml project file
  - Create prompts to include the necessary training and project data
  - Parses the response output filenames and files
  - Writes the files to disk or prints them on the screen

The prompts must be created so they result in structured output that can be parsed by the
program. The program handles creating the prompts as well as parsing the response to pull
out the structured response with filenames and file contents.

Since the input/output files may be large, the program breaks down the requests into
smaller pieces to avoid any API limits.

Example usage:
  ./gpt3-develop.py --api-key=<KEY> --project-file ./project.yaml --training-data ./project.md --output-dir=/tmp/project
"""
```

Please generate the command line code for ./gpt3-develop.py:

# Open Source Projects

This markdown file is training data that describes overview and details for what
good python open source projects look like. This document gives general background
information to gpt-3 about the goals of what we're trying to accomplish and
any other training data needed for context.

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

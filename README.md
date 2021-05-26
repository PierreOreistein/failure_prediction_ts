# TurboFan-Failure-Prediction

## Overview

This is your new Kedro project, which was generated using `Kedro 0.17.3`.

Take a look at the [Kedro documentation](https://kedro.readthedocs.io) to get started.

## Rules and guidelines

In order to get the best out of the template:

- Don't remove any lines from the `.gitignore` file we provide
- Make sure your results can be reproduced by following a [data engineering convention](https://kedro.readthedocs.io/en/stable/12_faq/01_faq.html#what-is-data-engineering-convention)
- Don't commit data to your repository
- Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

### Set-up

You need to create a virtual environment to safely work on the project. We recommend
using `pyenv`.

```console
$ pyenv virtualenv 3.8.8 <your-project> # replace `3.8.8` by the python version you need and `<your-project>` with your project name
$ pyenv local <your-project> # again, use the name of your environment
```

### Installing the dependencies

We will install the requirements so that we have the `kedro` command line utility, and
then use the `kedro install` command.

```console
$ pip install -r src/requirements.txt
$ # the next line is a work around so that the credentials of your private repo that are
$ # in `~/.pip/pip.conf` do not leak in the `requirements.txt` file
$ kedro build-reqs --no-emit-index-url
$ kedro install
```

As the prompt will tell you, if you need a new package, you need to add it to the
`src/requirements.in`, then re-build the requirements before installing with

```console
$ kedro build-reqs --no-emit-index-url && kedro install
```

### Installing the pre-commits

The pre-commits help avoid prevent common mistakes and ensure coherent style.
You need to install the development dependencies, and then initialize the pre-commits.

```console
$ pip install -r src/requirements-dev.txt
$ # optional, if the repo is not initialized for git
$ git init
$ pre-commit install
```

Now, every time you commit, some checks are run:

- Large files are not included in the commit,
- Yaml files are valid,
- End of files is an empty line,
- There are no calls to the python debugger,
- The line end are coherents,
- `isort`, `black`, `mypy` and `flake8` are run.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/03_tutorial/05_package_a_project.html)

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

### Using credentials in an agent

If you want to use credentials in an agent, you need to use environment
variables in the conf/base/credentials.yml, and add `!conf/base/credentials.yml` 
to your `.gitignore`. 

Example of conf/base/credentials.yml :
```console
# credentials.yml
db:
  username: ${USERNAME}
  password: ${PASSWORD}

```


## How to run your Kedro pipeline

You can run your Kedro project with:

```console
$ kedro run
```

## How to test your Kedro project

Have a look at the file `src/tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```console
$ kedro test
```

To configure the coverage threshold, go to the `.coveragerc` file.

## Project dependencies

To generate or update the dependency requirements for your project:

```console
$ kedro build-reqs --no-emit-index-url
```

This will copy the contents of `src/requirements.txt` into a new file `src/requirements.in` which will be used as the source for `pip-compile`. You can see the output of the resolution by opening `src/requirements.txt`.

After this, if you'd like to update your project requirements, please update `src/requirements.in` and re-run `kedro build-reqs`.

[Further information about project dependencies](https://kedro.readthedocs.io/en/stable/04_kedro_project_setup/01_dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, `catalog`, and `startup_error`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `kedro install` you will not need to take any extra steps before you use them.

### Jupyter

You can start a local notebook server:

```console
$ kedro jupyter notebook
```

### JupyterLab

You can also start JupyterLab:

```console
$ kedro jupyter lab
```

### IPython

And if you want to run an IPython session:

```console
$ kedro ipython
```

### How to convert notebook cells to nodes in a Kedro project

You can move notebook code over into a Kedro project structure using a mixture of [cell tagging](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#release-5-0-0) and Kedro CLI commands.

By adding the `node` tag to a cell and running the command below, the cell's source code will be copied over to a Python file within `src/<package_name>/nodes/`:

```console
$ kedro jupyter convert <filepath_to_my_notebook>
```

> _Note:_ The name of the Python file matches the name of the original notebook.

Alternatively, you may want to transform all your notebooks in one go. Run the following command to convert all notebook files found in the project root directory and under any of its sub-folders:

```
kedro jupyter convert --all
```

### How to ignore notebook output cells in `git`

To automatically strip out all output cell contents before committing to `git`, you can run `kedro activate-nbstripout`. This will add a hook in `.git/config` which will run `nbstripout` before anything is committed to `git`.

> _Note:_ Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://kedro.readthedocs.io/en/stable/03_tutorial/05_package_a_project.html)

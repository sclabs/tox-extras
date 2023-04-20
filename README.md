tox-extras
==========

A tox plugin to install extras directly from `pyproject.toml` into a testenv

Quick start
-----------

Install it with

    pip install tox-extras

Add it to `requires` in the `[tox]` section of your `tox.ini`

    [tox]
    min_version = 4.0
    requires = tox-extras

Say you have a lint extra in `pyproject.toml` which you want to use in a
testenv:

    [project.optional-dependencies]
    lint = ["black==23.3.0"]

In your `tox.ini` testenv sections you can write

    [testenv:lintonly]
    skip_sdist = true
    skip_install = true
    tox_extras = lint
    commands = black --check example.py

and this will install all deps from the "lint" extra into the testenv without
installing your package or any of its deps.

Motivation
----------

Tox has built-in support for installing extras using the `extras` testenv config
option, but this does not work when combined with `skip_install`.

This plugin adds a `tox_extras` option to the tox `EnvConfigSet` and installs
the extras named in this option into the testenv directly from `pyproject.toml`
without installing the package.

This would be especially valuable when we want to use `pyproject.toml` as a
single source of truth for our build, install, and dev dependencies (so putting
`deps` in `tox.ini` is out of the question), but at the same time we don't want
to "waste time" building and installing our package (and maybe its deps in a
first-time tox run, e.g., in CI) into a testenv that only runs a linter (and
therefore does not depend at all on the package or any deps being installed).

See https://github.com/tox-dev/tox/issues/2301 for the corresponding feature
request in tox.

See https://github.com/pypa/pip/issues/4783#issuecomment-343771222 for
commentary about the possible advantages of keeping all dependencies in one
place.

Limitations
-----------

This plugin explicitly parses `pyproject.toml`, so it will not work with
projects that define extras in `setup.py`.

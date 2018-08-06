# signac - PyData Ann Arbor MeetUp 2018

[![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/csadorf/pydata-ann-arbor-2018/master?urlpath=lab/tree/index.ipynb)

## About

This is a collection of Jupyter notebooks and slide decks used as an introduction and demonstration on how to use [**signac**](http://www.signac.io) presented at the [PyData Ann Arbor MeetUp group](https://www.meetup.com/PyData-Ann-Arbor/) on [August 7th 2018](https://www.meetup.com/PyData-Ann-Arbor/events/249050578/).
You can launch an **interactive** version of these notebooks following [this link](https://mybinder.org/v2/gh/csadorf/pydata-ann-arbor-2018/master?urlpath=lab/tree/index.ipynb) (powered by [MyBinder](https://mybinder.org/)).

The **signac** framework is a collection of Python packages that are designed to automate computational investigations and manage the underlying data spaces. The framework is lightweight and easy to integrate with other tools, such as [pandas](https://pandas.pydata.org/) or [tensorflow](https://www.tensorflow.org/).

* Part 1 - Introduction to signac's core functions ([slides](https://csadorf.github.io/pydata-ann-arbor-2018/))
* Part 2 - Demonstration of **signac** and **signac-flow**: A case study on projectile motion ([interactive notebook](https://mybinder.org/v2/gh/csadorf/pydata-ann-arbor-2018/master?urlpath=lab/tree/projectile/animate-projectile.ipynb), [source](projectile/animate-projectile.ipynb))
* Part 3 - The Python Ecosystem: Integrating **signac** with other Python tools, including [pandas](https://pandas.pydata.org/), [Sacred](https://github.com/IDSIA/sacred), and [datreant.core](http://datreant.org) ([interactive notebook](https://mybinder.org/v2/gh/csadorf/pydata-ann-arbor-2018/master?urlpath=lab/tree/integration/Integration.ipynb), [source](integration/Integration.ipynb))

## How to install signac

You can install signac either with [conda](https://conda.io/docs/user-guide/install/download.html) through the [conda-forge](https://conda-forge.org/) channel:
```bash
conda install -c conda-forge signac signac-flow
```
Alternatively you can install it with [pip](https://packaging.python.org/tutorials/installing-packages/#installing-to-the-user-site):
```bash
pip install --user signac signac-flow
```

## How to get help

For more information visit the [signac website](http://www.signac.io) or the [framework documentation](https://signac-docs.readthedocs.io/en/latest).

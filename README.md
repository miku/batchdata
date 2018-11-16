# batchdata

Batch data processing with luigi. A short introduction.

Workshop at PyCon Balkan, Belgrade, 2018-11-17, 17:00-18:30

![](images/luigi8.png)

# Setup

* Python 3 (3.6.4)

Clone (or fork) this repo:

```
$ git clone https://github.com/miku/batchdata.git
$ cd batchdata
```

Prepare your isolated setup and install the requirements:

```
$ pip install -r requirements.txt
```

# History

* Python framework open sourced by Spotify in September 24th, 2012

> It's a Python module that helps you build complex pipelines of batch jobs,
> handle dependency resolution, and create visualizations to help manage
> multiple workflows. Luigi comes with Hadoop support built in.

> We use Luigi internally at Spotify to run thousands of tasks every day,
> organized in complex dependency graphs. Luigi provides an infrastructure that
> powers several Spotify features including recommendations, top lists, A/B test
> analysis, external reports, internal dashboards, and many more.

Conceptually, Luigi is similar to GNU Make where you have certain tasks and
these tasks in turn may have dependencies on other tasks.

In 2018, one of the original authors works on other interesting things - and
there are more alternatives and sites for this problem.

# User list

* https://github.com/spotify/luigi#who-uses-luigi

# Extensions, Branches

* https://github.com/pharmbio/sciluigi

> A light-weight wrapper library around Spotify's Luigi workflow system to make
> writing scientific workflows more fluent, flexible and modular.

* https://github.com/scipipe/scipipe, http://scipipe.org/

> SciPipe is a library for writing Scientific Workflows, sometimes also called
> "pipelines", in the Go programming language.
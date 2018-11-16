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

* Python framework open sourced by Spotify [September 24th,
  2012](https://developer.spotify.com/community/news/2012/09/24/hello-world/)

> It's a Python module that helps you build complex pipelines of batch jobs,
> handle dependency resolution, and create visualizations to help manage
> multiple workflows. Luigi comes with Hadoop support built in.

> We use Luigi internally at Spotify to run thousands of tasks every day,
> organized in complex dependency graphs. Luigi provides an infrastructure that
> powers several Spotify features including recommendations, top lists, A/B test
> analysis, external reports, internal dashboards, and many more.

Conceptually, Luigi is similar to [GNU Make](https://www.gnu.org/software/make/)
where you have certain tasks and these tasks in turn may have dependencies on
other tasks.

In 2018, one of the original authors works on other interesting things - and
there are more alternatives and sites for this problem.

It's a small open-source project, with currently 10435 stars on GitHub, 537
people on the mailing list with about 905 topics.

# User list

* https://github.com/spotify/luigi#who-uses-luigi

Example uses:

* Processing Hotel Reviews with Python
* Create index of scientific articles of heterogeneous sources
*

# Random things from the mailing list

## Can Luigi replace my clunky build framework?

> Over the last decade or so I implemented my own dependency 'pipeline'
> framework for scientific computing, and it is in desperate need of a major
> overhaul that I would rather not do (well mostly not).  I've just discovered
> Luigi which is surprisingly similar in concept, but much much more solid and
> complete

## Open source projects that use Luigi

> I'm refactoring an ETL process which is built on Luigi and am rethinking our
project organization. One of our most common tasks is to standardize and
integrate a given type of dataset as acquired from dozens of different sources
in various formats. An example may be building a nationwide database of
property records by acquiring, standardizing, and integrating property records
from dozens or hundreds of local governments, all of which have completely
different source formats.


# Extensions, Branches

* https://github.com/pharmbio/sciluigi

> A light-weight wrapper library around Spotify's Luigi workflow system to make
> writing scientific workflows more fluent, flexible and modular.

* https://github.com/scipipe/scipipe, http://scipipe.org/

> SciPipe is a library for writing Scientific Workflows, sometimes also called
> "pipelines", in the Go programming language.

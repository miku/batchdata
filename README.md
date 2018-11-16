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

----

> I'm refactoring an **ETL process** which is built on Luigi and am rethinking our
> project organization. One of our most common tasks is to standardize and
> integrate a given type of dataset as acquired from dozens of different sources
> in various formats. **An example may be building a nationwide database of
> property records by acquiring, standardizing, and integrating property records
> from dozens or hundreds of local governments, all of which have completely
> different source formats**. 

> I'd love study some sizable open-source projects that use Luigi, especially
those with a similar use case. I'm looking for approaches to things like
packaging and deploying pipelines, test organization, separation of Luigi tasks
from utility/processing functions, organizing modules and sub-packages, design
patterns for reusing tasks that handle variable input formats and produce
standardized outputs, etc.

So far I've found the following projects:

* Open edX Data Pipeline: https://github.com/edx/edx-analytics-pipeline
* FBI Crime Data API: https://github.com/fbi-cde/crime-data-api
* siskin: https://github.com/miku/siskin

Are there other well-organized open source projects worth browsing?

----
"""
Basic example, a minimal task and command line integration.

Fill in the blanks.

Run:

    $ python main.py

Luigi requires a scheduler and comes with a local scheduler for development.

    $ python main.py --local-scheduler

Specify the task name (name of the class) to execute:

    $ python main.py <taskname> --local-scheduler

"""

import luigi

# 1. Write a class (e.g. `Hello`) that inherits from `luigi.Task`
# 2. Add a `run` method that prints some string.

if __name__ == '__main__':
    luigi.run()

